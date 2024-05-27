"""
This module collects some metrics on the distribution of nodes.

Methods
-------
"""

import math
from typing import Union, List, Tuple, Optional

import networkx as nx
import numpy as np

from metricX import common, boundary
from metricX.common import numeric


def center_of_mass(g: nx.Graph, pos: Union[str, dict, None] = None, weight: Union[str, dict, None] = None) \
        -> Optional[Tuple[float, float]]:
    """
        Calculates the center of mass of all vertices (i.e. the average vertex position). Edges are not considered.
    :param g: A networkX graph
    :type g: nx.Graph
    :param pos: Optional node position dictionary. If not supplied, node positions are read from the graph directly.
                If given as a string, the property under the given name in the networkX graph is used.
    :type pos: Union[str, dic, None]
    :param weight: An optional weight dictionary. If given as a string, the property under the given name in the
                   networkX graph is used.
    :type weight: Union[str, dict, None]
    :return:
    :rtype:
    """
    pos = common.get_node_positions(g, pos)

    if len(pos) == 0:
        return None

    if isinstance(weight, str):
        weight = nx.get_node_attributes(g, weight)

    total_sum = np.array([0.0, 0.0])

    for node, position in pos.items():
        node_position = np.array(position)
        if weight is not None:
            node_position *= weight[node]
        total_sum += node_position

    if weight is not None:
        total_weight = sum(weight.values())
    else:
        total_weight = g.number_of_nodes()

    total_sum /= total_weight

    return float(total_sum[0]), float(total_sum[1])


def __get_grid_distribution(g: nx.Graph, pos: Union[str, dict, None], grid_size):
    def __get_grid_cell__(min_bound, max_bound, value):
        return int(min(((value - min_bound) / (max_bound - min_bound)) * grid_size, grid_size - 1))

    x_min, y_min, x_max, y_max = boundary.bounding_box(g, pos)

    grid = np.zeros((grid_size, grid_size))

    for node in g.nodes():
        x, y = pos[node]
        grid[__get_grid_cell__(x_min, x_max, x)][__get_grid_cell__(y_min, y_max, y)] += 1

    return grid


def _balance(g: nx.Graph, pos: Union[str, dict, None], use_relative_coordinates: bool, index_offset: int) -> float:
    pos = common.get_node_positions(g, pos)

    if len(pos) == 0:
        return 0

    if use_relative_coordinates:
        box = boundary.bounding_box(g, pos)
        cutoff = box[index_offset] + (box[index_offset + 2] - box[index_offset]) / 2
    else:
        cutoff = 0

    upper_count = 0
    lower_count = 0

    for node, point in pos.items():
        if point[index_offset] > cutoff:
            upper_count += 1
        elif point[index_offset] < cutoff:
            lower_count += 1
        else:
            upper_count += 0.5
            lower_count += 0.5

    return 0 if lower_count + upper_count == 0 else (upper_count - lower_count) / (lower_count + upper_count)


def horizontal_balance(g: nx.Graph, pos: Union[str, dict, None] = None, use_relative_coordinates: bool = True) -> float:
    """
        Returns a value between -1 and 1 indicating the horizontal balance.

        A value of 0 means a perfectly even balance between the upper and lower half.
        A value of -1 means that all nodes lie on the lower half, a value of 1 means that all nodes lie on the upper
        half.
    :param g: A networkX graph
    :type g: nx.Graph
    :param pos: Optional node position dictionary. If not supplied, node positions are read from the graph directly.
                If given as a string, the property under the given name in the networkX graph is used.
    :type pos: Union[str, dic, None]
    :param use_relative_coordinates: Indicates whether to use the absolute zero points or relative coordinates.
            If use_relative_coordinates is true:
                The horizontal split line will be at the center between the lowest and the highest node in the graph.
            If use_relative_coordinates is false:
                The horizontal split line is put at y=0.
    :type use_relative_coordinates: bool
    :return: A value between -1 and 1.
    :rtype: float
    """

    return _balance(g, pos, use_relative_coordinates, 1)


def vertical_balance(g: nx.Graph, pos: Union[str, dict, None] = None, use_relative_coordinates: bool = True) -> float:
    """
        Returns a value between -1 and 1 indicating the vertical balance.

        A value of 0 means a perfectly even balance between the left and right half.
        A value of -1 means that all nodes lie on the left half, a value of 1 means that all nodes lie on the right
        half.
    :param g: A networkX graph
    :type g: nx.Graph
    :param pos: Optional node position dictionary. If not supplied, node positions are read from the graph directly.
                If given as a string, the property under the given name in the networkX graph is used.
    :type pos: Union[str, dic, None]
    :param use_relative_coordinates: Indicates whether to use the absolute zero points or relative coordinates.
            If use_relative_coordinates is true:
                The vertical split line will be at the center between the leftmost and the rightmost node in the graph.
            If use_relative_coordinates is false:
                The vertical split line is put at x=0.
    :type use_relative_coordinates: bool
    :return: A value between -1 and 1.
    :rtype: float
    """

    return _balance(g, pos, use_relative_coordinates, 0)


def homogeneity(g: nx.Graph, pos: Union[str, dict, None] = None) -> float:
    """
        Calculates how evenly the nodes are distributed among the four quadrants.

        The measure was first defined by Taylor and Rodgers [1].

        [1] M. Taylor and P. Rodgers, “Applying graphical design techniques to graph visualisation,” in
         Ninth International Conference on Information Visualisation (IV’05), London, England: IEEE, 2005,
         pp. 651–656, isbn: 978-0-7695-2397-2. doi: 10.1109/IV.2005.19.
    :param g: A networkX graph
    :type g: nx.Graph
    :param pos: Optional node position dictionary. If not supplied, node positions are read from the graph directly.
                If given as a string, the property under the given name in the networkX graph is used.
    :type pos: Union[str, dic, None]
    :return: A value between 0 and 1. A value of 0 indicates an even distribution among the quadrants, and 1 the worst
    case distribution.
    :rtype: float
    """
    if g.order() <= 1:
        return 0

    # Necessary variables
    n = g.order()
    n_avg = math.floor(n / 4)

    # Sum up the number of nodes in each quadrant
    pos = common.get_node_positions(g, pos)

    quadrants = __get_grid_distribution(g, pos, 2)
    multiply = []
    divide = []
    for n_quadrant in quadrants.flatten():
        n_quadrant = int(n_quadrant)
        if n_quadrant < n_avg:
            multiply += (list(range(n_quadrant + 1, n_avg + 1)))
        elif n_quadrant > n_avg:
            divide += (list(range(n_avg + 1, n_quadrant + 1)))

    # Calculate the logarithmic sum of the numerator and denominator
    numerator = sum(math.log(x) for x in multiply)
    denominator = sum(math.log(x) for x in divide)

    # Calculate the fraction using the exponential function
    fraction = math.exp(numerator - denominator)

    return 1 - fraction


def concentration(g: nx.Graph, pos: Union[str, dict, None] = None, grid_size: numeric = 0) -> float:
    # TODO make the bounding box a parameter, might be useful for some applications
    """
        Calculates the concentration of the given networkX graph g.
        The concentration is a density measure counting the number of nodes in each cell of a sqrt(n) * sqrt(n) grid,
        where n is the number of nodes in the graph. The counts for each cell are then summed up and divided by n-1.

        A concentration of 1 means that all nodes are within a single grid cell, and a concentration of 0 means that
        all nodes are evenly spaced between the cells.

        The measure was first defined by Taylor and Rodgers [1].


        [1] M. Taylor and P. Rodgers, “Applying graphical design techniques to graph visualisation,” in
         Ninth International Conference on Information Visualisation (IV’05), London, England: IEEE, 2005,
         pp. 651–656, isbn: 978-0-7695-2397-2. doi: 10.1109/IV.2005.19.
    :param g: A networkX graph
    :type g: nx.Graph
    :param pos: Optional node position dictionary. If not supplied, node positions are read from the graph directly.
                If given as a string, the property under the given name in the networkX graph is used.
    :type pos: Union[str, dic, None]
    :param grid_size: For large graphs, where the calculation might be time sensitive, set a bigger grid size to improve
                      performance. A higher grid size reduces the precision of the metric. In most cases, leaving the
                      default value should be sufficient.
    :type grid_size: numeric
    :return: The concentration of the graph between 0 and 1
    :rtype: float
    """
    if g.order() <= 1:
        return 0
    pos = common.get_node_positions(g, pos)

    if grid_size == 0:
        grid_size = int(math.ceil(math.sqrt(g.order())))
        expected_per_cell = 1
    elif grid_size < 0:
        raise ValueError("grid_size")
    elif grid_size > int(math.ceil(math.sqrt(g.order()))):
        raise ValueError("The cell size is to small for the given graph. There can be at most one grid cell per node "
                         "in the graph")
    else:
        expected_per_cell = g.order() / math.pow(grid_size, 2)

    grid = __get_grid_distribution(g, pos, grid_size)
    return (np.sum(np.maximum(grid - expected_per_cell, 0))) / (g.order() - 1)


class __EmbeddedPoint:
    """ Represents a vertex with position """

    def __init__(self, key, x, y):
        self.key = key
        self.x = x
        self.y = y

    def __str__(self):
        return "[{}, x: {}, y: {}]".format(self.key, self.x, self.x)


def closet_pair_of_points(g: nx.Graph, pos: Union[str, dict, None] = None):
    """
        Returns the two closest points a, b together with their euclidean distance in the form (a,b, distance)
    :param g: A networkX graph
    :type g: nx.Graph
    :param pos: Optional node position dictionary. If not supplied, node positions are read from the graph directly.
                If given as a string, the property under the given name in the networkX graph is used.
    :type pos: Union[str, dic, None]
    :return: The keys of the two involved nodes as well as their distance
    :rtype: (object, object, float)
    """
    if g.order() <= 1:
        return None, None, None
    pos = common.get_node_positions(g, pos)

    p_list = list(__EmbeddedPoint(p, pos[p][0], pos[p][1]) for p in pos)

    x_sorted = sorted(p_list, key=lambda p: p.x)
    y_sorted = sorted(p_list, key=lambda p: p.y)

    a, b, distance = _closest_pair_recursion(x_sorted, y_sorted)

    return a.key, b.key, distance


def _closest_pair_recursion(x_sorted, y_sorted):
    def _euclidean_distance(point_a: __EmbeddedPoint, point_b: __EmbeddedPoint) -> float:
        return math.sqrt((point_a.x - point_b.x) ** 2 + (point_a.y - point_b.y) ** 2)

    def _bruteforce_distance(points: List[__EmbeddedPoint]) -> Tuple[__EmbeddedPoint, __EmbeddedPoint, float]:
        mi = _euclidean_distance(points[0], points[1])
        p1 = points[0]
        p2 = points[1]
        ln_ax = len(points)
        if ln_ax == 2:
            return p1, p2, mi
        for i in range(ln_ax - 1):
            for j in range(i + 1, ln_ax):
                if i != 0 and j != 1:
                    d = _euclidean_distance(points[i], points[j])
                    if d < mi:  # Update min_dist and points
                        mi = d
                        p1, p2 = points[i], points[j]
        return p1, p2, mi

    def _closest_split_pair(x_sorted_list: List[__EmbeddedPoint], y_sorted_list: List[__EmbeddedPoint], old_min: float,
                            old_min_pair: Tuple[__EmbeddedPoint, __EmbeddedPoint]) \
            -> Tuple[__EmbeddedPoint, __EmbeddedPoint, float]:
        x_med = x_sorted_list[len(x_sorted_list) // 2].x

        close_y = [p for p in y_sorted_list if x_med - old_min <= p.x <= x_med + old_min]
        new_min = old_min
        for i in range(len(close_y) - 1):
            for j in range(i + 1, min(i + 7, len(close_y))):
                p, q = close_y[i], close_y[j]
                dst = _euclidean_distance(p, q)
                if dst < new_min:
                    old_min_pair = p, q
                    new_min = dst
        return old_min_pair[0], old_min_pair[1], new_min

    if len(x_sorted) <= 3:
        return _bruteforce_distance(x_sorted)

    mid = len(x_sorted) // 2
    x_median = x_sorted[mid].x
    # Split by x into two even halves
    left_x = x_sorted[:mid]
    right_x = x_sorted[mid:]

    left_y, right_y = list(), list()

    # Do the same for y
    for point in y_sorted:
        if point.x <= x_median:
            left_y.append(point)
        else:
            right_y.append(point)

    (p_left, q_left, min_left) = _closest_pair_recursion(left_x, left_y)
    (p_right, q_right, min_right) = _closest_pair_recursion(right_x, right_y)

    # Combine the two halves
    if min_left <= min_right:
        min_total = min_left
        min_pair = (p_left, q_left)
    else:
        min_total = min_left
        min_pair = (p_left, q_left)

    (p_split, q_split, min_split) = _closest_split_pair(x_sorted, y_sorted, min_total, min_pair)

    if min_total <= min_split:
        return min_pair[0], min_pair[1], min_total
    else:
        return p_split, q_split, min_split


def _edge_node_distance(edge: Tuple[object, object], node: object, pos) -> float:
    def _distance(point_a, point_b):
        return np.linalg.norm(point_a - point_b)

    a_pos, b_pos = np.asarray(pos[edge[0]]), np.asarray(pos[edge[1]])
    n_pos = np.asarray(pos[node])

    v_ab = b_pos - a_pos
    v_bn = n_pos - b_pos
    v_an = n_pos - a_pos
    v_na = a_pos - n_pos

    if np.linalg.norm(v_ab) == 0 or np.dot(v_ab, v_bn) > 0:
        # Node is closer to endpoint b
        return _distance(n_pos, b_pos)
    elif np.dot(v_ab, v_an) < 0:
        # Node is closer to endpoint a
        return _distance(n_pos, a_pos)
    else:
        # Node is closer to edge itself -> return distance to line
        return np.abs(np.cross(v_ab, v_na) / np.linalg.norm(v_ab))


def closest_pair_of_elements(g: nx.Graph, pos: Union[str, dict, None] = None):
    """
    Returns the two graph elements (i.e. nodes and edges) with minimum distance between between them.
    :param g: A networkX graph
    :type g: nx.Graph
    :param pos: Optional node position dictionary. If not supplied, node positions are read from the graph directly.
                If given as a string, the property under the given name in the networkX graph is used.
    :type pos: Union[str, dic, None]
    :return: The keys of the two closest graph elements as well as their distance
    :rtype: (object, object, float)
    """
    # TODO O(m * n) implementation for now, replace with a more efficient implementation
    #  Do a simple sweep line from top to bottom and then switch coordinates (left to right)
    #  Should be able to reuse the datastructures of the crossing algorithm

    pos = common.get_node_positions(g, pos)
    element_a, element_b, min_distance = closet_pair_of_points(g, pos)

    for edge in g.edges():
        for node in g.nodes():
            if edge[0] == node or edge[1] == node:
                continue

            distance = _edge_node_distance(edge, node, pos)

            if distance < min_distance:
                element_a, element_b, min_distance = node, edge, distance

    return element_a, element_b, min_distance


def gabriel_ratio(g: nx.Graph, pos: Union[str, dict, None] = None) -> float:
    """
    The Gabriel ratio is the ratio of all number of nodes falling within a minimum circle covering an edge for any edge.

    This measure was first defined by Mooney et al., 2024. [1]

    [1] Gavin J. Mooney , Helen C. Purchase , Michael Wybrow , and Stephen G. Kobourov - The Multi-Dimensional Landscape
     of Graph Drawing Metrics

    :param g: A networkX graph
    :type g: nx.Graph
    :param pos: Optional node position dictionary. If not supplied, node positions are read from the graph directly.
                If given as a string, the property under the given name in the networkX graph is used.
    :type pos: Union[str, dic, None]
    :return: The Gabriel ratio between 0 and 1
    :rtype: float
    """

    # TODO O(m * n) implementation for now, replace with a more efficient implementation
    #  I think a sweep line should be possible as well

    def _distance(point_a, point_b):
        return np.linalg.norm(point_a - point_b)

    def _within_circle(v, e):
        a_pos, b_pos = np.asarray(pos[e[0]]), np.asarray(pos[e[1]])
        n_pos = np.asarray(pos[v])

        mid_point = a_pos + 0.5 * (b_pos - a_pos)

        return _distance(mid_point, n_pos) < _distance(a_pos, b_pos)

    pos = common.get_node_positions(g, pos)

    max_estimate = (g.order() - 2) * (len(g.edges()))
    if max_estimate <= 0:
        return 1

    count = 0

    for node in g.nodes():
        conforming = True
        for edge in g.edges():
            if node == edge[0] or node == edge[1]:
                continue
            if _within_circle(node, edge):
                conforming = False
                break

        if not conforming:
            count += 1

    return 1 - (count / max_estimate)

# TODO node orthogonality
# TODO max node distance
