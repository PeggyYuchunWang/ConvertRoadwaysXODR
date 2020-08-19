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


def generateRoadCurves(road, nsamples):
    curves = {}

    section_id = 0

    for i, geom in enumerate(road.plan_view):
        if len(road.lanes.lane_sections) == 1:
            section_id = i + 1
            createSectionCurves(
                curves,
                road.attrib["id"],
                road.lanes.lane_sections[0],
                section_id,
                geom,
                nsamples
            )
        else:
            # TODO: Figure out how to handle multiple lane sections with
            # multiple geometries
            pass

    return curves


def createSectionCurves(curves, road_id, lane_section, section_id, geometry, nsamples):
    """
    DESCRIPTION
    """
    x_offset = 0.0
    y_offset = 0.0

    # Generate the curves for the left lanes
    if lane_section.left_lanes:
        lane_section.left_lanes.reverse()
        for lane in lane_section.left_lanes:
            tag = (road_id, section_id, lane.attrib["id"])
            x_offset, y_offset, c = createLaneCurve(
                lane,
                geometry,
                x_offset,
                y_offset,
                nsamples
            )

            if c is not None:
                curves[tag] = c

    # Must reset offset values for other side of road
    x_offset = 0.0
    y_offset = 0.0

    if lane_section.right_lanes:
        for lane in lane_section.right_lanes:
            tag = (road_id, section_id, lane.attrib["id"])
            x_offset, y_offset, c = createLaneCurve(
                lane,
                geometry,
                x_offset,
                y_offset,
                nsamples
            )

            if c is not None:
                curves[tag] = c


def createLaneCurve(lane, geometry, x_offset, y_offset, nsamples):
    """
    Creates a list of CurvePt elements that describe the properties of @geometry and @lane.
    Uses @y_offset to recognize the y position of the lane with respect to the
    y position of the preceding id value (allows for lanes with different widths within
    the same lane_section_id). Returns a list of CurvePt elements.
    """
    curve = None

    width = 4.0  # default width
    if lane.width is not None:
        width = lane.width.attrib["a"]

    s = geometry.attrib["s"]
    x_start = geometry.attrib["x"]
    y_start = geometry.attrib["y"]
    heading = geometry.attrib["hdg"]
    length = geometry.attrib["length"]

    # Calculate the distance to the center of the lane
    lane_sign = math.copysign(1.0, lane.attrib["id"])
    dx = (width/2.0) * math.sin(-heading) * lane_sign
    dy = (width/2.0) * math.cos(heading) * lane_sign

    # Calculate the new start position of the curve after offset and distance
    # to center of lane
    x_start += x_offset + dx
    y_start += y_offset + dy

    if geometry.type is None:
        x_end = x_start + length * math.cos(heading)
        y_end = y_start + length * math.sin(heading)

        curve = populate_curve_points_line(
            [x_start, y_start],
            [x_end, y_end],
            nsamples
        )
    elif type(geometry.type) is Arc:
        arc = geometry.type
        radius = 1.0 / arc.attrib["curvature"]

        # Calculate initial arc parameters
        phi = heading - math.pi / 2.0
        phi_total = length / radius

        # Calculate radius and circle center with lane center offset
        radius += math.sqrt(
            math.pow(x_offset + dx, 2) + math.pow(y_offset + dy, 2)
        )
        x0 = x_start - radius*math.cos(phi)
        y0 = y_start - radius*math.sin(phi)

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

    # Update x and y offset with distance to far end of lane
    x_offset += 2.0*dx
    y_offset += 2.0*dy

    return x_offset, y_offset, curve


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
    delta_arc = arc_length / (nsamples - 1)
    delta_theta = theta_total / (nsamples - 1)

    curve_points = [CurvePt] * nsamples

    for i in range(0, nsamples):
        P_x = radius * math.cos(theta) + center[0]
        P_y = radius * math.sin(theta) + center[1]
        curve_points[i] = CurvePt([P_x, P_y], theta + math.pi/2.0, s, 0.0)
        s += delta_arc
        theta += delta_theta

    return Curve(curve_points)
