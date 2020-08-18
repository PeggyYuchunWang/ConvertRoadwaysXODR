import math


class CurvePt:
    """
    Describes a point on a curve, associated with a curvature.

    Parameters
    ----------
    pos : list
        Global x,y position within a two element list.
    theta : float
        Orientation angle in radians.
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
        self.theta = theta
        self.s = float(s)
        self.k = float(k)
        self.kd = float(kd)

    def __str__(self):
        return (
            "CurvePt:\n"
            "   pos: <{:.8f}, {:.8f}> m\n"
            "   \u03f4: {:.8f} \u33ad ({:.8f}\u00b0)\n"
            "   s: {:.8f}\n"
            "   k: {:.8f}\n"
            "   \u03b4: {:.8f}".format(
                self.pos[0], self.pos[1],
                self.theta, math.degrees(self.theta),
                self.s,
                self.k,
                self.kd
            )
        )


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

    def __str__(self):
        return (
            "Start of curve\n{}\nEnd of curve\n{}".format(
                self.curve_points[0], self.curve_points[-1]
            )
        )

    def print_positions(self):
        print("Curve:")

        for i, point in enumerate(self.curve_points):
            print(
                "   {:d}: <{:.8f}, {:.8f}>".format(
                    i, point.pos[0], point.pos[1]
                )
            )
