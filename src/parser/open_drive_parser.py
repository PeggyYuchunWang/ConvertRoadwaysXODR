import xml.etree.ElementTree as ET
import src.parser.open_drive_roadways as rw
import src.utils as utils
import src.data.open_drive_framework as odf

from src.data.header import Header
from src.data.geo_reference import Geo_Reference
from src.data.offset import Offset
from src.data.road import Road
from src.data.road_predecessor_successor import Road_Predecessor_Successor
from src.data.road_type import Road_Type
from src.data.road_speed import Road_Speed
from src.data.geometry import Geometry
from src.data.spiral import Spiral
from src.data.arc import Arc
from src.data.poly3 import Poly3
from src.data.param_poly3 import Param_Poly3
from src.data.elevation import Elevation
from src.data.lateral_profile_superelevation import Lateral_Profile_Superelevation
from src.data.lateral_profile_shape import Lateral_Profile_Shape

from src.data.lanes import Lanes
from src.data.lane_offset import Lane_Offset
from src.data.lane_section import Lane_Section
from src.data.lane import Lane
from src.data.lane_width import Lane_Width
from src.data.lane_border import Lane_Border

from src.data.road_mark import Road_Mark
from src.data.road_mark_type import Road_Mark_Type
from src.data.road_mark_line import Road_Mark_Line


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

        #for junc in xml_root.findall("junction"):
        #    self.__parseJunction(self.data, junc)

    def __parse_header(self, framework, header):
        if header.attrib:
            att = header.attrib
            framework.header = Header(
                int(att["revMajor"]),
                int(att["revMinor"]),
                att["name"],
                att["version"],
                att["date"],
                float(att["north"]),
                float(att["south"]),
                float(att["east"]),
                float(att["west"])
            )
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
        
        pred = road.find("link/predecessor")
        if pred is not None:
            att = pred.attrib
            r.predecessor = Road_Predecessor_Successor(
                att["elementType"], 
                int(att["elementId"])
            )
            if "contactPoint" in att:
                r.predecessor.attrib["contact_point"] = att["contactPoint"]
            if "elementS" in att:
                r.predecessor.attrib["element_s"] = int(att["elementS"])
            if "elementDir" in att:
                r.predecessor.attrib["element_dir"] = int(att["elementDir"])
        
        succ = road.find("link/successor")
        if succ is not None:
            att = succ.attrib
            r.successor = Road_Predecessor_Successor(
                att["elementType"], 
                int(att["elementId"])
            )
            if "contactPoint" in att:
                r.successor.attrib["contact_point"] = att["contactPoint"]
            if "elementS" in att:
                r.successor.attrib["element_s"] = int(att["elementS"])
            if "elementDir" in att:
                r.successor.attrib["element_dir"] = int(att["elementDir"])

        type = road.find("type")
        if type is not None:
            att = type.attrib
            r.type = Road_Type(
                float(att["s"]),
                str(att["type"]),
                str(att["country"])
            )
            for child in type:
                if child.tag == "speed":
                    att = child.attrib
                    r.type.speed = Road_Speed(
                        float(att["max"]),
                        att["unit"]
                    )
        
        geos = road.findall("planView/geometry")
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
                    print(child.tag)
            r.plan_view.append(geo)

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
            r.elevation_profile = e

        lateral_profile = road.findall("lateralProfile")
        for child in lateral_profile:
            att = child.attrib
            if child.tag == "superelevation":
                se = Lateral_Profile_Superelevation(
                    float(att["s"]),
                    float(att["a"]),
                    float(att["b"]),
                    float(att["c"]),
                    float(att["d"])
                )
                r.lateral_profile["super_elevation"] = se
            elif child.tag == "shape":
                s = Lateral_Profile_Shape(
                    float(att["s"]),
                    float(att["t"]),
                    float(att["a"]),
                    float(att["b"]),
                    float(att["c"]),
                    float(att["d"])
                )
                r.lateral_profile["shapes"].append(s)
            else:
                print(child.tag)

        r.lanes = self.__parse_lanes(road.find("lanes"))
        framework.roads[r.attrib["id"]] = r

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
        
        laneSection = lanes.findall("laneSection")
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
                        att["type"],
                        utils.convertStringToBool(att["level"])
                    )
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

                    
                    road_mark = l.find("roadMark")
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
                            lane.road_mark.attrib["lane_change"] = float(att["laneChange"])
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
                                        att["rule"],
                                        float(att["width"])
                                    )
                                    type.lines.append(line)
                                lane.road_mark.type = type
                            else:
                                print(child.tag)

                    vl = l.find("userData/vectorLane")
                    if vl is not None:
                        lane.travelDir = vl.attrib["travelDir"]

                    if i == 0:
                        section.left_lanes[lane.attrib["id"]] = lane
                    elif i == 1:
                        section.right_lanes[lane.attrib["id"]] = lane
                    elif i == 2:
                        section.center_lane = lane

            output.lane_sections.append(section)
        return output


    def __parseJunction(self, roadways, junc):
        att = junc.attrib
        j = rw.Junction(att["id"], att["name"])
        if "type" in att:
                j.type = att["type"]
        for connection in junc:
            att = connection.attrib
            c = rw.connection(
                att["id"])
            if "type" in att:
                c.type = att["type"]
            if "incomingRoad" in att:
                c.incomingRoad = att["incomingRoad"]
            if "connectingRoad" in att:
                c.connectingRoad = att["connectingRoad"]
            if "contactPoint" in att:
                c.contactPoint = att["contactPoint"]
            ll = connection.find("laneLink")
            if ll is not None:
                c.laneLink = rw.LaneLink(ll.attrib["from"], ll.attrib["to"])
            j.connections.append(c)
        roadways.junctions[j.id] = j

    
