import math
from pyxodr.data.curve import Curve


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


def createCurve(road, lane_section_id, lane, geometry):
    if geometry.type is None:
        # a line
        return createCurveLine(road, lane_section_id, lane, geometry)

    # invalid geometry type
    return None, None


def createCurveLine(road, lane_section_id, lane, geometry):
    tag = (road.attrib["id"], lane_section_id, lane.attrib["id"])
    curve = None

    width = 4.0  # default width
    if lane.width is not None:
        width = lane.width.attrib["a"]
    
    length = road.attrib["length"]
    heading = geometry.attrib["hdg"]
    x1 = geometry.attrib["x"]
    x2 = geometry.attrib["x"] + length * math.cos(heading)

    # y_offset = (lane.attrib["id"] * width) + (width / 2.0)
    y1 = geometry.attrib["y"]
    y2 = geometry.attrib["y"] + length * math.sin(heading)
    dx = ((width * float(lane.attrib["id"])) * math.sin(heading))
    dy = ((width * float(lane.attrib["id"])) * math.cos(heading)) + (width / 2.0)
    curve = Curve(
        [x1 + dx, -(y1 + dy)],
        [x2 + dx, -(y2 + dy)],
        2
    )
    return tag, curve
