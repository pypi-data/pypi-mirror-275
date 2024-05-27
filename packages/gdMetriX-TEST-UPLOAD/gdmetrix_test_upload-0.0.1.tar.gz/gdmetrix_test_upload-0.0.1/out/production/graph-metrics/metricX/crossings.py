"""
    This module provides functions for dealing with crossings, including obtaining crossing angles.

    Usage
    -----

    To obtain a list of all crossings, simply call :func:`get_crossings()`:

    .. code-block:: python

        >>> g = nx.random_geometric_graph(20, 0.5)
        >>> crossing_list = get_crossings(g)

    To planarize a graph, call :func:`planarize()`:

    .. code-block:: python

        >>> planarize(g)

    This will replace all crossings with new nodes at the same positions.

    Methods
    -------

"""

import math
import sys
from typing import List, Optional, Tuple, Union

import networkx as nx
from shapely.geometry import LineString

from metricX import crossingDataTypes, logConfig, common, edge_directions, boundary
from metricX.crossingDataTypes import EventQueue, SweepLineEdgeInfo, SweepLineStatus, CrossingPoint, CrossingLine, \
    Crossing

logger = logConfig.get_logger(__name__)


def __share_endpoint__(line_a: SweepLineEdgeInfo, line_b: SweepLineEdgeInfo):
    return (line_a.edge[0] == line_b.edge[0] or line_a.edge[0] == line_b.edge[1] or line_a.edge[1] == line_b.edge[0]
            or line_a.edge[1] == line_b.edge[1])


def __check_lines__(line_a: SweepLineEdgeInfo, line_b: SweepLineEdgeInfo):
    if line_a is not None and line_b is not None:
        line1 = LineString((line_a.start_position, line_a.end_position))
        line2 = LineString((line_b.start_position, line_b.end_position))

        crossing_point = line1.intersection(line2)

        if not crossing_point.is_empty:
            if isinstance(crossing_point, LineString):
                return CrossingLine((crossing_point.coords[0][0], crossing_point.coords[0][1]),
                                    (crossing_point.coords[1][0], crossing_point.coords[1][1]))
            elif not __share_endpoint__(line_a, line_b):
                return CrossingPoint(crossing_point.x, crossing_point.y)
        else:
            return None
    else:
        return None


def get_crossings_quadratic(g: nx.Graph, pos: Union[str, dict, None] = None, include_node_crossings: bool = False,
                            precision: float = 1e-09) -> List[Crossing]:
    r"""
    This alternative crossing detection function is in general slower, but in certain worst-cases might outperform
    the :func:`get_crossings()` method.

    The :func:`get_crossings()` method has an asymptotic runtime of :math:`O((n+k) \text{log} n)`, where :math:`k`
    is the number of crossings. This method runs in :math:`O(n^2)` time, which might outperform the optimized
    function when the number of crossing is :math:`\Theta(n^2)`.

    :param g: A networkX graph
    :type g: nx.Graph
    :param pos: Optional node position dictionary. If not supplied, node positions are read from the graph directly.
        If given as a string, the property under the given name in the networkX graph is used.
    :type pos: Union[str, dic, None]
    :param include_node_crossings: Indicate whether crossings involving vertices should be returned as well. A
        crossing involves a vertex if an endpoint of an edge lies on another edge without actually crossing it.
        Singletons will never be considered, even if the vertex lies exactly on another edge.
    :type include_node_crossings: bool
    :param precision: Sets the relative numeric precision. Usually, it should not be necessary to adjust the default.
    :type precision: float
    :return: A list of crossings, with a list of involved edges per crossing.
    :rtype: List[Crossing]
    """

    crossingDataTypes.set_precision(precision)

    pos = common.get_node_positions(g, pos)

    # Simple O(n^2) implementation for now
    crossings = []

    for edge1 in g.edges():
        for edge2 in g.edges():

            if edge1 == edge2:
                continue

            crossing_point = __check_lines__(
                crossingDataTypes.SweepLineEdgeInfo(edge1, pos[edge1[0]], pos[edge1[1]]),
                crossingDataTypes.SweepLineEdgeInfo(edge2, pos[edge2[0]], pos[edge2[1]])
            )

            if crossing_point is not None:

                # Add to list
                already_contained = False
                for oldCrossing in crossings:
                    if crossingDataTypes.__points_equal__(oldCrossing.pos, crossing_point):
                        oldCrossing.involved_edges.add(edge1)
                        oldCrossing.involved_edges.add(edge2)
                        already_contained = True
                        break

                if not already_contained:
                    crossings.append(Crossing(crossing_point, {edge1, edge2}))

    def _filter_node_crossings(cr: Crossing):
        if type(cr.pos) is CrossingPoint:
            cr.involved_edges = __filter_crossing_edges(cr, pos, include_node_crossings)
        return len(cr.involved_edges) > 1

    if not include_node_crossings:
        return list(filter(lambda cr: _filter_node_crossings(cr), crossings))
    else:
        return crossings


def __build_event_queue__(g, node_positions):
    queue = EventQueue()
    for e in g.edges():
        edge_info = SweepLineEdgeInfo(e, node_positions[e[0]], node_positions[e[1]])
        queue.add_edge(edge_info)

    return queue


def __filter_crossing_edges(cr: Crossing, pos, include_node_crossings) -> set:
    if include_node_crossings:
        edges = cr.involved_edges

        # If all share an endpoint it is actually not a valid crossing
        if len(edges) > 0:
            edge_list = list(edges)
            endpoint_a = edge_list[0][0]
            endpoint_b = edge_list[0][1]
            contains_non_incident = False
            logger.debug("Endpoint a: %s, endpoint b: %s", endpoint_a, endpoint_b)
            for index in range(1, len(edge_list)):
                logger.debug("Comparing to: %s", edge_list[index])
                if (edge_list[index][0] != endpoint_a and edge_list[index][1] != endpoint_a and
                        edge_list[index][0] != endpoint_b and edge_list[index][1] != endpoint_b):
                    contains_non_incident = True
                    logger.debug("All different")
                    break

            if not contains_non_incident:
                return set()
    else:
        # Only add those edges which actually cross and not those just ending in that point
        edges = []
        for edge in cr.involved_edges:
            if not (crossingDataTypes.__points_equal__(pos[edge[0]], cr.pos)
                    or crossingDataTypes.__points_equal__(pos[edge[1]], cr.pos)):
                edges.append(edge)

        edges = set(edges)

    if len(edges) <= 1:
        return set()

    # It might be the case that we have removed all actual crossings and what remain are just crossing lines
    just_lines = True
    edge_list = list(edges)
    for index in range(1, len(edge_list)):
        if type(__check_lines__(
                SweepLineEdgeInfo(edge_list[0], pos[edge_list[0][0]], pos[edge_list[0][1]]),
                SweepLineEdgeInfo(edge_list[index], pos[edge_list[index][0]], pos[edge_list[index][1]])
        )) != CrossingLine:
            just_lines = False
            break

    if just_lines:
        return set()

    return edges


def get_crossings(g: nx.Graph, pos: Union[str, dict, None] = None, include_node_crossings: bool = False,
                  precision: float = 1e-09) \
        -> List[Crossing]:
    # TODO add a flag to signal if we want to report crossings involving just vertices?
    # TODO add a flag to signal if we want to report crossing lines?
    r"""
    Calculates all crossings occurring in the graph. This uses the Bentley Ottmann algorithm - adapted to handle
    degenerate cases - and runs in :math:`O((n+k) \log n` time and space, where :math:`k` is the number of reported
    crossings.

    :param g: A networkX graph
    :type g: nx.Graph
    :param pos: Optional node position dictionary. If not supplied, node positions are read from the graph directly.
        If given as a string, the property under the given name in the networkX graph is used.
    :type pos: Union[str, dic, None]
    :param include_node_crossings: Indicate whether crossings involving vertices should be returned as well. A
        crossing involves a vertex if an endpoint of an edge lies on another edge without actually crossing it.
        Singletons will never be considered, even if the vertex lies exactly on another edge.
    :type include_node_crossings: bool
    :param precision: Sets the relative numeric precision. Usually, it should not be necessary to adjust the default.
    :type precision: float
    :return: A list of crossings, with a list of involved edges per crossing.
    :rtype: List[Crossing]
    """

    logger.debug("Starting to calculate all crossings for %s", g)

    crossingDataTypes.set_precision(precision)

    pos = common.get_node_positions(g, pos)

    height = boundary.height(g, pos)

    crossings = []
    crossing_lines = []
    sweep_line_status = SweepLineStatus()

    # Initialize event points
    queue = __build_event_queue__(g, pos)

    def __insert_crossing_into_crossing_list__(cr: Crossing) -> None:

        filtered_edges = __filter_crossing_edges(cr, pos, include_node_crossings)
        if len(filtered_edges) == 0:
            return
        cr.involved_edges = filtered_edges

        logger.debug("Inserting crossing %s", cr)

        # TODO implement log n approach
        for index, existing_crossing in enumerate(crossings):
            if crossingDataTypes.__points_equal__(existing_crossing.pos, cr.pos):
                existing_crossing.involved_edges |= cr.involved_edges
                return

            if crossingDataTypes._less_than(existing_crossing.pos, cr.pos):
                crossings.insert(index, cr)
                return

        crossings.append(cr)

    def __get_extreme_edges__(edges, y) -> Tuple[Optional[SweepLineEdgeInfo], Optional[SweepLineEdgeInfo]]:
        smallest_x = sys.maxsize
        smallest_edge = None
        biggest_x = (sys.maxsize - 1) * -1
        biggest_edge = None

        for edge in edges:
            x = crossingDataTypes.__get_x_at_y__(edge, y)
            if x <= smallest_x:
                smallest_x = x
                smallest_edge = edge
            if x > biggest_x:
                biggest_x = x
                biggest_edge = edge
        return smallest_edge, biggest_edge

    def __append_crossing__(edge_a: SweepLineEdgeInfo, edge_b: SweepLineEdgeInfo,
                            edges_involved_at_current_event_point: List) -> None:
        logger.debug("  Checking %s and %s for intersection", "None" if edge_a is None else edge_a.edge,
                     "None" if edge_b is None else edge_b.edge)
        cr = __check_lines__(edge_a, edge_b)
        if cr is not None:
            logger.debug("  Found crossing %s", cr)

            if crossingDataTypes._less_than((current_event_point.x, current_event_point.y),
                                            (cr.x, cr.y)):
                queue.add_crossing(cr, [edge_a, edge_b])

            elif crossingDataTypes.__points_equal__(
                    (current_event_point.x, current_event_point.y),
                    (cr.x, cr.y)
            ):
                # This can only be the case if this is a crossing involving a vertex (i.e. check via bool flag)
                # We add the involved edges to the current crossing instead of adding a new event point
                if include_node_crossings:
                    logger.debug("Found a crossing %s involving at least one vertex", cr)
                    edges_involved_at_current_event_point.append(edge_a)
                    edges_involved_at_current_event_point.append(edge_b)

            elif edge_a.is_horizontal() or edge_b.is_horizontal():
                # TODO we add a new crossing point here, however we should look up if the point already exists and just
                #  add the horizontal edge to it
                __insert_crossing_into_crossing_list__(Crossing(CrossingPoint(cr.x, cr.y),
                                                                {edge_a.edge, edge_b.edge}))
            else:
                # In case the crossing came before, we assume it is already discovered
                logger.debug("Ignore that crossing, we already passed it with the sweep line")

    previous_y = None

    horizontal_edges = []

    while (current_event_point := queue.pop()) is not None:

        if previous_y is not None and not crossingDataTypes.__numeric_eq__(current_event_point.y, previous_y):
            horizontal_edges = []

        # In some cases (for example if an edge is horizontal or if the vertex itself is involved in the crossing)
        # we only discover crossings at the current point.
        # We save those here to add at the end
        edges_discovered_at_current_event_point = []

        logger.debug("Looking at position (%s,%s)", current_event_point.x, current_event_point.y)
        logger.debug("  Starting edges: %s", ([edge.edge for edge in current_event_point.start_list]))
        logger.debug("  Ending edges: %s", ([edge.edge for edge in current_event_point.end_list]))
        logger.debug("  Interior edges: %s", ([edge.edge for edge in current_event_point.interior_list]))
        logger.debug("  Horizontal edges: %s", ([edge.edge for edge in current_event_point.horizontal_list]))

        logger.debug("  Sweepline before: %s", sweep_line_status)

        # Start by removing all ends
        logger.debug("  Starting to remove ending edges")
        for edge_info in current_event_point.end_list:
            sweep_line_status.remove(previous_y, edge_info)
            if include_node_crossings:
                for horizontal in current_event_point.horizontal_list:
                    __append_crossing__(horizontal, edge_info, edges_discovered_at_current_event_point)

        logger.debug("  Reverse order of interior edges")
        # reverse the order of interior edges
        for edge in current_event_point.interior_list:
            if not edge.is_horizontal():
                sweep_line_status.remove(previous_y, edge)
                sweep_line_status.add(current_event_point.y - crossingDataTypes.__precision, edge)

        left_edge = sweep_line_status.get_left(current_event_point)
        right_edge = sweep_line_status.get_right(current_event_point)
        logger.debug("  Left edge: %s", "None" if left_edge is None else left_edge.edge)
        logger.debug("  Right edge: %s", "None" if right_edge is None else right_edge.edge)

        if len(current_event_point.start_list) == 0 and len(current_event_point.interior_list) == 0:
            # Nothing comes below that is connected to the current event point
            # So we check the above and below neighbour for crossings
            logger.debug("  No edges at current event point, just compare left and right edge")
            __append_crossing__(left_edge, right_edge, edges_discovered_at_current_event_point)
        else:
            # We filter out the horizontal edges that might be at the crossing as we do not care for them for obtaining
            # leftmost/rightmost member
            union = filter(lambda e: not e.is_horizontal(),
                           current_event_point.start_list | current_event_point.interior_list)
            leftmost, rightmost = __get_extreme_edges__(union,
                                                        current_event_point.y - 100 * crossingDataTypes.__precision)

            logger.debug("  Left most edge in point: %s", "None" if leftmost is None else leftmost.edge)
            logger.debug("  Right most edge in point: %s", "None" if rightmost is None else rightmost.edge)

            __append_crossing__(left_edge, leftmost, edges_discovered_at_current_event_point)
            __append_crossing__(right_edge, rightmost, edges_discovered_at_current_event_point)

        # Check edges at the actual crossing (this is necessary for vertical edges, which are otherwise not discovered)
        logger.debug("  Checking crossings with sweep line edges at current point")
        edges_at_crossing = set(
            sweep_line_status.get_range(current_event_point.y, current_event_point.x, current_event_point.x))

        # TODO argue why this range query still keeps the runtime at O((n+I) log n) (hopefully)
        if len(edges_at_crossing) > 0:
            logger.debug("  Found edges in sweepline intersecting current event point: %s", edges_at_crossing)

            # Check for crossing points
            involved_edges = current_event_point.interior_list | edges_at_crossing

            if include_node_crossings:
                involved_edges |= current_event_point.start_list | current_event_point.end_list

            crossing = Crossing(CrossingPoint(current_event_point.x, current_event_point.y),
                                set([edge.edge for edge in involved_edges]))

            __insert_crossing_into_crossing_list__(crossing)

        # Check for crossing lines

        if len(current_event_point.start_list) > 0:
            candidates_sorted = sorted(edges_at_crossing,
                                       key=lambda edge:
                                       crossingDataTypes.__get_x_at_y__(edge, current_event_point.y - height))
            start_sorted = sorted(current_event_point.start_list,
                                  key=lambda edge:
                                  crossingDataTypes.__get_x_at_y__(edge,
                                                                   current_event_point.y - height))

            index_candidate = index_start = 0
            start_group = []
            candidate_group = []
            while index_start < len(start_sorted) or index_candidate < len(candidates_sorted):
                overlap_starts = __check_lines__(start_sorted[index_start], start_sorted[index_start + 1]) \
                    if index_start < len(start_sorted) - 1 else None
                overlap_candidate = __check_lines__(start_sorted[index_start], candidates_sorted[index_candidate]) \
                    if index_candidate < len(candidates_sorted) and index_start < len(start_sorted) else None

                if type(overlap_starts) is CrossingLine:
                    start_group.append(start_sorted[index_start])
                    start_group.append(start_sorted[index_start + 1])
                    index_start += 1
                elif type(overlap_candidate) is CrossingLine:
                    start_group.append(start_sorted[index_start])
                    candidate_group.append(candidates_sorted[index_candidate])
                    index_candidate += 1
                else:
                    # Report group pairwise as line crossings
                    for i in range(len(start_group)):
                        for j in range(i + 1, len(start_group)):
                            a = start_group[i]
                            b = start_group[j]

                            crossing = __check_lines__(a, b)

                            if type(crossing) is CrossingLine:
                                logger.debug("  Found new crossing line between two start edges: %s", crossing)
                                crossing_lines.append(Crossing(__check_lines__(a, b), {a.edge, b.edge}))

                    for a in start_group:
                        for b in candidate_group:

                            crossing = __check_lines__(a, b)
                            if type(crossing) is CrossingLine:
                                logger.debug(" Found new crossing line between a start edge and a crossing edge: %s",
                                             crossing)
                                crossing_lines.append(Crossing(__check_lines__(a, b), {a.edge, b.edge}))

                    start_group = []
                    candidate_group = []

                    if index_start == len(start_sorted):
                        index_candidate += 1
                    elif index_candidate == len(candidates_sorted):
                        index_start += 1
                    elif (crossingDataTypes.__get_x_at_y__(
                            start_sorted[index_start], current_event_point.y - 1000) <
                          crossingDataTypes.__get_x_at_y__(
                              candidates_sorted[index_candidate], current_event_point.y - 1000)):
                        index_start += 1
                    else:
                        index_candidate += 1

        # TODO there is a degenerate case which leads to O(n^2) when all edges overlap
        #  somehow delete some of the overlapping edges?

        # Check horizontal edges
        for horizontal in current_event_point.horizontal_list:
            logger.debug("  Checking crossing on horizontal %s", horizontal)
            for edge_info in sweep_line_status.get_range(current_event_point.y, horizontal.start_position[0],
                                                         horizontal.end_position[0]):
                __append_crossing__(horizontal, edge_info, edges_discovered_at_current_event_point)

            logger.debug("  Checking crossings with previous horizontals")
            if crossingDataTypes.__points_equal__(horizontal.start_position,
                                                  (current_event_point.x, current_event_point.y)):
                for edge_info in horizontal_edges:
                    crossing_line = __check_lines__(edge_info, horizontal)
                    # It might be the case that this returns just a point => we detect that at a later stage
                    if type(crossing_line) is CrossingLine:
                        logger.debug("  Found new horizontal crossing line %s", crossing_line)
                        crossing_lines.append(Crossing(crossing_line, {edge_info.edge, horizontal.edge}))
                horizontal_edges.append(horizontal)
            else:
                # TODO remove in log(n) time
                horizontal_edges.remove(horizontal)

        # Insert start points
        logger.debug("  Inserting new edges into sweep line: %s", current_event_point.start_list)
        for edge_info in current_event_point.start_list:
            sweep_line_status.add(current_event_point.y - crossingDataTypes.__precision, edge_info)

        logger.debug("  Sweepline after: %s", sweep_line_status)

        # In order to report all crossings in order, we report it only after encountering it on the sweepline
        if current_event_point.is_crossing or len(edges_discovered_at_current_event_point) != 0:
            if include_node_crossings:
                relevant_edges = set([edge.edge for edge in
                                      current_event_point.start_list | current_event_point.end_list
                                      | current_event_point.interior_list | current_event_point.horizontal_list
                                      | set(edges_discovered_at_current_event_point)])
            else:
                relevant_edges = set([edge.edge for edge in current_event_point.interior_list])

            new_crossing = Crossing(CrossingPoint(current_event_point.x, current_event_point.y), relevant_edges)
            logger.debug("  Reporting new crossing %s", new_crossing)
            __insert_crossing_into_crossing_list__(new_crossing)
        else:
            # TODO if we want to detect Vertex-Vertex crossings, check if end and start list combined only
            #  contain one element (and the horizontal list as well)
            pass

        previous_y = current_event_point.y

    # Join crossing lines which completely identical regions
    crossing_lines = sorted(crossing_lines)

    crossing_lines_consolidated = []
    for i in range(0, len(crossing_lines) - 1):
        if crossingDataTypes.__points_equal__(crossing_lines[i].pos, crossing_lines[i + 1].pos):
            crossing_lines[i + 1].involved_edges |= crossing_lines[i].involved_edges
        else:
            print(crossing_lines[i])
            crossing_lines_consolidated.append(crossing_lines[i])
    if len(crossing_lines) > 0:
        crossing_lines_consolidated.append(crossing_lines[len(crossing_lines) - 1])

    # Remove false positives
    crossing_points_consolidated = []
    for cr in crossings:
        cr.involved_edges = __filter_crossing_edges(cr, pos, include_node_crossings)
        if len(cr.involved_edges) > 0:
            crossing_lines_consolidated.append(cr)

    return crossing_points_consolidated + crossing_lines_consolidated


def planarize(g: nx.Graph, pos: Union[str, dict, None] = None, include_node_crossings: bool = False) -> None:
    """
    Planarizes the graph by replacing all crossings with nodes.

    :param g: A networkX graph
    :type g: nx.Graph
    :param pos: Optional node position dictionary. If not supplied, node positions are read from the graph directly.
        If given as a string, the property under the given name in the networkX graph is used.
    :type pos: Union[str, dic, None]
    :param include_node_crossings: Indicate whether crossings involving vertices should be returned as well. A
        crossing involves a vertex if an endpoint of an edge lies on another edge without actually crossing it.
        Singletons will never be considered, even if the vertex lies exactly on another edge.
    :type include_node_crossings: bool
    """

    pos = common.get_node_positions(g, pos)

    crossings = get_crossings(g, pos, include_node_crossings)

    # Obtain a list of crossing per edge
    involved_edges = {}
    for crossing in crossings:
        for edge in crossing.involved_edges:
            if edge in involved_edges:
                involved_edges[edge].append(crossing)
            else:
                involved_edges[edge] = [crossing]

    # TODO how to handle crossings where an edge endpoint is involved?
    i = 0
    for edge, crossings in involved_edges.items():
        crossings = sorted(crossings, key=lambda cr: common.euclidean_distance(cr.pos, pos[edge[0]]))

        g.remove_edge(edge[0], edge[1])

        last_node = edge[0]
        for crossing in crossings:
            if not hasattr(crossing, 'node_id'):
                crossing.node_id = "crossing" + str(i)
                new_pos = (crossing.pos.x, crossing.pos.y)
                g.add_node(crossing.node_id, pos=new_pos, is_elevated_crossing=True)
                pos[crossing.node_id] = new_pos
                i += 1

            if crossingDataTypes.__points_equal__(crossing.pos, pos[last_node]):
                logger.debug("Overlapping node positions")
                if last_node == edge[0]:
                    if g.degree(last_node) == 0:
                        g.remove_node(last_node)
                last_node = crossing.node_id
                continue

            g.add_edge(last_node, crossing.node_id)

            last_node = crossing.node_id

        # TODO same logic as for the first vertex
        g.add_edge(last_node, edge[1])


def crossing_angles(crossing: Crossing, pos: Union[str, dict, None], deg: bool = False) \
        -> List[float]:
    """
    Returns a list of angles in clockwise order formed by the edges at the crossing point.

    :param crossing: A crossing point
    :type crossing: metricX.Crossing
    :param pos: Optional node position dictionary. If not supplied, node positions are read from the graph directly.
        If given as a string, the property under the given name in the networkX graph is used.
    :type pos: Union[str, dic, None]
    :param deg: If true, the angles are returned as degrees in the range of (0,360). Otherwise, the angles are returned
        as radians.
    :type deg: bool
    :return: A list of angles at that crossing in clockwise order
    :rtype: List[float]
    """

    involved_nodes = set([node for edge in crossing.involved_edges for node in edge])

    # Filter out nodes that are at the crossing itself
    involved_nodes = list(filter(lambda node: not crossingDataTypes.__points_equal__(pos[node], crossing.pos),
                                 involved_nodes))

    return edge_directions.__edge_angles__(involved_nodes, crossing.pos, pos, deg)


def crossing_angular_resolution(g: nx.Graph, pos: Union[str, dict, None] = None, include_vertex_crossings: bool = False,
                                deg: bool = False) -> float:
    """
    Returns the minimal angle between two edges at any crossing.

    :param g: A networkX graph
    :type g: nx.Graph
    :param pos: Optional node position dictionary. If not supplied, node positions are read from the graph directly.
        If given as a string, the property under the given name in the networkX graph is used.
    :type pos: Union[str, dic, None]
    :param include_vertex_crossings:
    :type include_vertex_crossings:
    :param deg: If true, the angles are returned as degrees in the range of (0,360). Otherwise, the angles are returned
        as radians.
    :type deg: bool
    :return: The minimum angle between two edges in any of the crossings
    :rtype: float
    """
    pos = common.get_node_positions(g, pos)

    minimum = 360 if deg else math.pi * 2

    crs = get_crossings(g, pos, include_vertex_crossings)

    for crossing in crs:
        resolution = min(crossing_angles(crossing, pos, deg))

        if resolution < minimum:
            minimum = resolution

    return minimum
