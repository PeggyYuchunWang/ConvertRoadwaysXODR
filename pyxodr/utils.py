import math
from pyxodr.data.curve import Curve
from pyxodr.data.spiral import Spiral
from pyxodr.data.arc import Arc
from pyxodr.data.poly3 import Poly3
from pyxodr.data.param_poly3 import ParamPoly3
from pyxodr.data.elevation import Elevation


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


def createCurves(road, lane_section, geometry, nsamples):
    """
    Given a road, lane_section and a geometry, steps through all of
    the corresponding lanes and populates a dict with
    (road_id, lane_section_id, lane_id) keys and Curve element values.
    Returns None type if geometry is of an unimplemented type.
    """
    curves = {}
    lane_section_id = road.lanes.lane_sections.index(lane_section)

    for i, side in enumerate([lane_section.left_lanes,
                                lane_section.right_lanes]):
        current_y = geometry.attrib["y"]
        
        # step through each lane
        for lane in side:
            tag = (road.attrib["id"], lane_section_id, lane.attrib["id"])
            current_y, c = createCurveLine(road,
                                            lane,
                                            geometry,
                                            current_y,
                                            nsamples)
            if c is not None:
                curves[tag] = c
    return curves

    # invalid geometry type
    return None


def createCurveLine(road, lane, geometry, current_y=0, nsamples=2):
    """
    Creates a Curve element with the properties of @geometry and @lane.
    Uses @current_y to recognize the y position of the lane with respect to the
    preceeding id value (allows for lanes with different widths within
    the same lane_section_id). Returns a Curve element.
    """
    curve = None

    geo_type = "line"
    if geometry.type is not None:
        if type(geometry.type) is Arc:
            geo_type = "arc"
        if type(geometry.type) is Spiral:
            geo_type = "spiral"
        if type(geometry.type) is Poly3:
            geo_type = "poly3"
        if type(geometry.type) is ParamPoly3:
            geo_type = "polyparam3"

    width = 4.0  # default width
    if lane.width is not None:
        width = lane.width.attrib["a"]

    length = road.attrib["length"]
    heading = geometry.attrib["hdg"]

    x1 = geometry.attrib["x"]
    x2 = x1 + length * math.cos(heading)

    y1 = current_y
    y2 = y1 + length * math.sin(heading)

    dx = ((width * math.copysign(1.0, lane.attrib["id"])) * math.sin(heading))
    dy = (((width/2.0) * math.cos(heading)) *
          math.copysign(1.0, lane.attrib["id"]))

    curve = Curve(
        [x1 + dx, -(y1 + dy)],
        [x2 + dx, -(y2 + dy)],
        nsamples,
        geo_type
    )

    next_y = y1 + (math.copysign(width, float(lane.attrib["id"]) * math.cos(heading))) 

    return next_y, curve
