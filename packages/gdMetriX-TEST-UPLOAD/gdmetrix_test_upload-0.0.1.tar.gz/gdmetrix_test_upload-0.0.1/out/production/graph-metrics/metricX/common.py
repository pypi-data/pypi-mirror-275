"""
    Collects some definition used in other modules.
"""

from __future__ import annotations

import math
from typing import Union

import networkx as nx
import numpy as np

numeric = Union[int, float]


def get_node_positions(g, pos: Union[str, dict, None] = None) -> dict:
    """
        Tries to obtain the node positions for the given graph.

        If
            - pos is not supplied: Returns the positions of the 'pos' property in the graph - if present
            - pos is given as a string: Returns the positions saved in the properties of the graph under the that name
            - pos is a dictionary: Simply returns the given dictionary
    :param g: A networkX graph
    :type g: nx.Graph
    :param pos: Optional position value
    :type pos: Union[str, dict, None]
    :return: The node positions of the given graph
    :rtype: dict
    """
    if pos is None:
        pos = "pos"
    if not isinstance(pos, str):
        return pos
    return nx.get_node_attributes(g, pos)


class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def from_point(pos):
        return Vector(pos[0], pos[1])

    def upwardAndForwardDirection(self):
        return self if (self.y > 0 or (self.y == 0 and self.x >= 0)) else Vector(-self.x, -self.y)

    def _to_array(self) -> np.array:
        return np.asarray((self.x, self.y))

    def angle(self, other) -> Angle:
        a = self._to_array()
        b = other._to_array()

        if self.x == self.y == 0 or other.x == other.y == 0:
            return Angle(0)

        det = np.linalg.det(np.array([b, a]))
        dot = np.dot(b, a)
        angle = Angle(np.arctan2(det, dot))

        if angle < 0:
            return Angle(math.pi * 2) + angle
        else:
            return angle

    def angleToX(self) -> Angle:
        return self.angle(Vector(1, 0))

    def rotate(self, angle: Angle):
        sin = math.sin(angle.rad)
        cos = math.cos(angle.rad)
        return Vector(self.x * cos - self.y * sin, self.x * sin + self.y * cos)

    def mid(self, other):
        return (self + other) / 2

    def euclidean_distance(self: Vector, other: Vector) -> float:
        return abs(self - other)

    def dot(self, other) -> float:
        return self.x * other.x + self.y * other.y

    def cross(self, other) -> float:
        return self.x * other.y - self.y * other.x

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar: float) -> Vector:
        return Vector(self.x * scalar, self.y * scalar)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __truediv__(self, scalar: float) -> Vector:
        if scalar == 0:
            raise ValueError("Division by zero")
        return Vector(self.x / scalar, self.y / scalar)

    def __abs__(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __eq__(self, other: Vector) -> bool:
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __str__(self):
        return f"v({self.x},{self.y})"


class Angle(float):
    # TODO use this class everywhere throughout project

    def __init__(self, rad: float):
        self.rad = rad

    def __float__(self):
        return self.rad

    def __add__(self, other):
        if isinstance(other, Angle):
            return Angle(self.rad + other.rad)
        else:
            return Angle(self.rad + other)

    def __mul__(self, other: float):
        return Angle(self.rad * other)

    def __sub__(self, other: float):
        return Angle(self.rad - float(other))

    def __mod__(self, other: float):
        return Angle(self.rad % other)

    def deg(self) -> float:
        return np.degrees(self.rad)

    def rad(self) -> float:
        return self.rad

    def norm(self) -> Angle:
        rad = self.rad
        while rad > math.pi:
            rad -= math.pi
        while rad < 0:
            rad += math.pi
        return Angle(rad)

    def __str__(self):
        return f"{self.deg():.2f}°"

    def __hash__(self):
        return hash(self.rad)


def euclidean_distance(point_a, point_b) -> float:
    return math.sqrt((point_a[0] - point_b[0]) ** 2 + (point_a[1] - point_b[1]) ** 2)
