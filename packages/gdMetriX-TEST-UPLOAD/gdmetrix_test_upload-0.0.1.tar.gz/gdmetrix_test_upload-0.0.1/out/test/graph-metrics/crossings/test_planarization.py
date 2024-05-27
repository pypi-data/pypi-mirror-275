import unittest

import networkx as nx
# noinspection PyUnresolvedReferences
import pytest
# noinspection PyUnresolvedReferences
import pytest_socket

from metricX import crossings


class TestPlanarization(unittest.TestCase):

    def test_non_crossing_graph(self):
        g = nx.Graph()
        g.add_node(1, pos=(1, 1))
        g.add_node(2, pos=(3, 3))
        g.add_node(3, pos=(3, 1))
        g.add_node(4, pos=(4, 1))
        g.add_node(5, pos=(5, 4))
        g.add_node(6, pos=(1, 3))
        g.add_node(7, pos=(3, 5))
        g.add_node(8, pos=(4, 2))
        g.add_node(9, pos=(6, 5))
        g.add_node(10, pos=(8, 5))
        g.add_edges_from([(1, 2), (2, 3), (2, 5), (2, 7), (4, 5), (5, 7), (6, 7), (9, 10)])

        planar_g = g.copy()
        crossings.planarize(planar_g)

        assert g.nodes() == planar_g.nodes()
        assert g.edges() == planar_g.edges()

    def test_simple_crossing(self):
        g = nx.Graph()
        g.add_node(1, pos=(0, 0))
        g.add_node(2, pos=(1, 0))
        g.add_node(3, pos=(1, 1))
        g.add_node(4, pos=(0, 1))
        g.add_edges_from([
            (1, 3), (2, 4)
        ])

        planar_g = g.copy()
        crossings.planarize(planar_g)
        assert len(planar_g.nodes()) == 5

        correct_node_exists = False
        for node, data in planar_g.nodes(data=True):
            if data['pos'] == (0.5, 0.5):
                if sorted(nx.all_neighbors(planar_g, node)) == [1, 2, 3, 4]:
                    correct_node_exists = True

        assert correct_node_exists

    def test_vertex_at_edge(self):
        g = nx.Graph()
        g.add_node(1, pos=(0, 0))
        g.add_node(2, pos=(0, 2))
        g.add_node(3, pos=(0, 1))
        g.add_node(4, pos=(1, 1))
        g.add_edges_from([(1, 2), (3, 4)])

        planar_g = g.copy()
        crossings.planarize(planar_g, include_node_crossings=True)
        assert len(planar_g.nodes()) == 4

        correct_node_exists = False
        for node, data in planar_g.nodes(data=True):
            if data['pos'] == (0, 1):
                if sorted(nx.all_neighbors(planar_g, node)) == [1, 2, 4]:
                    correct_node_exists = True

        assert correct_node_exists is True

    def test_vertex_at_edge_2(self):
        g = nx.Graph()
        g.add_node(1, pos=(0, 0))
        g.add_node(2, pos=(0, 2))
        g.add_node(3, pos=(0, 1))
        g.add_node(4, pos=(1, 1))
        g.add_edges_from([(1, 2), (3, 4)])

        planar_g = g.copy()
        crossings.planarize(planar_g, include_node_crossings=False)
        assert len(planar_g.nodes()) == 4
        assert len(planar_g.edges()) == 2

    def test_multiple_edges_at_crossing(self):
        g = nx.Graph()
        g.add_node(1, pos=(-1, 1))
        g.add_node(2, pos=(0, 1))
        g.add_node(3, pos=(1, 1))
        g.add_node(4, pos=(-1, 0))
        g.add_node(5, pos=(1, 0))
        g.add_node(6, pos=(-1, -1))
        g.add_node(7, pos=(0, -1))
        g.add_node(8, pos=(1, -1))
        edges = [(1, 8), (2, 7), (3, 6), (4, 5)]
        g.add_edges_from(edges)

        planar_g = g.copy()
        crossings.planarize(planar_g)
        assert len(planar_g.nodes()) == 9

        correct_node_exists = False
        for node, data in planar_g.nodes(data=True):
            if data['pos'] == (0, 0):
                if sorted(nx.all_neighbors(planar_g, node)) == [1, 2, 3, 4, 5, 6, 7, 8]:
                    correct_node_exists = True

        assert correct_node_exists is True

    def test_edge_with_multiple_crossings(self):
        g = nx.Graph()
        g.add_node(1, pos=(0, 0))
        g.add_node(2, pos=(3, 0))
        g.add_node(3, pos=(1, 1))
        g.add_node(4, pos=(1, -1))
        g.add_node(5, pos=(2, 1))
        g.add_node(6, pos=(2, -1))

        g.add_edges_from([(1, 2), (3, 4), (5, 6)])

        crossings.planarize(g)

        assert g.order() == 8
        assert len(g.edges()) == 7
