import math
import numpy as np


class CurvePt:
    """
    Describes a point on a curve, associated with a curvature.

    Parameters
    ----------
    pos : list
        Global x,y position within a two element list.
    theta : float
        Orientation angle (converted to radians).
    s : float
        Distance along the curve.
    k : float
        Curvature.
    kd : float
        Derivative of curvature.

    Attributes
    ----------
    pos : list
        Global [x, y] position of the curve point.
    theta : float
    s : float
    k : float
    kd : float
    """
    def __init__(self, pos=[0.0, 0.0], theta=0, s=0, k=0, kd=0):
        self.pos = pos
        self.theta = math.radians(theta)
        self.s = float(s)
        self.k = float(k)
        self.kd = float(kd)


class Curve:
    """
    Contains a vector of CurvePt elements to describe the curvature of a lane
    on a road.

    Parameters
    ----------
    curve_points : list
        A list of CurvePt elements that make up the curve of a lane.

    Attributes
    ----------
    curve_points : list
        A list of CurvePt elements that make up the curve of a lane.
    """
    def __init__(self, curve_points=[]) -> None:
        self.curve_points = curve_points