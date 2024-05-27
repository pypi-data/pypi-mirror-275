import math
import random
import unittest

import networkx as nx
# noinspection PyUnresolvedReferences
import pytest
# noinspection PyUnresolvedReferences
import pytest_socket

from metricX import symmetry as sym


class TestInHouseSymmetry(unittest.TestCase):

    def test_empty_graph(self):
        g = nx.Graph()
        symmetry = sym.visual_symmetry(g)
        print(symmetry)
        assert symmetry == 1

    def test_single_node(self):
        g = nx.Graph()
        symmetry = sym.visual_symmetry(g)
        g.add_node(1, pos=(123, -45))
        print(symmetry)
        assert symmetry == 1

    def test_cycle_close_to_one(self):
        g = nx.Graph()

        for i in range(0, 360):
            g.add_node(i, pos=(math.sin(math.radians(i)), math.cos(math.radians(i))))

        symmetry = sym.visual_symmetry(g)
        print(symmetry)
        assert symmetry > 0.95

    def test_cycle_with_edges_close_to_one(self):
        g = nx.Graph()

        for i in range(0, 360):
            g.add_node(i, pos=(math.sin(math.radians(i)), math.cos(math.radians(i))))
            if i < 360 - 1:
                g.add_edge(i, i + 1)

        symmetry = sym.visual_symmetry(g)
        print(symmetry)
        assert symmetry > 0.95

    def test_rectangle_close_to_one(self):
        g = nx.Graph()

        for i in range(50):
            g.add_node(i, pos=(0, i))
            g.add_node(i + 50, pos=(50, i))

        for i in range(50):
            g.add_node(i + 100, pos=(i, 0))
            g.add_node(i + 150, pos=(i, 50))

        symmetry = sym.visual_symmetry(g)
        print(symmetry)
        assert symmetry > 0.95

    def test_simple_rectangle_close_to_one(self):
        g = nx.Graph()

        g.add_node(1, pos=(-1, -1))
        g.add_node(2, pos=(-1, 1))
        g.add_node(3, pos=(1, 1))
        g.add_node(4, pos=(1, -1))
        g.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1)])

        symmetry = sym.visual_symmetry(g)
        print(symmetry)
        assert symmetry > 0.95

    def test_big_random_graph_undirected_is_deterministic(self):
        graph_size = 100
        random.seed(2308590348590)
        g = nx.fast_gnp_random_graph(graph_size, 0.5, 30219490182903)
        random_embedding = {n: [random.randint(-10000, 10000), random.randint(-10000, 10000)] for n in
                            range(0, graph_size + 1)}
        symmetry_a = sym.visual_symmetry(g, random_embedding)
        symmetry_b = sym.visual_symmetry(g, random_embedding)
        print(symmetry_a)
        print(symmetry_b)
        print(symmetry_a - symmetry_b)
        assert abs(symmetry_a - symmetry_b) < 1e-08

    def test_big_random_graph_directed_is_deterministic(self):
        graph_size = 25
        random.seed(9132809123)
        g = nx.fast_gnp_random_graph(graph_size, 0.5, 2348923409890890123, True)
        random_embedding = {n: [random.randint(-10000, 10000), random.randint(-10000, 10000)] for n in
                            range(0, graph_size + 1)}

        symmetry_a = sym.visual_symmetry(g, random_embedding)
        symmetry_b = sym.visual_symmetry(g, random_embedding)
        print(symmetry_a)
        print(symmetry_b)
        print(symmetry_a - symmetry_b)
        assert abs(symmetry_a - symmetry_b) < 1e-08
