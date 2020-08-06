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


def createCurves(road, lane_section, geometry, nsamples):
    """
    Given a road, lane_section and a geometry, steps through all of
    the corresponding lanes and populates a dict with
    (road_id, lane_section_id, lane_id) keys and Curve element values.
    Returns None type if geometry is of an unimplemented type.
    """
    if geometry.type is None:
        # a line
        curves = {}
        lane_section_id = road.lanes.lane_sections.index(lane_section)

        for i, side in enumerate([lane_section.left_lanes,
                                  lane_section.right_lanes]):
            previous_y = 0
            # step through each lane
            for lane in side:
                tag = (road.attrib["id"], lane_section_id, lane.attrib["id"])
                previous_y, c = createCurveLine(road,
                                                lane,
                                                geometry,
                                                previous_y, nsamples)
                if c is not None:
                    curves[tag] = c

        return curves

    # invalid geometry type
    return None


def createCurveLine(road, lane, geometry, previous_y, nsamples):
    """
    Creates a Curve element with the properties of @geometry and @lane.
    Uses @previous_y to recognize the y position of the lane with the
    preceeding id value (allows for lanes with different widths within
    the same lane_section_id). Returns a Curve element.
    """
    curve = None

    width = 4.0  # default width
    if lane.width is not None:
        width = lane.width.attrib["a"]

    length = road.attrib["length"]
    heading = geometry.attrib["hdg"]
    x1 = geometry.attrib["x"]
    x2 = geometry.attrib["x"] + length * math.cos(heading)

    y1 = geometry.attrib["y"] + previous_y
    y2 = y1 + length * math.sin(heading)

    dx = ((width * lane.attrib["id"]) * math.sin(heading))
    dy = (((width/2.0) * math.cos(heading)) *
          math.copysign(1.0, lane.attrib["id"]))

    curve = Curve(
        [x1 + dx, -(y1 + dy)],
        [x2 + dx, -(y2 + dy)],
        nsamples
    )

    previous_y = y1 + math.copysign(width, float(lane.attrib["id"]))

    return previous_y, curve
