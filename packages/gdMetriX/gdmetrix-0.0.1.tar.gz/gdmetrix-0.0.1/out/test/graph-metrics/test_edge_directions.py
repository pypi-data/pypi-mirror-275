import math
import unittest

import networkx as nx
# noinspection PyUnresolvedReferences
import pytest
# noinspection PyUnresolvedReferences
import pytest_socket

from metricX import edge_directions


class TestUpwardsFlow(unittest.TestCase):

    def test_empty_graph(self):
        g = nx.DiGraph()

        flow = edge_directions.upwards_flow(g)

        assert flow == 0

    def test_singleton(self):
        g = nx.DiGraph()
        g.add_node(1, pos=(213, 1.2))

        flow = edge_directions.upwards_flow(g)

        assert flow == 0

    def test_undirected_graph(self):
        g = nx.Graph()
        g.add_node(1, pos=(21, 29))
        g.add_node(2, pos=(0, 0))
        g.add_node(3, pos=(12, 0.4))
        g.add_edges_from([(1, 2), (1, 3), (2, 3)])

        # noinspection PyTypeChecker
        flow = edge_directions.upwards_flow(g)

        assert flow == 0

    def test_single_edge_1(self):
        g = nx.DiGraph()
        g.add_node(1, pos=(0, 0))
        g.add_node(2, pos=(0, 1))
        g.add_edge(1, 2)

        flow = edge_directions.upwards_flow(g)

        assert flow == 1

    def test_single_edge_2(self):
        g = nx.DiGraph()
        g.add_node(1, pos=(0, 0))
        g.add_node(2, pos=(1, 1))
        g.add_edge(1, 2)

        flow = edge_directions.upwards_flow(g)

        assert flow == 1

    def test_single_edge_different_upwards_direction(self):
        g = nx.DiGraph()
        g.add_node(1, pos=(0, 0))
        g.add_node(2, pos=(0, 1))
        g.add_edge(1, 2)

        flow = edge_directions.upwards_flow(g, direction_vector=(0, -1))

        assert flow == 0

    def test_single_edge_different_upwards_direction_2(self):
        g = nx.DiGraph()
        g.add_node(1, pos=(0, 0))
        g.add_node(2, pos=(1, 1))
        g.add_edge(1, 2)

        flow = edge_directions.upwards_flow(g, direction_vector=(0, -1))

        assert flow == 0

    def test_orthogonal_edge_not_counted(self):
        g = nx.DiGraph()
        g.add_node(1, pos=(0, 0))
        g.add_node(2, pos=(0, 1))
        g.add_node(3, pos=(5, 5))
        g.add_node(4, pos=(6, 5))
        g.add_edges_from([(1, 2), (3, 4)])

        flow = edge_directions.upwards_flow(g)

        assert flow == 0.5

    def test_orthogonal_edge_not_counted_custom_direction(self):
        g = nx.DiGraph()
        g.add_node(1, pos=(0, 0))
        g.add_node(2, pos=(0, 1))
        g.add_node(3, pos=(5, 5))
        g.add_node(4, pos=(4, 6))
        g.add_edges_from([(1, 2), (3, 4)])

        flow = edge_directions.upwards_flow(g, direction_vector=(1, 1))

        assert flow == 0.5


class TestAverageFlow(unittest.TestCase):

    def test_empty_graph(self):
        g = nx.DiGraph()

        average_flow = edge_directions.average_flow(g)
        print(average_flow)

        assert average_flow is None

    def test_singleton(self):
        g = nx.DiGraph()
        g.add_node(1, pos=(213, 1.2))

        average_flow = edge_directions.average_flow(g)
        print(average_flow)

        assert average_flow is None

    def test_undirected_graph(self):
        g = nx.Graph()
        g.add_node(1, pos=(21, 29))
        g.add_node(2, pos=(0, 0))
        g.add_node(3, pos=(12, 0.4))
        g.add_edges_from([(1, 2), (1, 3), (2, 3)])

        # noinspection PyTypeChecker
        average_flow = edge_directions.average_flow(g)
        print(average_flow)

        assert average_flow is None

    def test_opposite_vectors(self):
        g = nx.DiGraph()
        g.add_node(1, pos=(-1, -1))
        g.add_node(2, pos=(1, 1))
        g.add_node(3, pos=(0, 0))
        g.add_edges_from([(3, 1), (3, 2)])

        average_flow = edge_directions.average_flow(g)
        print(average_flow)

        assert average_flow[0] == 0
        assert average_flow[1] == 0

    def test_opposite_vectors_2(self):
        g = nx.DiGraph()
        g.add_node(1, pos=(-2, -2))
        g.add_node(2, pos=(1, 1))
        g.add_node(3, pos=(0, 0))
        g.add_edges_from([(3, 1), (3, 2)])

        average_flow = edge_directions.average_flow(g)
        print(average_flow)

        assert average_flow[0] == 0
        assert average_flow[1] == 0

    def test_single_edge_1(self):
        g = nx.DiGraph()
        g.add_node(1, pos=(1, 1))
        g.add_node(2, pos=(5, 5))
        g.add_edge(1, 2)

        average_flow = edge_directions.average_flow(g)
        print(average_flow)

        assert math.isclose(average_flow[0], math.cos(math.pi / 4))
        assert math.isclose(average_flow[1], math.sin(math.pi / 4))

    def test_single_edge_2(self):
        g = nx.DiGraph()
        g.add_node(1, pos=(1, 1))
        g.add_node(2, pos=(1.1, 1.1))
        g.add_edge(1, 2)

        average_flow = edge_directions.average_flow(g)
        print(average_flow)

        assert math.isclose(average_flow[0], math.cos(math.pi / 4))
        assert math.isclose(average_flow[1], math.sin(math.pi / 4))

    def test_single_edge_3(self):
        g = nx.DiGraph()
        g.add_node(1, pos=(-1, -1))
        g.add_node(2, pos=(-1.5, -1))
        g.add_edge(1, 2)

        average_flow = edge_directions.average_flow(g)
        print(average_flow)

        assert average_flow[0] == -1
        assert average_flow[1] == 0

    def test_single_edge_4(self):
        g = nx.DiGraph()
        g.add_node(1, pos=(-1, -1))
        g.add_node(2, pos=(-1, -0.9))
        g.add_edge(1, 2)

        average_flow = edge_directions.average_flow(g)
        print(average_flow)

        assert average_flow[0] == 0
        assert average_flow[1] == 1

    def test_coherence_to_average_flow(self):
        g = nx.DiGraph()
        g.add_node(1, pos=(1, 1))
        g.add_node(2, pos=(0, 0))
        g.add_edge(1, 2)

        coherence = edge_directions.coherence_to_average_flow(g)

        assert coherence == 1

    def test_coherence_to_average_flow_2(self):
        g = nx.DiGraph()
        g.add_node(1, pos=(1, 1))
        g.add_node(2, pos=(0, 0))
        g.add_node(3, pos=(2, 2))
        g.add_edge(1, 2)
        g.add_edge(2, 3)

        coherence = edge_directions.coherence_to_average_flow(g)

        assert coherence is None


class TestEdgeOrthogonality(unittest.TestCase):

    def test_horizontal_edge(self):
        g = nx.DiGraph()
        g.add_node(1, pos=(1, 1))
        g.add_node(2, pos=(2, 1))
        g.add_edge(1, 2)

        orthogonality = edge_directions.edge_orthogonality(g)

        assert math.isclose(orthogonality, 1)

    def test_vertical_edge(self):
        g = nx.DiGraph()
        g.add_node(1, pos=(1, 2))
        g.add_node(2, pos=(1, 1))
        g.add_edge(1, 2)

        orthogonality = edge_directions.edge_orthogonality(g)

        assert math.isclose(orthogonality, 1)

    def test_45_degree_edge(self):
        g = nx.DiGraph()
        g.add_node(1, pos=(1, 1))
        g.add_node(2, pos=(2, 2))
        g.add_edge(1, 2)

        orthogonality = edge_directions.edge_orthogonality(g)

        assert math.isclose(orthogonality, 0)

    def test_45_degree_edge_2(self):
        g = nx.DiGraph()
        g.add_node(1, pos=(1, 1))
        g.add_node(2, pos=(2, 0))
        g.add_edge(1, 2)

        orthogonality = edge_directions.edge_orthogonality(g)

        assert math.isclose(orthogonality, 0)

    def test_inbetween_edge(self):
        g = nx.Graph()
        g.add_node(1, pos=(0, 0))
        g.add_node(2, pos=(math.cos(math.pi / 8), math.sin(math.pi / 8)))
        g.add_edge(1, 2)

        orthogonality = edge_directions.edge_orthogonality(g)

        assert math.isclose(orthogonality, 0.5)

    def test_inbetween_edge_2(self):
        g = nx.Graph()
        g.add_node(1, pos=(0, 0))
        g.add_node(2, pos=(math.sin(math.pi / 16), math.cos(math.pi / 16)))
        g.add_edge(1, 2)

        orthogonality = edge_directions.edge_orthogonality(g)

        assert math.isclose(orthogonality, 0.75)
