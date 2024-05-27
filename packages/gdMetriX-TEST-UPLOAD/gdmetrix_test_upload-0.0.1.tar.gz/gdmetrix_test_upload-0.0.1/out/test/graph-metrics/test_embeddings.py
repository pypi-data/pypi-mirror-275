import math
import unittest

import networkx as nx
# noinspection PyUnresolvedReferences
import pytest

from metricX import edge_directions


# noinspection PyUnresolvedReferences


class TestCombinatorialEmbedding(unittest.TestCase):

    def test_star(self):
        g = nx.Graph()
        g.add_node('center', pos=(0, 0))

        for i in range(1, 36):
            g.add_node(i, pos=(math.sin(math.radians(i * 10)), math.cos(math.radians(i * 10))))
            g.add_edge('center', i)

        embedding = edge_directions.combinatorial_embedding(g)
        print(embedding)

        assert len(embedding) == 36
        assert len(embedding['center']) == 35
        assert embedding['center'] == sorted(range(1, 36))

    def test_multigraph(self):
        g = nx.MultiGraph()
        g.add_node(0, pos=(0, 0))
        g.add_node(1, pos=(1, 0))
        g.add_node(2, pos=(0, -1))
        g.add_node(3, pos=(-1, 0))
        g.add_edges_from([(0, 1), (0, 2), (0, 3), (0, 2)])

        embedding = edge_directions.combinatorial_embedding(g)
        print(embedding)

        assert len(embedding) == 4
        assert len(embedding[0]) == 4
        assert embedding[0] == [1, 2, 2, 3]

    def test_self_loop_not_included(self):
        g = nx.MultiGraph()
        g.add_node(0, pos=(0, 0))
        g.add_node(1, pos=(1, 1))
        g.add_edges_from([(0, 0), (0, 1)])

        embedding = edge_directions.combinatorial_embedding(g)
        print(embedding)

        assert len(embedding) == 2
        assert len(embedding[0]) == 1


class TestEdgeAngles(unittest.TestCase):

    def test_star(self):
        g = nx.Graph()
        g.add_node('center', pos=(0, 0))

        for i in range(0, 36):
            g.add_node(i, pos=(math.cos(math.radians(i * 10)), math.sin(math.radians(i * 10))))
            g.add_edge('center', i)

        angles = edge_directions.edge_angles(g, 'center', deg=True)
        print(angles)
        assert len(angles) == 36

        for angle in angles:
            assert math.isclose(angle, 10)

    def test_two_simple_edges(self):
        g = nx.Graph()
        g.add_node(1, pos=(1, 1))
        g.add_node(2, pos=(1, 2))
        g.add_node(3, pos=(2, 2))

        g.add_edges_from([(1, 2), (1, 3)])

        angles = edge_directions.edge_angles(g, 1, deg=True)
        print(angles)
        embedding = edge_directions.combinatorial_embedding(g)
        print(embedding)
        assert len(angles) == 2
        angles = sorted(angles)
        assert math.isclose(angles[0], 45)
        assert math.isclose(angles[1], 360 - 45)

    def test_four_edges(self):
        g = nx.Graph()
        g.add_node(1, pos=(0, 0))
        g.add_node(2, pos=(-0.5, 1))
        g.add_node(3, pos=(+0.5, 1))

        g.add_node(4, pos=(1, 0))
        g.add_node(5, pos=(-1, 0))

        g.add_edges_from([(1, 2), (1, 3), (1, 4), (1, 5)])

        offset_angle = 63.43494882292201  # angle between 3 and 4

        angles = edge_directions.edge_angles(g, 1, deg=True)
        print(angles)

        assert len(angles) == 4

        assert math.isclose(angles[0], offset_angle)
        assert math.isclose(angles[1], 180)
        assert math.isclose(angles[2], offset_angle)
        assert math.isclose(angles[3], 180 - 2 * offset_angle)

    def test_single_edge(self):
        g = nx.Graph()
        g.add_node(1, pos=(92, 934))
        g.add_node(2, pos=(9, 23.3))
        g.add_edge(1, 2)

        angles = edge_directions.edge_angles(g, 1, deg=True)
        print(angles)

        assert len(angles) == 1
        assert math.isclose(angles[0], 360)


class TestAngularResolution(unittest.TestCase):

    def test_star(self):
        g = nx.Graph()
        g.add_node('center', pos=(0, 0))

        for i in range(0, 36):
            g.add_node(i, pos=(math.cos(math.radians(i * 10)), math.sin(math.radians(i * 10))))
            g.add_edge('center', i)

        resolution = edge_directions.angular_resolution(g, deg=True)

        assert math.isclose(resolution, 10)

    def test_two_simple_edges(self):
        g = nx.Graph()
        g.add_node(1, pos=(1, 1))
        g.add_node(2, pos=(1, 2))
        g.add_node(3, pos=(2, 2))

        g.add_edges_from([(1, 2), (1, 3)])

        angles = edge_directions.edge_angles(g, 1, deg=True)

        resolution = edge_directions.angular_resolution(g, deg=True)

        assert math.isclose(resolution, 45)

    def test_four_edges(self):
        g = nx.Graph()
        g.add_node(1, pos=(0, 0))
        g.add_node(2, pos=(-0.5, 1))
        g.add_node(3, pos=(+0.5, 1))

        g.add_node(4, pos=(1, 0))
        g.add_node(5, pos=(-1, 0))

        g.add_edges_from([(1, 2), (1, 3), (1, 4), (1, 5)])

        resolution = edge_directions.angular_resolution(g, deg=True)

        assert resolution == 53.13010235415598

    def test_single_edge(self):
        g = nx.Graph()
        g.add_node(1, pos=(92, 934))
        g.add_node(2, pos=(9, 23.3))
        g.add_edge(1, 2)

        resolution = edge_directions.angular_resolution(g)

        assert math.isclose(resolution, math.pi * 2)
