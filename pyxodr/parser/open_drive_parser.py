import xml.etree.ElementTree as ET
import pyxodr.utils as utils
import pyxodr.data.open_drive_framework as odf

from pyxodr.data.header import Header
from pyxodr.data.geo_reference import Geo_Reference
from pyxodr.data.offset import Offset

from pyxodr.data.road import Road
from pyxodr.data.road_predecessor_successor import Road_Predecessor_Successor
from pyxodr.data.road_neighbor import Road_Neighbor
from pyxodr.data.road_type import Road_Type
from pyxodr.data.road_speed import Road_Speed

from pyxodr.data.geometry import Geometry
from pyxodr.data.spiral import Spiral
from pyxodr.data.arc import Arc
from pyxodr.data.poly3 import Poly3
from pyxodr.data.param_poly3 import Param_Poly3
from pyxodr.data.elevation import Elevation

from pyxodr.data.lateral_profile import Lateral_Profile
from pyxodr.data.lateral_profile_superelevation import Lateral_Profile_Superelevation
from pyxodr.data.lateral_profile_shape import Lateral_Profile_Shape

from pyxodr.data.lanes import Lanes
from pyxodr.data.lane_offset import Lane_Offset
from pyxodr.data.lane_section import Lane_Section
from pyxodr.data.lane import Lane
from pyxodr.data.lane_width import Lane_Width
from pyxodr.data.lane_height import Lane_Height
from pyxodr.data.lane_border import Lane_Border
from pyxodr.data.lane_material import Lane_Material
from pyxodr.data.lane_visibility import Lane_Visibility
from pyxodr.data.lane_access import Lane_Access
from pyxodr.data.lane_rule import Lane_Rule
from pyxodr.data.lane_speed import Lane_Speed

from pyxodr.data.road_mark import Road_Mark
from pyxodr.data.road_mark_type import Road_Mark_Type
from pyxodr.data.road_mark_line import Road_Mark_Line
from pyxodr.data.road_mark_sway import Road_Mark_Sway
from pyxodr.data.road_mark_explicit import Road_Mark_Explicit
from pyxodr.data.road_mark_explicit_line import Road_Mark_Explicit_Line

from pyxodr.data.junction import Junction
from pyxodr.data.junction_connection import Junction_Connection
from pyxodr.data.junction_lane_link import Junction_Lane_Link
from pyxodr.data.junction_priority import Junction_Priority
from pyxodr.data.junction_predecessor_successor import Junction_Predecessor_Successor
from pyxodr.data.junction_group import Junction_Group
from pyxodr.data.junction_controller import Junction_Controller

from pyxodr.data.objects import Objects
from pyxodr.data.object import Object
from pyxodr.data.object_repeat import Object_Repeat
from pyxodr.data.object_outline import Object_Outline
from pyxodr.data.object_outline_corner_road import Object_Outline_Corner_Road
from pyxodr.data.object_outline_corner_local import Object_Outline_Corner_Local
from pyxodr.data.object_material import Object_Material
from pyxodr.data.object_validity import Object_Validity
from pyxodr.data.object_parking_space import Object_Parking_Space
from pyxodr.data.object_marking import Object_Marking
from pyxodr.data.object_border import Object_Border
from pyxodr.data.object_reference import Object_Reference
from pyxodr.data.object_tunnel import Object_Tunnel
from pyxodr.data.object_bridge import Object_Bridge

from pyxodr.data.signal import Signal
from pyxodr.data.signal_validity import Signal_Validity
from pyxodr.data.signal_dependency import Signal_Dependency
from pyxodr.data.signal_reference import Signal_Reference
from pyxodr.data.signal_position_inertial import Signal_Position_Inertial
from pyxodr.data.signal_position_road import Signal_Position_Road
from pyxodr.data.signal_repeat import Signal_Repeat

from pyxodr.data.controller import Controller
from pyxodr.data.controller_signal_control import Controller_Signal_Control

from pyxodr.data.railroad import Railroad
from pyxodr.data.railroad_switch import Railroad_Switch
from pyxodr.data.railroad_track import Railroad_Track
from pyxodr.data.railroad_switch_partner import Railroad_Switch_Partner

from pyxodr.data.station import Station
from pyxodr.data.station_platform import Station_Platform
from pyxodr.data.station_platform_segment import Station_Platform_Segment


class OpenDriveParser:
    """
    Parser for OpenDrive that will store all content in the PyXODR data object.

    Attributes
    ----------
    data : Open_Drive_Framework
        The data container for the contents from an OpenDrive XML.
    """
    def __init__(self):
        self.data = odf.Open_Drive_Framework()
        self.parse_curves = False
        self.curves = {}  # dict with keys (road_id, lane_section_id, lane_id)

    def parse_file(self, filename="test_data/carlaExs/Town02.xodr",
                   parse_curves=False):
        """
        Parses an xml file, written using the OpenDrive standard, and stores
        its contents in the parser's data object.

        Parameters
        ----------
        filename : str, optional
            The filename to parse. Accepts absolute path or relative path where
            code was called.
        """
        print("parsing: ", filename)
        root = ET.parse(filename).getroot()
        self.parse_curves = parse_curves
        self.__parse(xml_root=root)
        print("done parsing: ", filename)

    def __parse(self, xml_root):
        for header in xml_root.findall("header"):
            self.__parse_header(self.data, header)

        for road in xml_root.findall("road"):
            self.__parse_road(self.data, road)

        for junc in xml_root.findall("junction"):
            self.__parse_junction(self.data, junc)

        for junc_group in xml_root.findall("junctionGroup"):
            self.__parse_junction_group(self.data, junc_group)

        for cont in xml_root.findall("controller"):
            self.__parse_controller(self.data, cont)

        for stat in xml_root.findall("station"):
            self.__parse_station(self.data, stat)

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
                # I think that in ver1.6 User Data is not found in this way
                continue
                # for v in child:
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

        self.__parse_road_predecessor_and_successor(
            r,
            road.find("link/predecessor"),
            road.find("link/successor")
        )

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
                    print("Unknown type child tag: ", child.tag)

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

        if road.find("objects") is not None:
            r.objects = self.__parse_objects(road.find("objects"))

        if road.find("signals") is not None:
            r.signals = self.__parse_signals(road.find("signals"))

        if road.find("railroad") is not None:
            r.railroad = self.__parse_railroad(road.find("railroad"))

        if self.parse_curves:
            self.__parse_curves(r)

        framework.roads[r.attrib["id"]] = r

    def __parse_curves(self, road):
        for geo in road.plan_view:
            lane_sections = road.lanes.lane_sections
            for ls in lane_sections:
                if ls.attrib["s"] < geo.attrib["s"] + geo.attrib["length"]:
                    # found a lane_section for which current Geometry element
                    # is applicable
                    for i, side in enumerate([ls.left_lanes, ls.right_lanes]):  # [ls.center_lane]]):
                        # step through each lane
                        for lane in side:
                            key, curve = utils.createCurve(
                                road,
                                lane_sections.index(ls),
                                lane,
                                geo)
                            if key is not None:
                                self.curves[key] = curve

    def __parse_road_predecessor_and_successor(self, r, pred, succ):
        if pred is not None:
            att = pred.attrib
            r.predecessor = Road_Predecessor_Successor(
                att["elementType"],
                int(att["elementId"])
            )
            if "contactPoint" in att:
                r.predecessor.attrib["contact_point"] = att["contactPoint"]
            if "elementS" in att:
                r.predecessor.attrib["element_s"] = float(att["elementS"])
            if "elementDir" in att:
                r.predecessor.attrib["element_dir"] = att["elementDir"]

        if succ is not None:
            att = succ.attrib
            r.successor = Road_Predecessor_Successor(
                att["elementId"],
                att["elementType"]
            )
            if "contactPoint" in att:
                r.successor.attrib["contact_point"] = att["contactPoint"]
            if "elementS" in att:
                r.successor.attrib["element_s"] = float(att["elementS"])
            if "elementDir" in att:
                r.successor.attrib["element_dir"] = att["elementDir"]

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
                    # if parse_curves:
                    #     curve = utils.createCurveSpiral(r, geo)
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
                    geo.type = Param_Poly3(
                        att["pRange"],
                        float(att["aU"]),
                        float(att["bU"]),
                        float(att["cU"]),
                        float(att["dU"]),
                        float(att["aV"]),
                        float(att["bV"]),
                        float(att["cV"]),
                        float(att["dV"])
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
                section.attrib["single_side"] = utils.convertStringToBool(
                    att["singleSide"]
                )

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
                        lane.attrib["level"] = utils.convertStringToBool(
                            att["level"]
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
                        lane.border = Lane_Border(
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
                            lane.road_mark.attrib["roughness"] = float(
                                att["roughness"]
                            )

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
                        lane.height = Lane_Height(
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
                att["type"]
            )
            if "color" in att:
                lane.road_mark.attrib["color"] = att["color"]
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
                    print("Unknown road mark child tag: ", child.tag)

    def __parse_objects(self, objects):
        objs = Objects()
        for obj in objects.findall("object"):
            att = obj.attrib
            o = Object(
                att["type"],
                att["id"],
                float(att["s"]),
                float(att["t"])
            )
            if "zOffset" in att:
                o.attrib["z_offset"] = float(att["zOffset"])
            if "validLength" in att:
                o.attrib["valid_length"] = float(att["validLength"])
            if "orientation" in att:
                o.attrib["orientation"] = att["orientation"]
            if "subtype" in att:
                o.attrib["subtype"] = att["subtype"]
            if "dynamic" in att:
                o.attrib["dynamic"] = att["dynamic"]
            if "hdg" in att:
                o.attrib["hdg"] = float(att["hdg"])
            if "name" in att:
                o.attrib["name"] = att["name"]
            if "pitch" in att:
                o.attrib["pitch"] = float(att["pitch"])
            if "roll" in att:
                o.attrib["roll"] = float(att["roll"])
            if "height" in att:
                o.attrib["height"] = float(att["height"])
            if "length" in att:
                o.attrib["length"] = float(att["length"])
            if "width" in att:
                o.attrib["width"] = float(att["width"])
            if "radius" in att:
                o.attrib["radius"] = float(att["radius"])

            if obj.findall("repeat") is not None:
                self.__parse_object_repeats(o, obj.findall("repeat"))

            if obj.find("outlines") is not None:
                self.__parse_object_outlines(o, obj.find("outlines"))

            material = obj.find("material")
            if material is not None:
                att = material.attrib
                o.material = Object_Material(
                    att["surface"]
                )
                if "friction" in att:
                    obj.material.attrib["friction"] = float(att["friction"])
                if "roughness" in att:
                    obj.material.attrib["roughness"] = float(att["roughness"])

            for validity in obj.findall("validity"):
                att = validity.attrib
                o.validity = Object_Validity(
                    att["fromLane"],
                    att["toLane"]
                )

            parking_space = obj.find("parkingSpace")
            if parking_space is not None:
                att = parking_space.attrib
                o.parking_space = Object_Parking_Space(
                    att["access"]
                )
                if "restrictions" in att:
                    o.parking_space.attrib["restrictions"] = att[
                        "restrictions"
                    ]

            if obj.find("markings") is not None:
                self.__parse_object_markings(o, obj.find("markings"))

            for borders in obj.findall("borders"):
                for border in borders:
                    att = border.attrib
                    b = Object_Border(
                        float(att["width"]),
                        att["type"],
                        str(att["outlineId"])
                    )
                    if "useCompleteOutline" in att:
                        b.attrib["useCompleteOutline"] = bool(
                            att["useCompleteOutline"]
                        )
                    o.borders.append(b)

            objs.objects.append(o)

            if objects.findall("objectReference") is not None:
                self.__parse_object_references(
                    objs,
                    objects.findall("objectReference")
                )

            if objects.findall("tunnel") is not None:
                self.__parse_object_tunnels(objs, objects.findall("tunnel"))

            if objects.findall("bridge") is not None:
                self.__parse_object_bridges(objs, objects.findall("bridge"))

        return objs

    def __parse_object_repeats(self, o, repeats):
        for repeat in repeats:
            att = repeat.attrib
            r = Object_Repeat(
                float(att["s"]),
                float(att["length"]),
                float(att["distance"])
            )
            if "tStart" in att:
                r.attrib["t_start"] = float(att["tStart"])
            if "tEnd" in att:
                r.attrib["t_end"] = float(att["tEnd"])
            if "heightStart" in att:
                r.attrib["height_start"] = float(att["heightStart"])
            if "heightEnd" in att:
                r.attrib["height_end"] = float(att["heightEnd"])
            if "zOffsetStart" in att:
                r.attrib["z_offset_start"] = float(att["zOffsetStart"])
            if "zOffsetEnd" in att:
                r.attrib["z_offset_end"] = float(att["zOffsetEnd"])
            if "widthStart" in att:
                r.attrib["width_start"] = float(att["widthStart"])
            if "widthEnd" in att:
                r.attrib["width_end"] = float(att["widthEnd"])
            if "lengthStart" in att:
                r.attrib["length_start"] = float(att["lengthStart"])
            if "lengthEnd" in att:
                r.attrib["length_end"] = float(att["lengthEnd"])
            if "radiusStart" in att:
                r.attrib["radius_start"] = float(att["radiusStart"])
            if "radiusEnd" in att:
                r.attrib["radius_end"] = float(att["radiusEnd"])
            o.repeats.append(r)

    def __parse_object_outlines(self, o, outlines):
        for outline in outlines:
            att = outline.attrib
            ol = Object_Outline(att["id"])
            if "fillType" in att:
                ol.attrib["fill_type"] = att["fillType"]
            if "outer" in att:
                ol.attrib["outer"] = att["outer"]
            if "closed" in att:
                ol.attrib["closed"] = att["closed"]
            if "laneType" in att:
                ol.attrib["lane_type"] = att["laneType"]

            for corner_road in outline.findall("cornerRoad"):
                att = corner_road.attrib
                cr = Object_Outline_Corner_Road()
                if "id" in att:
                    cr.attrib["id"] = att["id"]
                if "s" in att:
                    cr.attrib["s"] = float(att["s"])
                if "t" in att:
                    cr.attrib["t"] = float(att["t"])
                if "dz" in att:
                    cr.attrib["dz"] = float(att["dz"])
                if "height" in att:
                    cr.attrib["height"] = float(att["height"])
                ol.corner_roads.append(cr)

            for corner_local in outline.findall("cornerLocal"):
                att = corner_local.attrib
                cl = Object_Outline_Corner_Local()
                if "id" in att:
                    cl.attrib["id"] = att["id"]
                if "u" in att:
                    cl.attrib["height"] = float(att["u"])
                if "v" in att:
                    cl.attrib["v"] = float(att["v"])
                if "z" in att:
                    cl.attrib["z"] = float(att["z"])
                if "height" in att:
                    cl.attrib["height"] = float(att["height"])
                ol.corner_locals.append(cl)

            o.outlines.append(ol)

    def __parse_object_markings(self, o, markings):
        for mark in markings:
            att = mark.attrib
            m = Object_Marking()
            if "side" in att:
                m.attrib["side"] = att["side"]
            if "weight" in att:
                m.attrib["weight"] = att["weight"]
            if "width" in att:
                m.attrib["width"] = float(att["width"])
            if "color" in att:
                m.attrib["color"] = att["color"]
            if "zOffset" in att:
                m.attrib["z_offset"] = float(att["zOffset"])
            if "spaceLength" in att:
                m.attrib["space_length"] = float(att["spaceLength"])
            if "lineLength" in att:
                m.attrib["line_length"] = float(att["lineLength"])
            if "startOffset" in att:
                m.attrib["start_offset"] = float(att["startOffset"])
            if "stopOffset" in att:
                m.attrib["stop_offset"] = float(att["stopOffset"])

            for corner_reference in mark:
                att = corner_reference.attrib
                m.corner_references.append(att["id"])

            o.markings.append(m)

    def __parse_object_references(self, objs, obj_references):
        for ref in obj_references:
            att = ref.attrib
            r = Object_Reference(
                float(att["s"]),
                float(att["t"]),
                att["id"]
            )
            if "zOffset" in att:
                r.attrib["z_offset"] = float(att["zOffset"])
            if "validLength" in att:
                r.attrib["valid_length"] = float(att["validLength"])
            if "orientation" in att:
                r.attrib["orientation"] = att["orientation"]

            objs.references.append(r)

    def __parse_object_tunnels(self, objs, tunnels):
        for tunnel in tunnels:
            att = tunnel.attrib
            t = Object_Tunnel(
                float(att["s"]),
                float(att["length"]),
                att["id"]
            )
            if "type" in att:
                t.attrib["type"] = att["type"]
            if "name" in att:
                t.attrib["name"] = att["name"]
            if "lighting" in att:
                t.attrib["lighting"] = int(att["lighting"])
            if "daylight" in att:
                t.attrib["daylight"] = int(att["daylight"])

            objs.tunnels.append(t)

    def __parse_object_bridges(self, objs, bridges):
        for bridge in bridges:
            att = bridge.attrib
            b = Object_Bridge(
                float(att["s"]),
                float(att["length"]),
                att["id"]
            )
            if "type" in att:
                b.attrib["type"] = att["type"]
            if "name" in att:
                b.attrib["name"] = att["name"]

            objs.bridges.append(b)

    def __parse_signals(self, signals):
        sgnls = {}
        for signal in signals:
            att = signal.attrib
            s = Signal(
                att["id"],
                float(att["s"]),
                float(att["t"])
            )
            if "name" in att:
                s.attrib["name"] = att["name"]
            if "zOffset" in att:
                s.attrib["z_offset"] = float(att["zOffset"])
            if "dynamic" in att:
                s.attrib["dynamic"] = att["dynamic"]
            if "orientation" in att:
                s.attrib["orientation"] = att["orientation"]
            if "country" in att:
                s.attrib["country"] = att["country"]
            if "countryRevision" in att:
                s.attrib["country_revision"] = att["countryRevision"]
            if "validLength" in att:
                s.attrib["valid_length"] = float(att["validLength"])
            if "type" in att:
                s.attrib["type"] = att["type"]
            if "subtype" in att:
                s.attrib["subtype"] = att["subtype"]
            if "value" in att:
                s.attrib["value"] = float(att["value"])
            if "unit" in att:
                s.attrib["unit"] = att["unit"]
            if "height" in att:
                s.attrib["height"] = float(att["height"])
            if "width" in att:
                s.attrib["width"] = float(att["width"])
            if "text" in att:
                s.attrib["text"] = att["text"]
            if "hOffset" in att:
                s.attrib["h_offset"] = float(att["hOffset"])
            if "pitch" in att:
                s.attrib["pitch"] = float(att["pitch"])
            if "roll" in att:
                s.attrib["roll"] = float(att["roll"])

            for validity in signal.findall("validity"):
                att = validity.attrib
                v = Signal_Validity(
                    att["fromLane"],
                    att["toLane"]
                )
                s.validity_records.append(v)

            for dependency in signal.findall("dependency"):
                att = dependency.attrib
                d = Signal_Dependency(att["id"])
                if "type" in att:
                    d.attrib["type"] = att["type"]
                s.dependency_records.append(d)

            for reference in signal.findall("reference"):
                att = reference.attrib
                r = Signal_Reference(
                    att["elementType"]
                )
                if "elementID" in att:
                    r.attrib["element_id"] = att["elementID"]
                if "type" in att:
                    r.attrib["type"] = float(att["type"])
                s.references.append(r)

            position = signal.find("positionInertial")
            if position is not None:
                att = position.attrib
                s.position_inertial = Signal_Position_Inertial(
                    float(att["x"]),
                    float(att["y"]),
                    float(att["z"])
                )
                if "hdg" in att:
                    s.position_inertial.attrib["hdg"] = float(att["hdg"])
                if "pitch" in att:
                    s.position_inertial.attrib["pitch"] = float(att["pitch"])
                if "roll" in att:
                    s.position_inertial.attrib["roll"] = float(att["roll"])
            else:
                position = signal.find("positionRoad")
                if position is not None:
                    att = position.attrib
                    s.position_road = Signal_Position_Road(
                        att["road_id"],
                        float(att["s"]),
                        float(att["t"])
                    )
                    if "z_offset" in att:
                        s.position_road.attrib["z_offset"] = float(
                            att["z_offset"]
                        )
                    if "h_offset" in att:
                        s.position_road.attrib["h_offset"] = float(
                            att["h_offset"]
                        )
                    if "pitch" in att:
                        s.position_road.attrib["pitch"] = float(att["pitch"])
                    if "roll" in att:
                        s.position_road.attrib["roll"] = float(att["roll"])

            for repeat in signal.findall("signalReference"):
                att = repeat.attrib
                r = Signal_Repeat(
                    float(att["s"]),
                    float(att["t"]),
                    att["id"]
                )
                if "orientation" in att:
                    r.attrib["orientation"] = float(att["orientation"])
                s.repeats.append(r)

            sgnls[s.attrib["id"]] = s

        return sgnls

    def __parse_railroad(self, railroad):
        att = railroad.attrib
        r = Railroad()
        for switch in railroad.findall("switch"):
            att = switch.attrib
            s = Railroad_Switch(
                att["name"],
                att["id"]
            )
            if "position" in att:
                s.attrib["position"] = att["position"]

            mainTrack = switch.find("mainTrack")
            att = mainTrack.attrib
            s.main_track = Railroad_Track(
                att["id"],
                float(att["s"]),
                att["dir"]
            )

            sideTrack = switch.find("sideTrack")
            att = sideTrack.attrib
            s.side_track = Railroad_Track(
                att["id"],
                float(att["s"]),
                att["dir"]
            )

            partnerSwitch = switch.find("partner")
            if partnerSwitch is not None:
                att = partnerSwitch.attrib
                s.switch_partner = Railroad_Switch_Partner(
                    att["name"],
                    att["id"]
                )

            r.switches[s.attrib["id"]] = s

        return r

    def __parse_junction(self, framework, junc):
        att = junc.attrib
        j = Junction(
            att["id"]
        )
        if "name" in att:
            j.attrib["name"] = att["name"]
        if "type" in att:
            j.attrib["type"] = att["type"]

        connections = junc.findall("connection")
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

    def __parse_junction_group(self, framework, junc_group):
        att = junc_group.attrib
        junction_group = Junction_Group(att["id"])
        if "name" in att:
            junction_group.attrib["name"] = att["name"]
        if "type" in att:
            junction_group.attrib["type"] = att["type"]

        for ref in junc_group.findall("junctionReference"):
            att = ref.attrib
            junction_group.junction_references.append(att["junction"])

        framework.junction_groups[junction_group.attrib["id"]] = junction_group

    def __parse_controller(self, framework, cont):
        att = cont.attrib
        controller = Controller(att["id"])
        if "name" in att:
            controller.attrib["name"] = att["name"]
        if "sequence" in att:
            controller.attrib["sequence"] = att["sequence"]

        for c in cont.findall("control"):
            att = c.attrib
            sc = Controller_Signal_Control(att["signalId"])
            if "type" in att:
                sc.attrib["type"] = att["type"]
            controller.signal_control_records.append(sc)

        framework.controllers[controller.attrib["id"]] = controller

    def __parse_station(self, framework, stat):
        att = stat.attrib
        station = Station(att["id"])
        if "name" in att:
            station.attrib["name"] = att["name"]
        if "type" in att:
            station.attrib["type"] = att["type"]

        for plat in stat.findall("platform"):
            att = plat.attrib
            p = Station_Platform(att["id"])
            if "name" in att:
                p.attrib["name"] = att["name"]

            for seg in plat.findall("segment"):
                att = seg.attrib
                s = Station_Platform_Segment(
                    att["roadId"],
                    float(att["sStart"]),
                    float(att["sEnd"]),
                    att["side"]
                )
                p.segments.append(s)

            station.platforms.append(p)

        framework.stations[station.attrib["id"]] = station
