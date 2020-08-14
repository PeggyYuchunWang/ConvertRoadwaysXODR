import math
import numpy as np
from scipy.optimize import fsolve
from pyxodr.data.curve import Curve
from pyxodr.data.curve import CurvePt
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
                    # print("current_x: ", current_x)
                    # print("current_y: ", current_y)
                    tag = (road.attrib["id"], lane_section_id, lane.attrib["id"])
                    current_x, current_y, c = createLaneCurve(road,
                                                              lane,
                                                              geometry,
                                                              current_x,
                                                              current_y,
                                                              nsamples)
                    if c is not None:
                        if tag in curves.keys():
                            curves[tag].curve_points.extend(c.curve_points) #[1:])
                        else:
                            curves[tag] = c
                
                # for k in curves.keys():
                #     print(k)
                #     c = curves[k]
                #     for cp in c:
                #         print(cp.pos)
                #     print()
    return curves

    # invalid geometry type
    return None


def createLaneCurve(road, lane, geometry, current_x=0, current_y=0, nsamples=2):
    """
    Creates a list of CurvePt elements that describe the properties of @geometry and @lane.
    Uses @current_y to recognize the y position of the lane with respect to the
    y position of the preceeding id value (allows for lanes with different widths within
    the same lane_section_id). Returns a list of CurvePt elements.
    """
    curve = None

    width = 4.0  # default width
    if lane.width is not None:
        width = lane.width.attrib["a"]

    length = geometry.attrib["length"]
    heading = geometry.attrib["hdg"]

    lane_sign = math.copysign(1.0, lane.attrib["id"])
    dx = (width/2.0) * math.sin(heading) * lane_sign 
    dy = (width/2.0) * math.cos(heading) * lane_sign

    if geometry.type is None:
        x1 = current_x
        x2 = x1 + length * math.cos(heading)

        y1 = current_y
        y2 = y1 + length * math.sin(heading)

        curve = populate_curve_points_line(
            [x1 + dx, y1 + dy],
            [x2 + dx, y2 + dy],
            nsamples
        )     
    elif type(geometry.type) is Arc:
        arc = geometry.type

        x1 = current_x
        y1 = current_y
        print("x1: ", x1)
        print("y1: ", y1)
        radius = 1.0 / arc.attrib["curvature"]
        r_squared = math.pow(radius,2)

        # solve for center points of circle that represents the arc
        # root = fsolve(arc_equations, [x1*.95, y1*.95], args=(x1, y1, radius, heading))
        # print(np.isclose(arc_equations(root, x1, y1, radius, heading), [0.0, 0.0]))
        
        x0 = x1 - math.sqrt(r_squared / (1 - math.pow(math.tan(heading), 2)))
        y0 = y1 - math.sqrt(r_squared - math.pow((x1-x0),2))
        
        print("x0, y0: ", x0 , " , ", y0 )
        
        # print("r^2 ", math.pow(radius,2), " = ", math.pow((x1 - x0), 2) - math.pow((y1 - y0), 2))  # set equal to radius^2
        # print("heading ", heading, " = ", math.atan((y1-y0)/(x1-x0)))

        curve = populate_curve_points_arc(
            [x1 + dx, y1 + dy],
            [x0, y0],
            heading,
            radius,
            geometry.attrib["length"],
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

def populate_curve_points_arc(start, center, heading, radius, arc_length, nsamples=3):
        """
        
        """
        if start == center:
            # invalid start/center points
            return None

        theta_end = arc_length / radius  
        theta = heading  
        delta_theta = (arc_length / (nsamples-1)) / radius

        s = 0.0
        curve_points = [CurvePt] * nsamples
        for i in range(0, nsamples):
            cp_theta = theta_end - theta
            P_x = radius * math.cos(cp_theta) + center[0]
            P_y = radius * math.sin(cp_theta) + center[1]
            curve_points[i] = CurvePt([P_x, P_y], cp_theta, s, 0.0)
            s += P_x
            theta += delta_theta

        return Curve(curve_points)

def arc_equations(vars, x1, y1, radius, heading):
    x0, y0 = vars
    eq1 = math.pow((x1-x0), 2) + math.pow((y1-y0), 2) - math.pow(radius, 2) 
    eq2 = math.atan((y1-y0)/(x1-x0)) - heading 
    return eq1, eq2
