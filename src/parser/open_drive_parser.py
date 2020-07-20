import xml.etree.ElementTree as ET
import src.parser.open_drive_roadways as rw
import src.utils as utils
import src.data.open_drive_framework as odf

from src.data.header import Header
from src.data.geo_reference import Geo_Reference
from src.data.offset import Offset

from src.data.road import Road
from src.data.road_predecessor_successor import Road_Predecessor_Successor
from src.data.road_neighbor import Road_Neighbor
from src.data.road_type import Road_Type
from src.data.road_speed import Road_Speed

from src.data.geometry import Geometry
from src.data.spiral import Spiral
from src.data.arc import Arc
from src.data.poly3 import Poly3
from src.data.param_poly3 import Param_Poly3
from src.data.elevation import Elevation

from src.data.lateral_profile import Lateral_Profile
from src.data.lateral_profile_superelevation import Lateral_Profile_Superelevation
from src.data.lateral_profile_shape import Lateral_Profile_Shape

from src.data.lanes import Lanes
from src.data.lane_offset import Lane_Offset
from src.data.lane_section import Lane_Section
from src.data.lane import Lane
from src.data.lane_width import Lane_Width
from src.data.lane_height import Lane_Height
from src.data.lane_border import Lane_Border
from src.data.lane_material import Lane_Material
from src.data.lane_visibility import Lane_Visibility
from src.data.lane_access import Lane_Access
from src.data.lane_rule import Lane_Rule
from src.data.lane_speed import Lane_Speed

from src.data.road_mark import Road_Mark
from src.data.road_mark_type import Road_Mark_Type
from src.data.road_mark_line import Road_Mark_Line
from src.data.road_mark_sway import Road_Mark_Sway
from src.data.road_mark_explicit import Road_Mark_Explicit
from src.data.road_mark_explicit_line import Road_Mark_Explicit_Line

from src.data.junction import Junction
from src.data.junction_connection import Junction_Connection
from src.data.junction_lane_link import Junction_Lane_Link
from src.data.junction_priority import Junction_Priority
from src.data.junction_predecessor_successor import Junction_Predecessor_Successor
from src.data.junction_group import Junction_Group
from src.data.junction_controller import Junction_Controller


class OpenDriveParser:
    def __init__(self):
        self.data = odf.Open_Drive_Framework()

    def parse_file(self, filename="test_data/carlaExs/Town02.xodr"):
        print("parsing: ", filename)
        root = ET.parse(filename).getroot()
        self.__parse(xml_root=root)  
        print("done parsing: ", filename)    

    def __parse(self, xml_root):
        
        #fills in the header node information
        for header in xml_root.findall("header"):
            self.__parse_header(self.data, header)

        for road in xml_root.findall("road"):
            self.__parse_road(self.data, road)

        for junc in xml_root.findall("junction"):
            self.__parse_junction(self.data, junc)

    def __parse_header(self, framework, header):
        if header.attrib:
            att = header.attrib
            framework.header = Header(
                int(att["revMajor"]),
                int(att["revMinor"])
            )
            if "name" in att:
                framework.header.attrib["name"] = att["name"]
            if "version" in att:
                framework.header.attrib["version"] = att["version"]
            if "date" in att:
                framework.header.attrib["date"] = att["date"]
            if "north" in att:
                framework.header.attrib["north"] = float(att["north"])
            if "south" in att:
                framework.header.attrib["south"] = float(att["south"])
            if "east" in att:
                framework.header.attrib["east"] = float(att["east"])
            if "west" in att:
                framework.header.attrib["west"] = float(att["west"])
            if "vendor" in att:
                framework.header.attrib["vendor"] = att["vendor"]
        for child in header:
            if child.tag == "userData":
                #I think that in ver1.6 User Data is not found in this way
                continue
                #for v in child:
                #    if v.tag == "vectorScene":
                #        att = v.attrib
                #        framework.Geo_Reference.vectorScene = rw.VectorScene(
                #            att["program"], att["version"])
            elif child.tag == "geoReference":
                framework.header.geo_reference = Geo_Reference(child.text)
            elif child.tag == "offset":
                if child.attrib:
                    att = child.attrib
                    framework.header.offset = Offset(
                        float(att["x"]),
                        float(att["y"]),
                        float(att["z"]),
                        float(att["hdg"])
                    )

    def __parse_road(self, framework, road):
        att = road.attrib
        r = Road(
            att["id"],
            float(att["length"]),
            att["junction"]
        )
        if "name" in att:
            r.attrib["name"] = att["name"]
        if "rule" in att:
            r.attrib["rule"] = att["rule"]
        
        self.__parse_road_predecessor_and_successor(r, road.find("link/predecessor"), road.find("link/successor"))

        for neighbor in road.findall("neighbor"):
            att = neighbor.attrib
            n = Road_Neighbor(
                att["side"],
                att["elementId"],
                att["direction"]
            )
            r.neighbors.append(n)

        type = road.find("type")
        if type is not None:
            att = type.attrib
            r.type = Road_Type(
                float(att["s"]),
                str(att["type"])
            )
            if "country" in att:
                r.type.attrib["country"] = att["country"]
            for child in type:
                if child.tag == "speed":
                    att = child.attrib
                    r.type.speed = Road_Speed(float(att["max"]))
                if "unit" in att:
                    r.type.speed.attrib["unit"] = att["unit"]
                else:
                    print("unkown type child tag: ", child.tag)
        
        self.__parse_road_geometrys(r, road.findall("planView/geometry"))

        elevations = road.findall("elevationProfile/elevation")
        for ele in elevations:
            att = ele.attrib
            e = Elevation(
                float(att["s"]),
                float(att["a"]),
                float(att["b"]),
                float(att["c"]),
                float(att["d"])
            )
            r.elevation_profile.append(e)

        self.__parse_road_lateral_profile(r, road.findall("lateralProfile"))

        r.lanes = self.__parse_lanes(road.find("lanes"))
        framework.roads[r.attrib["id"]] = r

    def __parse_road_predecessor_and_successor(self, r, pred, succ):
        if pred is not None:
            att = pred.attrib
            r.predecessor = Road_Predecessor_Successor(
                att["elementType"], 
                int(att["elementId"]),
                att["contactPoint"]
            )
            # if "contactPoint" in att:
            #     r.predecessor.attrib["contact_point"] = att["contactPoint"]
            if "elementS" in att:
                r.predecessor.attrib["element_s"] = int(att["elementS"])
            if "elementDir" in att:
                r.predecessor.attrib["element_dir"] = int(att["elementDir"])
        
        if succ is not None:
            att = succ.attrib
            r.successor = Road_Predecessor_Successor(
                att["elementType"], 
                int(att["elementId"]),
                att["contactPoint"]
            )
            # if "contactPoint" in att:
            #     r.successor.attrib["contact_point"] = att["contactPoint"]
            if "elementS" in att:
                r.successor.attrib["element_s"] = int(att["elementS"])
            if "elementDir" in att:
                r.successor.attrib["element_dir"] = int(att["elementDir"])

    def __parse_road_geometrys(self, r, geos):
        for g in geos:
            att = g.attrib
            geo = Geometry(
                float(att["s"]),
                float(att["x"]),
                float(att["y"]),
                float(att["hdg"]),
                float(att["length"])
            )
            for child in g:
                if child.tag == "line":
                    continue           
                elif child.tag == "spiral":
                    att = child.attrib
                    geo.type = Spiral(
                        float(att["curvStart"]),
                        float(att["curvEnd"])
                    )
                elif child.tag == "arc":
                    geo.type = Arc(float(child.attrib["curvature"]))
                elif child.tag == "poly3":
                    att = child.attrib
                    geo.type = Poly3(
                        float(att["a"]), 
                        float(att["b"]),
                        float(att["c"]), 
                        float(att["d"])
                    )
                elif child.tag == "paramPoly3":
                    att = child.attrib
                    geo.type = Param_Poly3(att["pRange"], float(att["aU"]),
                                float(att["bU"]), float(att["cU"]),
                                float(att["dU"]), float(att["aV"]),
                                float(att["bV"]), float(att["cV"]),
                    )
                else:
                    print("unkown geometry child tag: ", child.tag)
            r.plan_view.append(geo)

    def __parse_road_lateral_profile(self, r, lateral_profile):
        for child in lateral_profile:
            att = child.attrib
            r.lateral_profile = Lateral_Profile()
            if child.tag == "superelevation":
                se = Lateral_Profile_Superelevation(
                    float(att["s"]),
                    float(att["a"]),
                    float(att["b"]),
                    float(att["c"]),
                    float(att["d"])
                )
                r.lateral_profile.super_elevation = se
            elif child.tag == "shape":
                s = Lateral_Profile_Shape(
                    float(att["s"]),
                    float(att["t"]),
                    float(att["a"]),
                    float(att["b"]),
                    float(att["c"]),
                    float(att["d"])
                )
                r.lateral_profile.shapes.append(s)
            elif child.tag == "lateralProfile":
                continue
            else:
                print("unkown lateral profile child: ", child.tag)

    def __parse_lanes(self, lanes):
        output = Lanes()
        laneOffset = lanes.findall("laneOffset")
        for lo in laneOffset:
            att = lo.attrib
            # Standard has "t_grEqZero" as element of [0, inf)
            offset = Lane_Offset(
                float(att["s"]),
                float(att["a"]),
                float(att["b"]),
                float(att["c"]),
                float(att["d"])
            )
            output.lane_offset = offset
        
        self.__parse_lane_sections(output, lanes, lanes.findall("laneSection"))

        return output

    def __parse_lane_sections(self, output, lanes, laneSection):
        for ls in laneSection:
            att = ls.attrib
            section = Lane_Section(float(att["s"]))
            if "singleSide" in att:
                section.attrib["single_side"] = utils.convertStringToBool(att["singleSide"])

            left = lanes.findall("laneSection/left/lane")
            right = lanes.findall("laneSection/right/lane")
            center = lanes.findall("laneSection/center/lane")
            for i, side in enumerate([left, right, center]):
                for l in side:
                    att = l.attrib
                    lane = Lane(
                        int(att["id"]),
                        att["type"]
                    )
                    if "level" in att:
                        lane.attrib["level"] = utils.convertStringToBool(att["level"])

                    pred = l.find("link/predecessor")
                    if pred is not None:
                        lane.predecessor_id = int(pred.attrib["id"])
                    
                    succ = l.find("link/successor")
                    if succ is not None:
                        lane.successor_id = int(succ.attrib["id"])
                    
                    width = l.find("width")
                    if width is not None:
                        att = width.attrib
                        lane.width = Lane_Width(
                            float(att["sOffset"]),
                            float(att["a"]),
                            float(att["b"]),
                            float(att["c"]),
                            float(att["d"])
                        )

                    border = l.find("border")
                    if border is not None:
                        att = border.attrib
                        lane.border= Lane_Border(
                            float(att["sOffset"]),
                            float(att["a"]),
                            float(att["b"]),
                            float(att["c"]),
                            float(att["d"])
                        )

                    material = l.find("material")
                    if material is not None:
                        att = material.attrib
                        lane.material = Lane_Material(
                            float(att["sOffset"]),
                            float(att["friction"])
                        )
                        if "surface" in att:
                            lane.road_mark.attrib["surface"] = att["surface"]
                        if "roughness" in att:
                            lane.road_mark.attrib["roughness"] = float(att["roughness"])
                    
                    visibility = l.find("visibility")
                    if visibility is not None:
                        att = visibility.attrib
                        lane.visibility = Lane_Visibility(
                            float(att["sOffset"]),
                            float(att["forward"]),
                            float(att["back"]),
                            float(att["left"]),
                            float(att["right"])
                        )
                    
                    speed = l.find("speed")
                    if speed is not None:
                        att = speed.attrib
                        lane.speed = Lane_Speed(
                            float(att["sOffset"]),
                            float(att["max"])
                        )
                        if "unit" in att:
                            lane.speed.attrib["unit"] = att["unit"]

                    access = l.find("access")
                    if access is not None:
                        att = access.attrib
                        lane.access = Lane_Access(
                            float(att["sOffset"]),
                            att["rule"],
                            att["restriction"]
                        )

                    height = l.find("height")
                    if height is not None:
                        att = height.attrib
                        lane.height= Lane_Height(
                            float(att["sOffset"]),
                            float(att["inner"]),
                            float(att["outer"])
                        )

                    rule = l.find("rule")
                    if rule is not None:
                        att = rule.attrib
                        lane.rule = Lane_Rule(
                            float(att["sOffset"]),
                            att["value"]
                        )

                    self.__parse_road_mark(lane, l.find("roadMark"))

                    vl = l.find("userData/vectorLane")
                    if vl is not None:
                        lane.travelDir = vl.attrib["travelDir"]

                    if i == 0:
                        section.left_lanes.append(lane)
                    elif i == 1:
                        section.right_lanes.append(lane)
                    elif i == 2:
                        section.center_lane = lane
            output.lane_sections.append(section)

    def __parse_road_mark(self, lane, road_mark):
        if road_mark is not None:
            att = road_mark.attrib
            lane.road_mark = Road_Mark(
                float(att["sOffset"]),
                att["type"],
                att["color"]
            )
            if "material" in att:
                lane.road_mark.attrib["material"] = att["material"]
            if "width" in att:
                lane.road_mark.attrib["width"] = float(att["width"])
            if "laneChange" in att:
                lane.road_mark.attrib["lane_change"] = att["laneChange"]
            if "height" in att:
                lane.road_mark.attrib["height"] = float(att["height"])
            
            for child in road_mark:
                if child.tag == "type":
                    att = child.attrib
                    type = Road_Mark_Type(
                        att["name"],
                        float(att["width"])
                    )
                    for l in child:
                        att = l.attrib
                        line = Road_Mark_Line(
                            float(att["length"]),
                            float(att["space"]),
                            float(att["tOffset"]),
                            float(att["sOffset"]),
                            float(att["width"])
                        )
                        if "rule" in att:
                            line.attrib["rule"] = att["rule"]
                        if "color" in att:
                            line.attrib["color"] = att["color"]
                        type.lines.append(line)
                    lane.road_mark.type = type
                elif child.tag == "sway":
                    att = child.attrib
                    sway = Road_Mark_Sway(
                        float(att["ds"]),
                        float(att["a"]), 
                        float(att["b"]),
                        float(att["c"]), 
                        float(att["d"])
                    )
                    lane.road_mark.sway = sway
                elif child.tag == "explicit":
                    att = child.attrib
                    ex = Road_Mark_Explicit(
                        att["name"],
                        float(att["width"])
                    )
                    for l in child:
                        att = l.attrib
                        ex_line = Road_Mark_Explicit_Line(
                            float(att["length"]),
                            float(att["tOffset"]),
                            float(att["sOffset"]),
                            att["rule"],
                            float(att["width"])
                        )
                        if "rule" in att:
                            ex_line.attrib["rule"] = att["rule"]
                        ex.lines.append(ex_line)
                    lane.road_mark.explicit = ex            
                else:
                    print("unkown road mark child tag: ", child.tag)

    def __parse_objects(self, framework):
        print()

    def __parse_junction(self, framework, junc):
        att = junc.attrib
        j = Junction(
            att["id"]
        )
        if "name" in att:
                j.type = att["name"]
        if "type" in att:
                j.type = att["type"]
        
        connections = junc.finall("connection")
        for connection in connections:
            att = connection.attrib
            c = Junction_Connection(
                att["id"],
                att["incomingRoad"],
                att["connectingRoad"],
                att["contactPoint"]          
            )
            if "type" in att:
                c.attrib["type"] = att["type"]

            pred = connection.find("predecessor")
            if pred is not None:
                c.predecessor = Junction_Predecessor_Successor(
                    att["elementType"],
                    att["elementId"],
                    att["elementS"],
                    att["elementDir"],
                )
                    
            succ = connection.find("successor")
            if succ is not None:
                c.successor = Junction_Predecessor_Successor(
                    att["elementType"],
                    att["elementId"],
                    att["elementS"],
                    att["elementDir"],
                )
            
            links = connection.findall("laneLink")
            for ll in links:
                att = ll.attrib
                link = Junction_Lane_Link(
                    att["from"], 
                    att["to"]
                )
                c.lane_links.append(link)
            j.connections.append(c)

        priorities = junc.findall("priority")
        for p in priorities:
            att = p.attrib
            priority = Junction_Priority()
            if "high" in att:
                priority.attrib["high"] = att["high"]
            if "low" in att:
                priority.attrib["low"] = att["low"]
            j.priorities.append(priority)

        controllers = junc.findall("controller")
        for control in controllers:
            att = control.attrib
            c = Junction_Controller(att["id"])   
            if "type" in att:
                c.attrib["type"] = att["type"]
            if "sequence" in att:
                c.attrib["sequence"] = att["sequence"]           
            j.controllers.append(c)
            
        framework.junctions[j.attrib["id"]] = j

    
