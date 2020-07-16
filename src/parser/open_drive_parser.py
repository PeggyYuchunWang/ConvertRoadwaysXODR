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
from src.data.geometry import Geometry
from src.data.spiral import Spiral
from src.data.arc import Arc
from src.data.poly3 import Poly3
from src.data.param_poly3 import Param_Poly3

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

    def __parse_lanes(self, lanes):
        output = rw.Lanes()
        laneOffset = lanes.findall("laneOffset")
        for lo in laneOffset:
            att = lo.attrib
            # Standard has "t_grEqZero" as element of [0, inf)
            offset = rw.LaneOffset(
                float(att["s"]),
                float(att["a"]),
                float(att["b"]),
                float(att["c"]),
                float(att["d"])
            )
            output.laneOffset.append(offset)
        laneSection = lanes.findall("laneSection")
        for ls in laneSection:
            att = ls.attrib
            section = rw.LaneSection(float(att["s"]))
            if "singleSide" in att:
                section.single_side = utils.convertStringToBool(att["singleSide"])
            left = lanes.findall("laneSection/left/lane")
            right = lanes.findall("laneSection/right/lane")
            center = lanes.findall("laneSection/center/lane")
            for i, side in enumerate([left, right, center]):
                for l in side:
                    att = l.attrib
                    lane = rw.Lane(
                        int(att["id"]),
                        att["type"],
                        utils.convertStringToBool(att["level"])
                    )
                    pred = l.find("link/predecessor")
                    if pred is not None:
                        lane.predecessorId = int(pred.attrib["id"])
                    succ = l.find("link/successor")
                    if succ is not None:
                        lane.successorId = int(succ.attrib["id"])
                    width = l.find("width")
                    if width is not None:
                        att = width.attrib
                        lane.width = rw.Width(
                            float(att["sOffset"]),
                            float(att["a"]),
                            float(att["b"]),
                            float(att["c"]),
                            float(att["d"])
                        )
                    roadMark = l.find("roadMark")
                    if roadMark is not None:
                        att = roadMark.attrib
                        lane.roadMark = rw.RoadMark(
                            float(att["sOffset"]),
                            att["type"],
                            att["lanechange"]
                        )
                        if "material" in att:
                            lane.roadMark.material = att["material"]
                        if "width" in att:
                            lane.roadMark.width = float(att["width"])
                    vl = l.find("userData/vectorLane")
                    if vl is not None:
                        lane.travelDir = vl.attrib["travelDir"]
                    if i == 0:
                        section.left[lane.id] = lane
                    elif i == 1:
                        section.right[lane.id] = lane
                    elif i == 2:
                        section.center[lane.id] = lane
            output.laneSection.append(section)
        return output

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
                                float(att["dV"]))
                    geo.type_name = "paramPoly3"
                else:
                    print(child)
            r.planView.append(geo)

        # elevations = road.findall("elevationProfile/elevation")
        # for ele in elevations:
        #     att = ele.attrib
        #     e = rw.Elevation(
        #         float(att["s"]),
        #         float(att["a"]),
        #         float(att["b"]),
        #         float(att["c"]),
        #         float(att["d"])
        #     )
        #     r.elevationProfile.append(e)
        # lanes = road.find("lanes")
        # r.lanes = self.__parse_lanes(lanes)
        # framework.roads[r.id] = r
        framework.roads[r.attrib["id"]] = r

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

    
