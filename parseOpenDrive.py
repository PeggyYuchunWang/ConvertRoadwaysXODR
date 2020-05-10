import xml.etree.ElementTree as ET
import roadways as rw
import argparse

def parseHeader(roadways, header):
    if header.attrib:
        att = header.attrib
        roadways.header = rw.Header(att["revMajor"], att["revMinor"], att["version"],
            att["date"], att["north"], att["south"], att["east"], att["west"],
            att["vendor"])
    for child in header:
        if child.tag == "userData":
            for v in child:
                if v.tag == "vectorScene":
                    att = v.attrib
                    roadways.header.geoReference.vectorScene = rw.VectorScene(att["program"], att["version"])
        elif child.tag == "geoReference":
            roadways.header.newGeoReference(child.text)

def parseLanes(lanes):
    output = rw.Lanes()
    laneOffset = lanes.findall("laneOffset")
    for lo in laneOffset:
        att = lo.attrib
        offset = rw.LaneOffset(att["s"], att["a"], att["b"], att["c"], att["d"])
        output.laneOffset.append(offset)
    laneSection = lanes.findall("laneSection")
    for ls in laneSection:
        section = rw.LaneSection(ls.attrib["s"])
        left = lanes.findall("laneSection/left/lane")
        right = lanes.findall("laneSection/right/lane")
        center = lanes.findall("laneSection/center/lane")
        for i, side in enumerate([left, right, center]):
            for l in side:
                att = l.attrib
                lane = rw.Lane(att["id"], att["type"], att["level"])
                pred = l.find("link/predecessor")
                if pred is not None:
                    lane.predecessorId = pred.attrib["id"]
                succ = l.find("link/successor")
                if succ is not None:
                    lane.successorId = succ.attrib["id"]
                width = l.find("width")
                if width is not None:
                    att = width.attrib
                    lane.width = rw.Width(att["sOffset"], att["a"], att["b"], att["c"],
                        att["d"])
                roadMark = l.find("roadMark")
                if roadMark is not None:
                    att = roadMark.attrib
                    lane.roadMark = rw.RoadMark(att["sOffset"], att["type"],
                        att["material"], att["laneChange"])
                    if "width" in att:
                        lane.roadMark.width = att["width"]
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

def parseRoad(roadways, road):
    att = road.attrib
    r = rw.Road(att["name"], att["id"], att["length"], att["junction"])
    pred = road.find("link/predecessor")
    if pred is not None:
        att = pred.attrib
        r.roadPredecessor = rw.elementType(att["elementType"], att["elementId"])
        if "contactPoint" in att:
            r.roadPredecessor.contactPoint = att["contactPoint"]
    succ = road.find("link/successor")
    if succ is not None:
        att = succ.attrib
        r.roadSuccessor = rw.elementType(att["elementType"], att["elementId"])
        if "contactPoint" in att:
            r.roadSuccessor.contactPoint = att["contactPoint"]
    type = road.find("type")
    if type is not None:
        r.type_s = type.attrib["s"]
        r.type_type = type.attrib["type"]
        for c in type:
            r.max_speed = c.attrib["max"]
            r.speed_unit = c.attrib["unit"]
    geos = road.findall("planView/geometry")
    for g in geos:
        att = g.attrib
        geo = rw.Geometry(att["s"], att["x"], att["y"], att["hdg"], att["length"])
        for c in g:
            if c.tag == "line":
                geo.type = rw.Line()
            elif c.tag == "arc":
                geo.type = rw.Arc(c.attrib["curvature"])
            else:
                print("YIKES")
        r.planView.append(geo)
    elevations = road.findall("elevationProfile/elevation")
    for ele in elevations:
        att = ele.attrib
        e = rw.Elevation(att["s"], att["a"], att["b"], att["c"], att["d"])
        r.elevationProfile.append(e)
    lanes = road.find("lanes")
    r.lanes = parseLanes(lanes)
    roadways.roads.append(r)

def parseJunction(roadways, junc):
    att = junc.attrib
    j = rw.Junction(att["id"], att["name"])
    for connection in junc:
        att = connection.attrib
        c = rw.Connection(att["id"], att["incomingRoad"], att["connectingRoad"],
            att["contactPoint"])
        ll = connection.find("laneLink")
        c.laneLink = rw.LaneLink(ll.attrib["from"], ll.attrib["to"])
        j.connections.append(c)
    roadways.junctions.append(j)

def parseOpenDrive(filename="test_data/Town02.xodr"):
    root = ET.parse(filename).getroot()
    roadways = rw.OpenDriveRoadways()
    for header in root.findall("header"):
        parseHeader(roadways, header)
    for road in root.findall("road"):
        parseRoad(roadways, road)
    for junc in root.findall("junction"):
        parseJunction(roadways, junc)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--filename', default="test_data/Town02.xodr")
    args = parser.parse_args()
    parseOpenDrive(args.filename)
