import xml.etree.ElementTree as ET
import src.open_drive_roadways as rw

class OpenDriveParser:
    def __init__(self):
        self.data = rw.OpenDriveRoadways()

    def __parse_header(self, roadways, header):
        if header.attrib:
            att = header.attrib
            roadways.header = rw.Header(
                int(att["revMajor"]),
                int(att["revMinor"]),
                att["version"],
                att["date"],
                float(att["north"]),
                float(att["south"]),
                float(att["east"]),
                float(att["west"]),
                att["vendor"]
            )
        for child in header:
            if child.tag == "userData":
                for v in child:
                    if v.tag == "vectorScene":
                        att = v.attrib
                        roadways.header.geoReference.vectorScene = rw.VectorScene(
                            att["program"], att["version"])
            elif child.tag == "geoReference":
                roadways.header.newGeoReference(child.text)

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
            section = rw.LaneSection(float(ls.attrib["s"]))
            left = lanes.findall("laneSection/left/lane")
            right = lanes.findall("laneSection/right/lane")
            center = lanes.findall("laneSection/center/lane")
            for i, side in enumerate([left, right, center]):
                for l in side:
                    att = l.attrib
                    lane = rw.Lane(
                        int(att["id"]),
                        att["type"],
                        bool(att["level"])
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
                            att["material"],
                            att["laneChange"]
                        )
                        if "width" in att:
                            lane.roadMark.width = float(att["width"])
                    vl = l.find("userData/vectorLane")
                    if vl is not None:
                        lane.travelDir = vl.attrib["travelDir"]
                    if i == 0:
                        section.left.append(lane)
                    elif i == 1:
                        section.right.append(lane)
                    elif i == 2:
                        section.center.append(lane)
            output.laneSection.append(section)
        return output

    def __parse_road(self, roadways, road):
        att = road.attrib
        r = rw.Road(
            att["name"],
            int(att["id"]),
            float(att["length"]),
            int(att["junction"])
        )
        pred = road.find("link/predecessor")
        if pred is not None:
            att = pred.attrib
            r.roadPredecessor = rw.elementType(
                att["elementType"], int(att["elementId"]))
            if "contactPoint" in att:
                r.roadPredecessor.contactPoint = att["contactPoint"]
        succ = road.find("link/successor")
        if succ is not None:
            att = succ.attrib
            r.roadSuccessor = rw.elementType(
                att["elementType"], int(att["elementId"]))
            if "contactPoint" in att:
                r.roadSuccessor.contactPoint = att["contactPoint"]
        type = road.find("type")
        if type is not None:
            r.type_s = float(type.attrib["s"])
            r.type_type = type.attrib["type"]
            for c in type:
                r.max_speed = float(c.attrib["max"])
                r.speed_unit = c.attrib["unit"]
        geos = road.findall("planView/geometry")
        for g in geos:
            att = g.attrib
            geo = rw.Geometry(
                float(att["s"]),
                float(att["x"]),
                float(att["y"]),
                float(att["hdg"]),
                float(att["length"])
            )
            for c in g:
                if c.tag == "line":
                    geo.type = rw.Line()
                elif c.tag == "arc":
                    geo.type = rw.Arc(float(c.attrib["curvature"]))
                else:
                    print("YIKES")
            r.planView.append(geo)
        elevations = road.findall("elevationProfile/elevation")
        for ele in elevations:
            att = ele.attrib
            e = rw.Elevation(
                float(att["s"]),
                float(att["a"]),
                float(att["b"]),
                float(att["c"]),
                float(att["d"])
            )
            r.elevationProfile.append(e)
        lanes = road.find("lanes")
        r.lanes = self.__parse_lanes(lanes)
        roadways.roads[r.id] = r

    def __parseJunction(self, roadways, junc):
        att = junc.attrib
        j = rw.Junction(att["id"], att["name"])
        for connection in junc:
            att = connection.attrib
            c = rw.Connection(
                att["id"], att["incomingRoad"], att["connectingRoad"],
                att["contactPoint"])
            ll = connection.find("laneLink")
            c.laneLink = rw.LaneLink(ll.attrib["from"], ll.attrib["to"])
            j.connections.append(c)
        roadways.junctions[j.id] = j

    def parse_file(self, filename="test_data/Town02.xodr"):
        root = ET.parse(filename).getroot()
        for header in root.findall("header"):
            self.__parse_header(self.data, header)
        for road in root.findall("road"):
            self.__parse_road(self.data, road)
        for junc in root.findall("junction"):
            self.__parseJunction(self.data, junc)
        print("done parse")
