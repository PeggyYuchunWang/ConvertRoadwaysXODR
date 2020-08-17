from pyxodr.data.curve import Curve
from pyxodr.data.curve import CurvePt
from pyxodr.data.spiral import Spiral
from pyxodr.data.arc import Arc
from pyxodr.data.poly3 import Poly3
from pyxodr.data.param_poly3 import ParamPoly3
from pyxodr.data.elevation import Elevation

import numpy as np

import math


def convertStringToBool(boolean_str):
    """
    Converts a string from OpenDrive's string representation of a Boolean to a
    Python Boolean.

    Expects the string to be either "true" or "false".

    Parameters
    ----------
    boolean_str : str
        A string representing a Boolean value; Either "true" or "false".

    Returns
    -------
    bool
        A Python bool of either True or False.
    """
    if boolean_str.strip().lower() == "false":
        return False
    elif boolean_str.strip().lower() == "true":
        return True


def createCurves(road, lane_section, curr_geos, nsamples):
    """
    DESCRIPTION
    """
    curves = {}
    lane_section_id = road.lanes.lane_sections.index(lane_section)

    for i, side in enumerate([lane_section.left_lanes,
                              lane_section.right_lanes]):
        if len(side) != 0:
            for geometry in curr_geos:
                current_x = geometry.attrib["x"]
                current_y = geometry.attrib["y"]

                # step through each lane
                for lane in side:
                    tag = (road.attrib["id"], lane_section_id, lane.attrib["id"])
                    current_x, current_y, c = createLaneCurve(road,
                                                              lane,
                                                              geometry,
                                                              current_x,
                                                              current_y,
                                                              nsamples)
                    if c is not None:
                        if tag in curves.keys():
                            curves[tag].curve_points.extend(c.curve_points)
                        else:
                            curves[tag] = c
    return curves


def createLaneCurve(road, lane, geometry, current_x=0, current_y=0, nsamples=2):
    """
    Creates a list of CurvePt elements that describe the properties of @geometry and @lane.
    Uses @current_y to recognize the y position of the lane with respect to the
    y position of the preceding id value (allows for lanes with different widths within
    the same lane_section_id). Returns a list of CurvePt elements.
    """
    curve = None

    width = 4.0  # default width
    if lane.width is not None:
        width = lane.width.attrib["a"]

    length = geometry.attrib["length"]
    heading = geometry.attrib["hdg"]
    s = geometry.attrib["s"]

    lane_sign = math.copysign(1.0, lane.attrib["id"])
    dx = (width/2.0) * math.sin(heading) * lane_sign
    dy = (width/2.0) * math.cos(heading) * lane_sign

    x1 = current_x
    y1 = current_y

    if geometry.type is None:
        x2 = x1 + length * math.cos(heading)
        y2 = y1 + length * math.sin(heading)

        curve = populate_curve_points_line(
            [x1 + dx, y1 + dy],
            [x2 + dx, y2 + dy],
            nsamples
        )
    elif type(geometry.type) is Arc:
        arc = geometry.type
        radius = 1.0 / arc.attrib["curvature"]
        print("x1: ", x1)
        print("y1: ", y1)

        # Calculate initial arc parameters
        phi = heading - math.pi / 2.0
        phi_total = length / radius

        x0 = x1 - radius*math.cos(phi)
        y0 = y1 - radius*math.sin(phi)
        print("x0, y0: ", x0 , " , ", y0 )
        # Calculate radius with lane center offset
        radius += math.sqrt(dx*dx + dy*dy)

        curve = populate_curve_points_arc(
            [x0, y0],
            s,
            phi,
            phi_total,
            radius,
            nsamples
        )

    # elif type(geometry.type) is Spiral:
    #     geo_type = "spiral"
    # elif type(geometry.type) is Poly3:
    #     geo_type = "poly3"
    # elif type(geometry.type) is ParamPoly3:
    #     geo_type = "polyparam3"

    next_x = x1 + (width * math.sin(heading) * lane_sign)
    next_y = y1 + (width * math.cos(heading) * lane_sign)

    # TODO Pass back dx and dy? Do all lanes in a lane sections at once instead?

    return next_x, next_y, curve


def populate_curve_points_line(start, end, nsamples=2):
    """
    Populates a Curve element with @nsamples CurvePt elements that
    describe the curve of a lane with a line geometry type.
    If @start and @end are the same, returns None.
    Otherwise, returns a Curve element populated with CurvePt elements.
    """
    if start == end:
        # invalid start/end points
        return None

    theta = math.atan2(end[1]-start[1], end[0]-start[0])
    delta = np.linalg.norm([end[0]-start[0], end[1]-start[1]]) / (nsamples-1)

    s = 0.0
    curve_points = [CurvePt] * nsamples
    for i in range(1, nsamples+1):
        t = (i-1)/(nsamples-1)
        P_x = start[0] + (end[0]-start[0])*t
        P_y = start[1] + (end[1]-start[1])*t
        curve_points[i-1] = CurvePt([P_x, P_y], theta, s, 0.0)
        s += delta

    return Curve(curve_points)


def populate_curve_points_arc(
    center,
    s,
    theta,
    theta_total,
    radius,
    nsamples=3
):
    """
    """
    arc_length = theta_total * radius
    delta_arc = arc_length / nsamples
    delta_theta = (theta_total - theta) / nsamples

    curve_points = [CurvePt] * nsamples

    for i in range(0, nsamples):
        P_x = radius * math.cos(theta) + center[0]
        P_y = radius * math.sin(theta) + center[1]
        curve_points[i] = CurvePt([P_x, P_y], theta, s, 0.0)
        s += delta_arc
        theta += delta_theta
        print("P_{}: {}".format(i, [P_x, P_y]))

    return Curve(curve_points)
