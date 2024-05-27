"""
This module collects metrics concerning the orientation of edges.

Methods
-------

"""

import math
from typing import Union, Tuple, Optional, List

import networkx as nx
import numpy as np

from metricX import common
from metricX.common import numeric, Vector


def upwards_flow(g: nx.DiGraph, pos: Union[str, dict, None] = None,
                 direction_vector: Tuple[numeric, numeric] = (0, 1)) -> Optional[float]:
    """
        Calculates the percentage of edges pointing in the 'upwards' direction.
        An edge points 'upwards' if the angle between the upwards vector and the edge is smaller than 90 degrees.

        The measure was first defined by Helen Purchase  [1].

        [1] Helen C. Purchase, Metrics for Graph Drawing Aesthetics, 2002
    :param g: A networkX graph
    :type g: nx.Graph
    :param pos: Optional node position dictionary. If not supplied, node positions are read from the graph directly.
                If given as a string, the property under the given name in the networkX graph is used.
    :type pos: Union[str, dic, None]
    :param direction_vector: Defines the direction of 'upwards'
    :type direction_vector: Tuple[numeric, numeric]
    :return: Percentage of edges pointing 'upwards'
    :rtype: Optional[float]
    """
    if g is None or not nx.is_directed(g) or len(g.edges()) == 0:
        return 0

    if direction_vector == (0, 0):
        return None

    pos = common.get_node_positions(g, pos)

    sum_upward_edges = 0

    for edge in g.edges():
        e_vector = np.subtract(pos[edge[1]], pos[edge[0]])
        inner_product = np.inner(e_vector, direction_vector)

        if inner_product > 0:
            sum_upward_edges += 1

    return float(sum_upward_edges) / len(g.edges())


def average_flow(g: nx.DiGraph, pos: Union[str, dict, None] = None) -> Optional[Tuple[float, float]]:
    """
        Calculates the average edge direction.
    :param g: A networkX graph
    :type g: nx.Graph
    :param pos: Optional node position dictionary. If not supplied, node positions are read from the graph directly.
                If given as a string, the property under the given name in the networkX graph is used.
    :type pos: Union[str, dic, None]
    :return: The average edge direction, as a normalized vector.
    :rtype: Optional[Tuple[float, float]]
    """
    if g is None or not nx.is_directed(g) or len(g.edges()) == 0:
        return None

    pos = common.get_node_positions(g, pos)
    sum_vector = np.array([0.0, 0.0])

    for edge in g.edges():
        e_vector = np.subtract(pos[edge[1]], pos[edge[0]])
        length = np.linalg.norm(e_vector)
        if length != 0:
            sum_vector += e_vector / length

    sum_length = np.linalg.norm(sum_vector)
    if sum_length != 0:
        average = sum_vector / sum_length
    else:
        average = sum_vector

    np.nan_to_num(average, False, 0)
    return float(average[0]), float(average[1])


def coherence_to_average_flow(g: nx.DiGraph, pos: Union[str, dict, None] = None) -> Optional[float]:
    """
        Calculates the upwards flow along the average edge direction.
        This is equal to calling upwards_flow(g, average_flow(g))
    :param g: A networkX graph
    :type g: nx.Graph
    :param pos: Optional node position dictionary. If not supplied, node positions are read from the graph directly.
                If given as a string, the property under the given name in the networkX graph is used.
    :type pos: Union[str, dic, None]
    :return: The coherence to the average flow
    :rtype: Optional[float]
    """
    return upwards_flow(g, pos, average_flow(g, pos))


def ordered_neighborhood(g: nx.Graph, node: object, pos: Union[str, dict, None] = None) -> List:
    """
        Returns the neighborhood of the given node in the networkX graph ordered clockwise.
    :param g: A networkX graph
    :type g: nx.Graph
    :param node: A node key present in the given networkX graph
    :type node: object
    :param pos: Optional node position dictionary. If not supplied, node positions are read from the graph directly.
                If given as a string, the property under the given name in the networkX graph is used.
    :type pos: Union[str, dic, None]
    :return: List of neighbors of 'node' ordered clockwise
    :rtype: List
    """
    pos = common.get_node_positions(g, pos)

    neighbors = [edge[0] if edge[0] != node else edge[1] for edge in g.edges(node)]
    neighbors = list(filter(lambda nb: nb != node, neighbors))
    return __order_clockwise__(neighbors, pos[node], pos)


def __order_clockwise__(nodes: List, origin: Tuple[numeric, numeric], pos: Union[str, dict, None]) -> List:
    def __get_angle_between_nodes__(pos_a, pos_b) -> float:
        vector = Vector.from_point(pos_b).minus(Vector.from_point(pos_a))
        return Vector(0, 1).angle(vector)

    return sorted(nodes, key=lambda nb: __get_angle_between_nodes__(origin, pos[nb]))


def __edge_angles__(nodes: List, origin: Tuple[numeric, numeric], pos: Union[str, dict, None], deg: bool = False) \
        -> List:
    ordered_nodes = __order_clockwise__(nodes, origin, pos)

    angles = []

    if len(ordered_nodes) == 1:
        angles.append(math.pi * 2)
    else:
        for i in range(len(ordered_nodes)):
            p_nb_a = np.asarray(pos[ordered_nodes[i]])
            p_nb_b = np.asarray(pos[ordered_nodes[(i + 1) % len(ordered_nodes)]])
            vector_nb_a = Vector(p_nb_a[0] - origin[0], p_nb_a[1] - origin[1])
            vector_nb_b = Vector(p_nb_b[0] - origin[0], p_nb_b[1] - origin[1])
            angle = vector_nb_a.angle(vector_nb_b)
            angles.append(angle)

    return [np.degrees(angle) for angle in angles] if deg else angles


def combinatorial_embedding(g: nx.Graph, pos: Union[str, dict, None] = None) -> dict:
    """
        Returns the combinatorial embedding for the given networkX graph g.
    :param g: A networkX graph
    :type g: nx.Graph
    :param pos: Optional node position dictionary. If not supplied, node positions are read from the graph directly.
                If given as a string, the property under the given name in the networkX graph is used.
    :type pos: Union[str, dic, None]
    :return: The new node positions
    :rtype: dict
    """
    pos = common.get_node_positions(g, pos)
    return {node: ordered_neighborhood(g, node, pos) for node in g.nodes()}


def edge_angles(g: nx.Graph, node: object, pos: Union[str, dict, None] = None, deg: bool = False) -> List:
    """
        Returns a list of edge angles for the given node present in the networkX graph.
    :param g: A networkX graph
    :type g: nx.Graph
    :param node: A node key present in the given networkX graph
    :type node: object
    :param pos: Optional node position dictionary. If not supplied, node positions are read from the graph directly.
                If given as a string, the property under the given name in the networkX graph is used.
    :type pos: Union[str, dic, None]
    :param deg: If true, the angles are returned as degrees in the range of (0,360). Otherwise, the angles are returned
                as radians.
    :type deg: bool
    :return: List of angles between the edges in a clockwise order
    :rtype: List
    """
    pos = common.get_node_positions(g, pos)
    neighbors = ordered_neighborhood(g, node, pos)

    return __edge_angles__(neighbors, pos[node], pos, deg)


def angular_resolution(g: nx.Graph, pos: Union[str, dict, None] = None, deg: bool = False) -> float:
    """
        Returns the shallowest angle between any two edges sharing an endpoint
    :param g: A networkX graph
    :type g: nx.Graph
    :param pos: Optional node position dictionary. If not supplied, node positions are read from the graph directly.
                If given as a string, the property under the given name in the networkX graph is used.
    :type pos: Union[str, dic, None]
    :param deg: If true, the angles are returned as degrees in the range of (0,360). Otherwise, the angles are returned
                as radians.
    :type deg: bool
    """
    pos = common.get_node_positions(g, pos)

    minimum = 360 if deg else math.pi * 2

    for node in g.nodes():
        resolution = min(edge_angles(g, node, pos, deg))

        if resolution < minimum:
            minimum = resolution

    return minimum


def edge_orthogonality(g: nx.Graph, pos: Union[str, dict, None] = None) -> float:
    # TODO extend to accept custom slope number
    """
    Returns the extend to which edges are vertical or horizontal.

    The measure was first defined by Helen Purchase  [1].

    [1] Helen C. Purchase, Metrics for Graph Drawing Aesthetics, 2002

    :param g: A networkX graph
    :type g: nx.Graph
    :param pos: Optional node position dictionary. If not supplied, node positions are read from the graph directly.
                If given as a string, the property under the given name in the networkX graph is used.
    :type pos: Union[str, dic, None]
    """

    pos = common.get_node_positions(g, pos)

    total = 0
    for edge in g.edges():
        v_edge = Vector.from_point(pos[edge[1]]).minus(Vector.from_point(pos[edge[0]]))
        angle = v_edge.angle(Vector(1, 0))
        degree_deviation = angle % (math.pi / 2)
        degree_deviation = min(degree_deviation, math.pi / 2 - degree_deviation)
        total += degree_deviation * 4 / math.pi

    return 1 - (total / len(g.edges()))

# TODO Slope number
#  If directed => negative angles possible as well
