"""
    Unit tests for crossing detection.
"""

import inspect
import math
import random
import unittest

import matplotlib.pyplot as plt
import networkx as nx
# noinspection PyUnresolvedReferences
import pytest
# noinspection PyUnresolvedReferences
import pytest_socket

import metricX.common
from metricX import crossings


def __rotate_point__(point, angle):
    if isinstance(point, crossings.CrossingLine):
        return crossings.CrossingLine(__rotate_point__(point.point_a, angle),
                                      __rotate_point__(point.point_b, angle))
    if isinstance(point, crossings.CrossingPoint):
        return crossings.CrossingPoint(__rotate_point__((point[0], point[1]), angle)[0],
                                       __rotate_point__((point[0], point[1]), angle)[1])
    rad = math.radians(angle % 360)
    return (point[0] * math.cos(rad) - point[1] * math.sin(rad),
            point[0] * math.sin(rad) + point[1] * math.cos(rad))


def __rotate_graph__(g, angle):
    for node, position in nx.get_node_attributes(g, "pos").items():
        g.nodes[node]["pos"] = __rotate_point__(position, angle)


def __rotate_crossings__(crossing_list, angle):
    return [crossings.Crossing(
        __rotate_point__(crossing.pos, angle), crossing.involved_edges)
        for crossing in crossing_list]


def __draw_graph__(g: nx.Graph, title: str, crossings_a, crossings_b):
    ax = plt.gca()
    ax.set_title(title)

    pos = metricX.common.get_node_positions(g)

    # nx.draw_networkx(g, pos=nx.get_node_attributes(g, "pos"), ax=ax)
    nx.draw_networkx_edges(g, pos, ax=ax)
    nx.draw_networkx_nodes(g, pos, ax=ax, node_size=20)
    ax.tick_params(left=True, bottom=True, labelleft=True, labelbottom=True)
    plt.axis("on")

    # Points
    points_a = list(filter(lambda cr: type(cr.pos) is metricX.crossings.crossingDataTypes.CrossingPoint, crossings_a))
    points_b = list(filter(lambda cr: type(cr.pos) is metricX.crossings.crossingDataTypes.CrossingPoint, crossings_b))

    x_values = [point.pos[0] for point in points_a]
    y_values = [point.pos[1] for point in points_a]
    plt.plot(x_values, y_values, 'rX', markersize=12)

    x_values = [point.pos[0] for point in points_b]
    y_values = [point.pos[1] for point in points_b]
    plt.plot(x_values, y_values, 'gX', markersize=9)

    plt.show()


def __equal_crossings__(crossings_a, crossings_b, g, title):
    print("Expected {}".format(crossings_b))
    print("Actual   {}".format(crossings_a))

    if sorted(crossings_b) != sorted(crossings_a):
        __draw_graph__(g, title, crossings_a, crossings_b)

    # assert len(crossings_a) == len(crossings_b)
    assert sorted(crossings_a) == sorted(crossings_b)


def __assert_crossing_equality__(g, crossing_list, include_rotation: bool = False,
                                 include_node_crossings: bool = False):
    title = inspect.getouterframes(inspect.currentframe(), 2)[1][3]
    __equal_crossings__(crossings.get_crossings(g, include_node_crossings=include_node_crossings), crossing_list,
                        g, title)
    angle_resolution = 10
    if include_rotation:
        for i in range(0, int(360 / angle_resolution)):
            __rotate_graph__(g, angle_resolution)
            crossing_list = __rotate_crossings__(crossing_list, 10)
            print(nx.get_node_attributes(g, "pos"))
            __equal_crossings__(crossings.get_crossings(g, include_node_crossings=include_node_crossings),
                                crossing_list, g, title)


class TestSimpleCrossings(unittest.TestCase):

    def test_empty_graph(self):
        g = nx.Graph()
        __assert_crossing_equality__(g, [])

    def test_singleton(self):
        g = nx.Graph()
        g.add_node(1, pos=(0, 0))
        __assert_crossing_equality__(g, [])

    def test_non_crossing_graph_without_verticals_or_horizontals(self):
        g = nx.Graph()
        g.add_node(1, pos=(2, 7))
        g.add_node(2, pos=(4, 7))
        g.add_node(3, pos=(7, 7))
        g.add_node(4, pos=(4, 6))
        g.add_node(5, pos=(1, 4))
        g.add_node(6, pos=(2, 4))
        g.add_node(7, pos=(3, 4))
        g.add_node(8, pos=(5, 4))
        g.add_node(9, pos=(7, 4))
        g.add_node(10, pos=(2, 3))
        g.add_node(11, pos=(7, 3))
        g.add_node(12, pos=(3, 2))
        g.add_node(13, pos=(4, 2))
        g.add_node(14, pos=(5, 2))
        g.add_node(15, pos=(7, 2))
        g.add_node(16, pos=(1, 1))
        g.add_node(17, pos=(2, 1))
        g.add_node(18, pos=(5, 1))
        g.add_node(19, pos=(6, 1))
        g.add_node(20, pos=(2, 0))
        g.add_edges_from([
            (1, 5), (1, 7), (2, 9), (4, 8), (6, 13), (10, 16), (11, 18), (12, 17), (14, 20), (15, 19)
        ])
        __assert_crossing_equality__(g, [])

    def test_non_crossing_graph_1(self):
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
        __assert_crossing_equality__(g, [], True)

    def test_non_crossing_graph_2(self):
        g = nx.Graph()
        g.add_node(1, pos=(1, 1))
        g.add_node(2, pos=(9, 7))
        g.add_node(3, pos=(5, 7))
        g.add_node(4, pos=(5, 6))
        g.add_node(5, pos=(5, 5))
        g.add_node(6, pos=(5, 4))
        g.add_node(7, pos=(5, 3))
        g.add_node(8, pos=(5, 2))
        g.add_node(9, pos=(5, 1))
        g.add_edges_from([
            (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9),
            (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9)
        ])
        __assert_crossing_equality__(g, [], True)

    def test_simple_crossing_0(self):
        g = nx.Graph()
        g.add_node(1, pos=(0, 0))
        g.add_node(2, pos=(1, 0))
        g.add_node(3, pos=(1, 1))
        g.add_node(4, pos=(0, 1))
        g.add_edges_from([
            (1, 3), (2, 4)
        ])
        __assert_crossing_equality__(g, [crossings.Crossing(crossings.CrossingPoint(0.5, 0.5), [(1, 3), (2, 4)])])

    def test_simple_crossing_1(self):
        g = nx.Graph()
        g.add_node(1, pos=(0, 0))
        g.add_node(2, pos=(1, 0))
        g.add_node(3, pos=(1, 1))
        g.add_node(4, pos=(0, 1))
        g.add_edges_from([
            (1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)
        ])
        __assert_crossing_equality__(g, [crossings.Crossing(crossings.CrossingPoint(0.5, 0.5), [(1, 3), (2, 4)])])

    def test_simple_crossing_2(self):
        g = nx.Graph()
        g.add_node(1, pos=(1, 1))
        g.add_node(2, pos=(4, 4))
        g.add_node(3, pos=(1, 2))
        g.add_node(4, pos=(4, 5))
        g.add_node(5, pos=(1, 3))
        g.add_node(6, pos=(4, 6))
        g.add_node(7, pos=(1, 4))
        g.add_node(8, pos=(4, 7))
        g.add_node(9, pos=(3, 7))
        g.add_node(10, pos=(3, 1))
        g.add_edges_from([
            (1, 2), (3, 4), (5, 6), (7, 8), (9, 10)
        ])
        __assert_crossing_equality__(g, [
            crossings.Crossing(crossings.CrossingPoint(3, 3), [(1, 2), (9, 10)]),
            crossings.Crossing(crossings.CrossingPoint(3, 4), [(3, 4), (9, 10)]),
            crossings.Crossing(crossings.CrossingPoint(3, 5), [(5, 6), (9, 10)]),
            crossings.Crossing(crossings.CrossingPoint(3, 6), [(7, 8), (9, 10)]),

        ])

    def test_end_point_crossing(self):
        g = nx.Graph()
        g.add_node(1, pos=(0, 5))
        g.add_node(2, pos=(4, 5))
        g.add_node(3, pos=(0, 4))
        g.add_node(4, pos=(4, 4))
        g.add_node(5, pos=(2, 3))
        g.add_node(6, pos=(0, 0))
        g.add_node(7, pos=(4, 0))
        g.add_edges_from([
            (1, 5), (2, 5), (3, 7), (4, 6)
        ])
        __assert_crossing_equality__(g, [
            crossings.Crossing(crossings.CrossingPoint(2, 2), [(3, 7), (4, 6)])
        ])

    def test_non_crossing_graph_directed(self):
        g = nx.DiGraph()
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
        __assert_crossing_equality__(g, [], True)

    def test_crossing_graph_directed(self):
        g = nx.DiGraph()
        g.add_node(1, pos=(0, 0))
        g.add_node(2, pos=(1, 0))
        g.add_node(3, pos=(1, 1))
        g.add_node(4, pos=(0, 1))
        g.add_edges_from([
            (1, 3), (2, 4)
        ])
        __assert_crossing_equality__(g, [crossings.Crossing(crossings.CrossingPoint(0.5, 0.5), [(1, 3), (2, 4)])])

    def test_self_loop(self):
        g = nx.DiGraph()
        g.add_node(1, pos=(0, 0))
        g.add_edge(1, 1)

        __assert_crossing_equality__(g, [], True, True)

    def test_self_loop_in_edge(self):
        g = nx.DiGraph()
        g.add_node(1, pos=(0, 0))
        g.add_node(2, pos=(-1, 0))
        g.add_node(3, pos=(1, 0))
        g.add_edge(1, 1)
        g.add_edge(2, 3)

        __assert_crossing_equality__(g, [], True)

    def test_self_loop_in_edge_2(self):
        g = nx.DiGraph()
        g.add_node(1, pos=(0, 0))
        g.add_node(2, pos=(-1, 0))
        g.add_node(3, pos=(1, 0))
        g.add_edge(1, 1)
        g.add_edge(2, 3)

        __assert_crossing_equality__(g, [
            crossings.Crossing(crossings.CrossingPoint(0, 0), [(2, 3), (1, 1)])
        ], True, True)

    def test_self_loop_in_crossing(self):
        g = nx.DiGraph()
        g.add_node(1, pos=(0, 0))
        g.add_node(2, pos=(-1, -1))
        g.add_node(3, pos=(1, 1))
        g.add_node(4, pos=(-1, 1))
        g.add_node(5, pos=(1, -1))
        g.add_edges_from([(1, 1), (2, 3), (4, 5)])

        __assert_crossing_equality__(g, [
            crossings.Crossing(crossings.CrossingPoint(0, 0), [(2, 3), (4, 5)])
        ], True)

    def test_self_loop_in_crossing_2(self):
        g = nx.DiGraph()
        g.add_node(1, pos=(0, 0))
        g.add_node(2, pos=(-1, -1))
        g.add_node(3, pos=(1, 1))
        g.add_node(4, pos=(-1, 1))
        g.add_node(5, pos=(1, -1))
        g.add_edges_from([(1, 1), (2, 3), (4, 5)])

        __assert_crossing_equality__(g, [
            crossings.Crossing(crossings.CrossingPoint(0, 0), [(1, 1), (2, 3), (4, 5)])
        ], True, True)


class TestCrossingsInvolvingVertices(unittest.TestCase):

    def test_vertex_at_edge_1(self):
        g = nx.Graph()
        g.add_node(1, pos=(0, 0))
        g.add_node(2, pos=(0, 2))
        g.add_node(3, pos=(0, 1))
        g.add_node(4, pos=(1, 2))
        g.add_edges_from([(1, 2), (3, 4)])
        __assert_crossing_equality__(g, [crossings.Crossing(crossings.CrossingPoint(0, 1), [(1, 2), (3, 4)])],
                                     include_node_crossings=True)

    def test_vertex_at_edge_2(self):
        g = nx.Graph()
        g.add_node(1, pos=(0, 0))
        g.add_node(2, pos=(0, 2))
        g.add_node(3, pos=(0, 1))
        g.add_node(4, pos=(1, 1))
        g.add_edges_from([(1, 2), (3, 4)])
        __assert_crossing_equality__(g, [crossings.Crossing(crossings.CrossingPoint(0, 1), [(1, 2), (3, 4)])],
                                     include_node_crossings=True)

    def test_vertex_at_edge_3(self):
        g = nx.Graph()
        g.add_node(1, pos=(0, 0))
        g.add_node(2, pos=(0, 2))
        g.add_node(3, pos=(0, 1))
        g.add_node(4, pos=(1, 0))
        g.add_edges_from([(1, 2), (3, 4)])
        __assert_crossing_equality__(g, [crossings.Crossing(crossings.CrossingPoint(0, 1), [(1, 2), (3, 4)])],
                                     include_node_crossings=True)

    def test_vertex_at_edge_4(self):
        g = nx.Graph()
        g.add_node(1, pos=(0, 1))
        g.add_node(2, pos=(2, 1))
        g.add_node(3, pos=(1, 1))
        g.add_node(4, pos=(1, 0))

        g.add_edges_from([(1, 2), (3, 4)])
        __assert_crossing_equality__(g, [crossings.Crossing(crossings.CrossingPoint(1, 1), [(1, 2), (3, 4)])],
                                     include_node_crossings=True)

    def test_vertex_at_edge_5(self):
        g = nx.Graph()
        g.add_node(1, pos=(0, 1))
        g.add_node(2, pos=(2, 1))
        g.add_node(3, pos=(1, 1))
        g.add_node(4, pos=(0, 0))
        g.add_edges_from([(1, 2), (3, 4)])
        __assert_crossing_equality__(g, [crossings.Crossing(crossings.CrossingPoint(1, 1), [(1, 2), (3, 4)])],
                                     include_node_crossings=True)

    def test_vertex_at_edge_6(self):
        g = nx.Graph()
        g.add_node(1, pos=(0, 1))
        g.add_node(2, pos=(2, 1))
        g.add_node(3, pos=(1, 1))
        g.add_node(4, pos=(2, 0))
        g.add_edges_from([(1, 2), (3, 4)])
        __assert_crossing_equality__(g, [crossings.Crossing(crossings.CrossingPoint(1, 1), [(1, 2), (3, 4)])],
                                     include_node_crossings=True)

    def test_vertex_at_edge_7(self):
        g = nx.Graph()
        g.add_node(1, pos=(0, 1))
        g.add_node(2, pos=(2, 1))
        g.add_node(3, pos=(1, 1))
        g.add_node(4, pos=(1, 0))

        g.add_edges_from([(1, 2), (3, 4)])
        __assert_crossing_equality__(g, [crossings.Crossing(crossings.CrossingPoint(1, 1), [(1, 2), (3, 4)])], True,
                                     True)

    def test_vertex_at_edge_8(self):
        g = nx.Graph()
        g.add_node(1, pos=(0, 1))
        g.add_node(2, pos=(2, 1))
        g.add_node(3, pos=(1, 1))
        g.add_node(4, pos=(0, 0))
        g.add_edges_from([(1, 2), (3, 4)])
        __assert_crossing_equality__(g, [crossings.Crossing(crossings.CrossingPoint(1, 1), [(1, 2), (3, 4)])], True,
                                     True)

    def test_vertex_at_edge_9(self):
        g = nx.Graph()
        g.add_node(1, pos=(0, 1))
        g.add_node(2, pos=(2, 1))
        g.add_node(3, pos=(1, 1))
        g.add_node(4, pos=(2, 0))
        g.add_edges_from([(1, 2), (3, 4)])
        __assert_crossing_equality__(g, [crossings.Crossing(crossings.CrossingPoint(1, 1), [(1, 2), (3, 4)])], True,
                                     True)

    def test_vertex_at_edge_1_disabled(self):
        g = nx.Graph()
        g.add_node(1, pos=(0, 0))
        g.add_node(2, pos=(0, 2))
        g.add_node(3, pos=(0, 1))
        g.add_node(4, pos=(1, 2))
        g.add_edges_from([(1, 2), (3, 4)])
        __assert_crossing_equality__(g, [])

    def test_vertex_at_edge_2_disabled(self):
        g = nx.Graph()
        g.add_node(1, pos=(0, 0))
        g.add_node(2, pos=(0, 2))
        g.add_node(3, pos=(0, 1))
        g.add_node(4, pos=(1, 1))
        g.add_edges_from([(1, 2), (3, 4)])
        __assert_crossing_equality__(g, [])

    def test_vertex_at_edge_3_disabled(self):
        g = nx.Graph()
        g.add_node(1, pos=(0, 0))
        g.add_node(2, pos=(0, 2))
        g.add_node(3, pos=(0, 1))
        g.add_node(4, pos=(1, 0))
        g.add_edges_from([(1, 2), (3, 4)])
        __assert_crossing_equality__(g, [])

    def test_vertex_at_edge_4_disabled(self):
        g = nx.Graph()
        g.add_node(1, pos=(0, 1))
        g.add_node(2, pos=(2, 1))
        g.add_node(3, pos=(1, 1))
        g.add_node(4, pos=(1, 0))

        g.add_edges_from([(1, 2), (3, 4)])
        __assert_crossing_equality__(g, [])

    def test_vertex_at_edge_5_disabled(self):
        g = nx.Graph()
        g.add_node(1, pos=(0, 1))
        g.add_node(2, pos=(2, 1))
        g.add_node(3, pos=(1, 1))
        g.add_node(4, pos=(0, 0))
        g.add_edges_from([(1, 2), (3, 4)])
        __assert_crossing_equality__(g, [])

    def test_vertex_at_edge_6_disabled(self):
        g = nx.Graph()
        g.add_node(1, pos=(0, 1))
        g.add_node(2, pos=(2, 1))
        g.add_node(3, pos=(1, 1))
        g.add_node(4, pos=(2, 0))
        g.add_edges_from([(1, 2), (3, 4)])
        __assert_crossing_equality__(g, [])

    def test_vertex_at_edge_7_disabled(self):
        g = nx.Graph()
        g.add_node(1, pos=(0, 1))
        g.add_node(2, pos=(2, 1))
        g.add_node(3, pos=(1, 1))
        g.add_node(4, pos=(1, 0))

        g.add_edges_from([(1, 2), (3, 4)])
        __assert_crossing_equality__(g, [], True)

    def test_vertex_at_edge_8_disabled(self):
        g = nx.Graph()
        g.add_node(1, pos=(0, 1))
        g.add_node(2, pos=(2, 1))
        g.add_node(3, pos=(1, 1))
        g.add_node(4, pos=(0, 0))
        g.add_edges_from([(1, 2), (3, 4)])
        __assert_crossing_equality__(g, [], True)

    def test_vertex_at_edge_9_disabled(self):
        g = nx.Graph()
        g.add_node(1, pos=(0, 1))
        g.add_node(2, pos=(2, 1))
        g.add_node(3, pos=(1, 1))
        g.add_node(4, pos=(2, 0))
        g.add_edges_from([(1, 2), (3, 4)])
        __assert_crossing_equality__(g, [], True)

    def test_vertex_at_vertex_1(self):
        g = nx.Graph()
        g.add_node(1, pos=(-2, -3))
        g.add_node(2, pos=(0, 0))
        g.add_node(3, pos=(-1, 1))
        g.add_node(4, pos=(0, 0))
        g.add_edges_from([(1, 2), (3, 4)])
        __assert_crossing_equality__(g, [
            crossings.Crossing(crossings.CrossingPoint(0, 0), [(1, 2), (3, 4)])
        ], True, True)

    def test_vertex_at_vertex_2(self):
        g = nx.Graph()
        g.add_node(1, pos=(-2, -3))
        g.add_node(2, pos=(0, 0))
        g.add_node(3, pos=(-1, 1))
        g.add_node(4, pos=(0, 0))
        g.add_edges_from([(1, 2), (3, 4)])
        __assert_crossing_equality__(g, [], True)


class TestHorizontalCrossings(unittest.TestCase):

    def test_vertical_horizontal_crossing(self):
        g = nx.Graph()
        g.add_node(1, pos=(0, 1))
        g.add_node(2, pos=(2, 1))
        g.add_node(3, pos=(1, 0))
        g.add_node(4, pos=(1, 2))
        g.add_edges_from([(1, 2), (3, 4)])
        __assert_crossing_equality__(g, [crossings.Crossing(crossings.CrossingPoint(1, 1), [(1, 2), (3, 4)])])

    def test_horizontal_line_with_vertex_crossing(self):
        g = nx.Graph()
        g.add_node(1, pos=(0, 1))
        g.add_node(2, pos=(1, 1))
        g.add_node(3, pos=(2, 1))
        g.add_node(4, pos=(3, 1))
        g.add_node(5, pos=(0, 0))
        g.add_node(6, pos=(3, 2))

        g.add_edges_from([(1, 4), (2, 5), (3, 6)])
        __assert_crossing_equality__(g, crossings.get_crossings_quadratic(g, include_node_crossings=True),
                                     include_node_crossings=True)

    def test_horizontal_multiple_crossing_lines(self):
        g = nx.Graph()
        g.add_node(1, pos=(0, 1))
        g.add_node(2, pos=(5, 1))
        g.add_node(3, pos=(1, 0))
        g.add_node(4, pos=(1, 2))
        g.add_node(5, pos=(2, 0))
        g.add_node(6, pos=(2, 2))
        g.add_node(7, pos=(3, 0))
        g.add_node(8, pos=(3, 2))
        g.add_node(9, pos=(4, 0))
        g.add_node(10, pos=(4, 2))
        g.add_edges_from([(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)])

        __assert_crossing_equality__(g, [
            crossings.Crossing(crossings.CrossingPoint(1, 1), [(1, 2), (3, 4)]),
            crossings.Crossing(crossings.CrossingPoint(2, 1), [(1, 2), (5, 6)]),
            crossings.Crossing(crossings.CrossingPoint(3, 1), [(1, 2), (7, 8)]),
            crossings.Crossing(crossings.CrossingPoint(4, 1), [(1, 2), (9, 10)])
        ])


class TestOverlappingCrossings(unittest.TestCase):

    def test_overlapping_crossing_1(self):
        g = nx.Graph()
        g.add_node(1, pos=(0, 0))
        g.add_node(2, pos=(10, 0))
        g.add_node(3, pos=(3, 0))
        g.add_node(4, pos=(7, 0))
        g.add_edges_from([(1, 2), (3, 4)])
        __assert_crossing_equality__(g, [crossings.Crossing(crossings.CrossingLine((3, 0), (7, 0)), [(1, 2), (3, 4)])])

    def test_overlapping_crossing_2(self):
        g = nx.Graph()
        g.add_node(1, pos=(0, 0))
        g.add_node(2, pos=(7, 0))
        g.add_node(3, pos=(3, 0))
        g.add_node(4, pos=(10, 0))
        g.add_edges_from([(1, 2), (3, 4)])
        __assert_crossing_equality__(g, [crossings.Crossing(crossings.CrossingLine((3, 0), (7, 0)), [(1, 2), (3, 4)])])

    def test_overlapping_crossing_3(self):
        g = nx.Graph()
        g.add_node(1, pos=(0, 0))
        g.add_node(2, pos=(0, 10))
        g.add_node(3, pos=(0, 3))
        g.add_node(4, pos=(0, 7))
        g.add_edges_from([(1, 2), (3, 4)])
        __assert_crossing_equality__(g, [crossings.Crossing(crossings.CrossingLine((0, 3), (0, 7)), [(1, 2), (3, 4)])])

    def test_overlapping_crossing_4(self):
        g = nx.Graph()
        g.add_node(1, pos=(0, 0))
        g.add_node(2, pos=(0, 7))
        g.add_node(3, pos=(0, 3))
        g.add_node(4, pos=(0, 10))
        g.add_edges_from([(1, 2), (3, 4)])
        __assert_crossing_equality__(g, [crossings.Crossing(crossings.CrossingLine((0, 3), (0, 7)), [(1, 2), (3, 4)])])

    def test_overlapping_edges_crossing_another(self):
        g = nx.Graph()
        g.add_node(1, pos=(0, 0))
        g.add_node(2, pos=(1, 1))
        g.add_node(3, pos=(2, 2))
        g.add_node(4, pos=(3, 3))
        g.add_node(5, pos=(0, 1.5))
        g.add_node(6, pos=(3, 1.5))
        g.add_edges_from([(1, 4), (2, 3), (5, 6)])
        __assert_crossing_equality__(g, [crossings.Crossing(crossings.CrossingLine((1, 1), (2, 2)), [(1, 4), (2, 3)]),
                                         crossings.Crossing(crossings.CrossingPoint(1.5, 1.5), [(1, 4), (2, 3), (5, 6)])
                                         ])

    def test_overlapping_edges_crossing_another_2(self):
        g = nx.Graph()
        g.add_node(1, pos=(0, 0))
        g.add_node(2, pos=(1, 1))
        g.add_node(3, pos=(2, 2))
        g.add_node(4, pos=(3, 3))
        g.add_node(5, pos=(0, 1.5))
        g.add_node(6, pos=(3, 1.5))
        g.add_edges_from([(1, 3), (2, 4), (5, 6)])
        __assert_crossing_equality__(g, [crossings.Crossing(crossings.CrossingLine((1, 1), (2, 2)), [(1, 3), (2, 4)]),
                                         crossings.Crossing(crossings.CrossingPoint(1.5, 1.5), [(1, 3), (2, 4), (5, 6)])
                                         ])

    def test_overlapping_edges_common_endpoint(self):
        g = nx.Graph()
        g.add_node(1, pos=(0, 0))
        g.add_node(2, pos=(3, -2))
        g.add_node(3, pos=(6, -4))

        g.add_edges_from([(1, 2), (1, 3)])

        __assert_crossing_equality__(g, [crossings.Crossing(crossings.CrossingLine((0, 0), (3, -2)), [(1, 2), (1, 3)])],
                                     True)


class TestCommonEndpointCrossings(unittest.TestCase):

    def test_crossings_with_common_vertex(self):
        g = nx.Graph()
        g.add_node(1, pos=(0, 2))
        g.add_node(2, pos=(3, 2))
        g.add_node(3, pos=(1, 0))
        g.add_node(4, pos=(4, 0))

        g.add_node(5, pos=(1, 2))

        g.add_edges_from([(1, 4), (2, 3), (3, 5)])
        __assert_crossing_equality__(g, [
            crossings.Crossing(crossings.CrossingPoint(1.0, 1.5), [(3, 5), (1, 4)]),
            crossings.Crossing(crossings.CrossingPoint(2.0, 1.0), [(2, 3), (1, 4)])])

    def test_crossings_with_common_vertex_2(self):
        g = nx.Graph()
        g.add_node(1, pos=(0, 2))
        g.add_node(2, pos=(2, 2))
        g.add_node(3, pos=(1, 0))
        g.add_node(4, pos=(3, 0))

        g.add_node(5, pos=(1, 2))
        g.add_node(6, pos=(0, 1))

        g.add_edges_from([(1, 4), (2, 3), (3, 5), (4, 6)])

        __assert_crossing_equality__(g, crossings.get_crossings_quadratic(g))


class TestComplexCrossingScenarios(unittest.TestCase):

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
        __assert_crossing_equality__(g, [crossings.Crossing(crossings.CrossingPoint(0, 0), edges)])

    def test_no_crossing_with_shared_endpoint(self):
        g = nx.Graph()
        g.add_node(1, pos=(0, 0))
        g.add_node(2, pos=(1, 0))
        g.add_node(3, pos=(0, 1))
        g.add_edges_from([(1, 2), (2, 3)])
        __assert_crossing_equality__(g, [], True)

    def test_single_crossing_containing_all_types(self):
        g = nx.Graph()
        g.add_node(1, pos=(-2, 4))
        g.add_node(2, pos=(-3, 3))
        g.add_node(3, pos=(1, 3))
        g.add_node(4, pos=(2, 3))
        g.add_node(5, pos=(-2, 2))
        g.add_node(6, pos=(2, 1))
        g.add_node(7, pos=(3, 1))
        g.add_node(8, pos=(0, 0))
        g.add_node(9, pos=(0.25, -2))
        g.add_node(10, pos=(-3, -4))
        g.add_node(11, pos=(-1, -4))
        g.add_node(12, pos=(1, -4))
        g.add_node(13, pos=(2, -4))
        g.add_node(14, pos=(-2, -6))
        g.add_edges_from([(1, 13), (2, 11), (3, 14), (4, 8), (5, 8), (6, 8), (7, 12), (8, 9), (8, 10)])
        __assert_crossing_equality__(g, [
            crossings.Crossing(crossings.CrossingPoint(0, 0),
                               [(3, 14), (5, 8), (6, 8), (8, 10), (1, 13), (8, 9), (4, 8)]),
            crossings.Crossing(crossings.CrossingPoint(1.44444444444444444444, -2.88888888888888888),
                               [(1, 13), (7, 12)]),
            crossings.Crossing(crossings.CrossingPoint(-1.1538461538461537, -3.4615384615384617), [(3, 14), (2, 11)]),
            crossings.Crossing(crossings.CrossingPoint(-1.5517241379310345, -2.0689655172413794), [(8, 10), (2, 11)])
        ], include_node_crossings=True)

    def test_low_precision_group_crossing(self):
        g = nx.Graph()
        g.add_node(1, pos=(0, 3))
        g.add_node(2, pos=(2, 2.5))
        g.add_node(3, pos=(3.5, 3.5))
        g.add_node(4, pos=(4, 4.5))
        g.add_node(5, pos=(3, 0))
        g.add_node(6, pos=(0, 0))
        edges = [(1, 5), (2, 6), (3, 6), (4, 6)]
        g.add_edges_from(edges)

        crossing_list = crossings.get_crossings(g, precision=0.1)
        assert len(crossing_list) == 1
        assert math.isclose(crossing_list[0].pos[0], 1.5, rel_tol=0.1)
        assert math.isclose(crossing_list[0].pos[1], 1.5, rel_tol=0.1)

        # Note that we explicitly do not check for the contained edges as grouping crossings together which are not
        #  actually crossing at the same point

    def test_random_graph(self):
        random.seed(9018098129039)
        for i in range(0, 25):
            random_graph = nx.fast_gnp_random_graph(i, random.uniform(0.1, 1), random.randint(1, 10000000))
            random_embedding = {n: [random.randint(-100, 100), random.randint(-100, 100)] for n in range(0, i + 1)}
            nx.set_node_attributes(random_graph, random_embedding, "pos")
            __assert_crossing_equality__(random_graph, crossings.get_crossings_quadratic(random_graph),
                                         include_node_crossings=True)

    def test_random_graph_2(self):
        random.seed(9018098129039)
        for i in range(0, 25):
            random_graph = nx.fast_gnp_random_graph(i, random.uniform(0.1, 1), random.randint(1, 10000000))
            random_embedding = {n: [random.randint(-100, 100), random.randint(-100, 100)] for n in range(0, i + 1)}
            nx.set_node_attributes(random_graph, random_embedding, "pos")
            __assert_crossing_equality__(random_graph, crossings.get_crossings_quadratic(random_graph))

    def test_edge_with_length_0(self):
        g = nx.Graph()
        g.add_node(0, pos=(0, 0))
        g.add_node(1, pos=(0, 0))
        g.add_edge(0, 1)

        crossing_list = crossings.get_crossings(g)

        assert len(crossing_list) == 0

    def test_edge_with_length_0_in_edge(self):
        g = nx.Graph()

        g.add_node(0, pos=(0, 0))
        g.add_node(1, pos=(0, 0))
        g.add_node(2, pos=(-1, 0))
        g.add_node(3, pos=(1, 0))
        g.add_edges_from([(0, 1), (2, 3)])

        __assert_crossing_equality__(g, [
            crossings.Crossing(crossings.CrossingPoint(0, 0), [(0, 1), (2, 3)])
        ], True, True)

    def test_edge_with_length_0_in_crossing(self):
        g = nx.Graph()

        g.add_node(0, pos=(0, 0))
        g.add_node(1, pos=(0, 0))
        g.add_node(2, pos=(-1, -1))
        g.add_node(3, pos=(1, 1))
        g.add_node(4, pos=(1, -1))
        g.add_node(5, pos=(-1, 1))
        g.add_edges_from([(0, 1), (2, 3), (4, 5)])

        __assert_crossing_equality__(g, [
            crossings.Crossing(crossings.CrossingPoint(0, 0), [(0, 1), (2, 3), (4, 5)])
        ], True, True)

    def test_edge_with_length_0_in_crossing_2(self):
        g = nx.Graph()

        g.add_node(0, pos=(0, 0))
        g.add_node(1, pos=(0, 0))
        g.add_node(2, pos=(-1, -1))
        g.add_node(3, pos=(1, 1))
        g.add_node(4, pos=(1, -1))
        g.add_node(5, pos=(-1, 1))
        g.add_edges_from([(0, 1), (2, 3), (4, 5)])

        __assert_crossing_equality__(g, [
            crossings.Crossing(crossings.CrossingPoint(0, 0), [(0, 1), (2, 3), (4, 5)])
        ], True)

    def test_random_graph_small_grid(self):
        """
        Due to the smaller area, we expect much more edge cases such as:
            - Multiple crossings on the same point
            - Horizontal edges
            - Vertices on edges (we count those as crossings as well)
        """
        random.seed(19031023901923)

        for i in range(0, 25):
            random_graph = nx.fast_gnp_random_graph(i, random.uniform(0.1, 1), random.randint(1, 1000000))
            random_embedding = {n: [random.randint(-1, 1), random.randint(-1, 1)] for n in range(0, i + 1)}
            nx.set_node_attributes(random_graph, random_embedding, "pos")
            __assert_crossing_equality__(random_graph,
                                         crossings.get_crossings_quadratic(random_graph, include_node_crossings=True),
                                         include_node_crossings=True)

    def test_random_graph_small_grid_2(self):
        """
        Due to the smaller area, we expect much more edge cases such as:
            - Multiple crossings on the same point
            - Horizontal edges
            - Vertices on edges (we count those as crossings as well)
        """
        random.seed(19031023901923)

        for i in range(0, 25):
            random_graph = nx.fast_gnp_random_graph(i, random.uniform(0.1, 1), random.randint(1, 1000000))
            random_embedding = {n: [random.randint(-1, 1), random.randint(-1, 1)] for n in range(0, i + 1)}
            nx.set_node_attributes(random_graph, random_embedding, "pos")
            __assert_crossing_equality__(random_graph, crossings.get_crossings_quadratic(random_graph))

    def test_overlapping_edges_crossing_another_at_vertex(self):
        g = nx.Graph()
        g.add_node(1, pos=(0, 0))
        g.add_node(2, pos=(1, 1))
        g.add_node(3, pos=(2, 2))
        g.add_node(4, pos=(3, 3))
        g.add_node(5, pos=(1.5, 1.5))
        g.add_node(6, pos=(3, 1.5))
        g.add_edges_from([(1, 3), (2, 4), (5, 6)])
        __assert_crossing_equality__(g, [crossings.Crossing(crossings.CrossingLine((1, 1), (2, 2)), [(1, 3), (2, 4)]),
                                         crossings.Crossing(crossings.CrossingPoint(1.5, 1.5), [(1, 3), (2, 4), (5, 6)])
                                         ], include_node_crossings=True)

    def test_overlapping_edges_crossing_another_at_vertex_2(self):
        g = nx.Graph()
        g.add_node(1, pos=(0, 0))
        g.add_node(2, pos=(1, 1))
        g.add_node(3, pos=(2, 2))
        g.add_node(4, pos=(3, 3))
        g.add_node(5, pos=(1.5, 1.5))
        g.add_node(6, pos=(3, 1.5))
        g.add_edges_from([(1, 3), (2, 4), (5, 6)])
        __assert_crossing_equality__(g, [crossings.Crossing(crossings.CrossingLine((1, 1), (2, 2)), [(1, 3), (2, 4)])
                                         ])


class TestCrossingAngles(unittest.TestCase):

    def test_simple_crossing(self):
        g = nx.Graph()
        g.add_node(1, pos=(0, 0))
        g.add_node(2, pos=(1, 1))
        g.add_node(3, pos=(1, 0))
        g.add_node(4, pos=(0, 1))

        g.add_edges_from([(1, 2), (3, 4)])

        all_crossings = crossings.get_crossings(g)
        print(all_crossings)

        assert len(all_crossings) == 1

        crossing_angles = crossings.crossing_angles(all_crossings[0], nx.get_node_attributes(g, 'pos'), True)
        print(crossing_angles)

        assert len(crossing_angles) == 4
        assert crossing_angles[0] == 90
        assert crossing_angles[1] == 90
        assert crossing_angles[2] == 90
        assert crossing_angles[3] == 90

    def test_vertex_at_edge(self):
        g = nx.Graph()
        g.add_node(1, pos=(0, 0))
        g.add_node(2, pos=(5, 0))
        g.add_node(3, pos=(3, 5))
        g.add_node(4, pos=(3, 0))
        g.add_edges_from([(1, 2), (3, 4)])

        all_crossings = crossings.get_crossings(g, include_node_crossings=True)

        assert len(all_crossings) == 1

        crossing_angles = crossings.crossing_angles(all_crossings[0], nx.get_node_attributes(g, 'pos'), True)
        print(crossing_angles)

        assert len(crossing_angles) == 3
        assert crossing_angles[0] == 90
        assert crossing_angles[1] == 180
        assert crossing_angles[2] == 90

    def test_crossing_angular_resolution(self):
        g = nx.Graph()
        g.add_node(1, pos=(0, 0))
        g.add_node(2, pos=(5, 0))
        g.add_node(3, pos=(3, 5))
        g.add_node(4, pos=(3, 0))
        g.add_edges_from([(1, 2), (3, 4)])

        crossing_angular_resolution = crossings.crossing_angular_resolution(g, include_vertex_crossings=True, deg=True)
        assert crossing_angular_resolution == 90

    def test_crossing_angular_resolution_2(self):
        g = nx.Graph()
        g.add_node(1, pos=(0, 0))
        g.add_node(2, pos=(1, 1))
        g.add_node(3, pos=(1, 0))
        g.add_node(4, pos=(0, 1))

        g.add_edges_from([(1, 2), (3, 4)])

        crossing_angular_resolution = crossings.crossing_angular_resolution(g, include_vertex_crossings=True, deg=True)
        assert crossing_angular_resolution == 90
