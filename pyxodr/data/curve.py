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
    start : list
        Global [x, y] starting position of the lane within a two element list.
    end : list
        Global [x, y] ending position of the lane within a two element list.
    nsamples : int
        Number of CurvePt elements to describe the curve. Default is 2: the
        start and end CurvePt elements.

    Attributes
    ----------
    curve_points : list
        A list of CurvePt elements that make up the curve of a lane.
    """
    def __init__(self,
                 start=[0.0, 0.0],
                 end=[0.0, 0.0],
                 nsamples=2,
                 type="line") -> None:

        if type == "line":
            self.curve_points = self.populate_curve_points_line(start,
                                                                end,
                                                                nsamples)
        elif type == "arc":
            self.curve_points = self.populate_curve_points_arc(start,
                                                               end,
                                                               nsamples)

    def populate_curve_points_line(self, start, end, nsamples):
        """
        Populates a list with @nsamples CurvePt elements that
        describe the curve of a lane with a line geometry type.
        If @start and @end are the same, returns an empty list.
        Otherwise, returns a list of CurvePt elements.
        """
        if start == end:
            # invalid start/end points. Return empty list
            return []

        theta = math.atan2(end[0]-start[0], end[1]-start[1])
        delta = np.linalg.norm(
            [end[0]-start[0], end[1]-start[1]]) / (nsamples-1)

        s = 0.0
        curve = [CurvePt] * nsamples
        for i in range(1, nsamples+1):
            t = (i-1)/(nsamples-1)
            P_x = start[0] + (end[0]-start[0])*t
            P_y = start[1] + (end[1]-start[1])*t
            curve[i-1] = CurvePt([P_x, P_y], theta, s, 0.0)
            s += delta

        return curve

    def populate_curve_points_arc(self, start, end, nsamples):
        """
        Populates a list with @nsamples CurvePt elements that
        describe the curve of a lanewith an arc geometry type.
        If @start and @end are the same, returns an empty list.
        Otherwise, returns a list of CurvePt elements.
        """
        if start == end:
            # invalid start/end points. Return empty list
            return []

        theta = math.atan2(end[0]-start[0], end[1]-start[1])
        delta = np.linalg.norm(
            [end[0]-start[0], end[1]-start[1]]) / (nsamples-1)

        s = 0.0
        curve = [CurvePt] * nsamples
        for i in range(1, nsamples+1):
            t = (i-1)/(nsamples-1)
            P_x = start[0] + (end[0]-start[0])*t
            P_y = start[1] + (end[1]-start[1])*t
            curve[i-1] = CurvePt([P_x, P_y], theta, s, 0.0)
            s += delta

        return curve
