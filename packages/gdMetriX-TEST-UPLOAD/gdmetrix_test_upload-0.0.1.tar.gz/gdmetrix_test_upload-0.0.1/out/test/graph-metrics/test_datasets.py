import os
import unittest

# noinspection PyUnresolvedReferences
import pytest
# noinspection PyUnresolvedReferences
import pytest_socket

from metricX import datasets


def __test_graph_list__(graphs):
    has_elements = False
    for name, graph in graphs:
        assert name is not None
        assert graph is not None
        assert len(graph.nodes())
        has_elements = True

    assert has_elements


class TestBenchmarkDataset(unittest.TestCase):

    def __init__(self):
        super().__init__()
        x = 1 / 0

    @pytest.mark.xdist_group("benchmark_group")
    def test_get_list_of_available_files(self):
        available_datasets = datasets.get_available_datasets()
        assert len(available_datasets) > 0

        for dataset in available_datasets:
            assert dataset != ""

        assert len(available_datasets) == len(set(available_datasets))

    @pytest.mark.xdist_group("benchmark_group")
    def test_adapt_parameters(self):
        available_datasets = datasets.get_available_datasets()

        assert len(available_datasets) > 0

        for dataset_name in available_datasets:
            print(dataset_name)
            __test_graph_list__(datasets.iterate_dataset(dataset_name))

    @pytest.mark.xdist_group("benchmark_group")
    def test_do_not_adapt_parameters(self):
        available_datasets = datasets.get_available_datasets()

        assert len(available_datasets) > 0

        for dataset_name in available_datasets:
            print(dataset_name)
            __test_graph_list__(datasets.iterate_dataset(dataset_name))

    @pytest.mark.xdist_group("benchmark_group")
    def test_try_getting_non_existent_dataset(self):
        def _call_non_existent_list():
            for _ in datasets.iterate_dataset("I definitely do not exist"):
                pass

        self.assertRaises(KeyError, _call_non_existent_list)

    @pytest.mark.xdist_group("benchmark_group")
    def test_clean_cache_same_result(self):
        # Make sure it is already preloaded
        datasets.get_available_datasets()

        available_datasets = datasets.get_available_datasets()

        datasets.clear_cache()

        available_datasets_2 = datasets.get_available_datasets()

        assert available_datasets == available_datasets_2

    @pytest.mark.xdist_group("benchmark_group")
    def test_clean_cache_empty_folder(self):
        datasets.iterate_dataset(datasets.get_available_datasets()[0])
        assert len(os.listdir(datasets.__get_data_dir__())) > 0

        datasets.clear_cache()

        assert (not datasets.__get_data_dir__().exists()
                or len(os.listdir(datasets.__get_data_dir__())) == 0)

    @pytest.mark.xdist_group("benchmark_group")
    def test_get_list_of_graph_fresh_download(self):
        datasets.clear_cache()
        scrape = datasets.iterate_dataset(datasets.get_available_datasets()[0])
        __test_graph_list__(scrape)

    @pytest.mark.xdist_group("benchmark_group")
    def test_get_list_of_graph_get_from_cache(self):
        datasets.clear_cache()

        first_scrape = datasets.iterate_dataset(datasets.get_available_datasets()[0])
        __test_graph_list__(first_scrape)

        second_scrape = datasets.iterate_dataset(datasets.get_available_datasets()[0])
        __test_graph_list__(second_scrape)

    @pytest.mark.xdist_group("benchmark_group")
    def test_disable_sockets_should_not_throw_after_cache(self):
        pytest_socket.enable_socket()
        datasets.get_available_datasets()
        pytest_socket.disable_socket()
        available_datasets = datasets.get_available_datasets()
        assert len(available_datasets) > 0
        pytest_socket.enable_socket()

    @pytest.mark.xdist_group("benchmark_group")
    def test_disable_sockets_should_not_throw_after_cache_2(self):
        pytest_socket.enable_socket()

        # Make sure all graphs are downloaded from that dataset
        for _ in datasets.iterate_dataset(datasets.get_available_datasets()[0]):
            pass

        pytest_socket.disable_socket()

        second_scrape = datasets.iterate_dataset(datasets.get_available_datasets()[0])
        __test_graph_list__(second_scrape)

        pytest_socket.enable_socket()
