import unittest

from src.parser.open_drive_parser import OpenDriveParser

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

from src.data.road_mark import Road_Mark
from src.data.road_mark_type import Road_Mark_Type
from src.data.road_mark_line import Road_Mark_Line

from src.data.junction import Junction
from src.data.junction_connection import Junction_Connection
from src.data.junction_lane_link import Junction_Lane_Link
from src.data.junction_priority import Junction_Priority
from src.data.junction_predecessor_successor import Junction_Predecessor_Successor
from src.data.junction_controller import Junction_Controller

from src.data.junction_group import Junction_Group

from src.data.objects import Objects
from src.data.object import Object
from src.data.object_repeat import Object_Repeat
from src.data.object_outline import Object_Outline
from src.data.object_outline_corner_road import Object_Outline_Corner_Road
from src.data.object_outline_corner_local import Object_Outline_Corner_Local
from src.data.object_material import Object_Material
from src.data.object_validity import Object_Validity
from src.data.object_parking_space import Object_Parking_Space
from src.data.object_marking import Object_Marking
from src.data.object_border import Object_Border
from src.data.object_reference import Object_Reference
from src.data.object_tunnel import Object_Tunnel
from src.data.object_bridge import Object_Bridge

from src.data.signal import Signal
from src.data.signal_validity import Signal_Validity
from src.data.signal_dependency import Signal_Dependency
from src.data.signal_reference import Signal_Reference
from src.data.signal_position_inertial import Signal_Position_Inertial
from src.data.signal_position_road import Signal_Position_Road
from src.data.signal_repeat import Signal_Repeat

from src.data.controller import Controller
from src.data.controller_signal_control import Controller_Signal_Control

from src.data.railroad import Railroad
from src.data.railroad_switch import Railroad_Switch
from src.data.railroad_track import Railroad_Track
from src.data.railroad_switch_partner import Railroad_Switch_Partner

from src.data.station import Station
from src.data.station_platform import Station_Platform
from src.data.station_platform_segment import Station_Platform_Segment


class ParserTests(unittest.TestCase):
    def setUp(self):
        self.parser = OpenDriveParser()
        self.parser.parse_file("test_data/OpenDriveExs/Ex_Compilation.xodr")

    def tearDown(self):
        self.parser = None

    def test_header(self):
        header = self.parser.data.header
        self.assertIsInstance(header, Header)
        self.assertEqual(header.attrib["rev_major"], 1)
        self.assertEqual(header.attrib["rev_minor"], 6)
        self.assertEqual(header.attrib["name"], "")
        self.assertEqual(header.attrib["version"], "1.00")
        self.assertEqual(header.attrib["date"], "Wed Feb 26 17:41:13 2020")
        self.assertAlmostEqual(header.attrib["north"], 0.0)
        self.assertAlmostEqual(header.attrib["south"], 0.0)
        self.assertAlmostEqual(header.attrib['east'], 0.0)
        self.assertAlmostEqual(header.attrib["west"], 0.0)
        self.assertEqual(header.attrib["vendor"], "")
        self.assertIsNone(header.geo_reference)
        self.assertIsNone(header.offset)

    def test_road(self):
        for key in self.parser.data.roads:
            road = self.parser.data.roads[key]
            self.assertIsInstance(road, Road)
            self.assertEqual(road.attrib["name"], "")
            self.assertEqual(road.attrib["length"], 5.0000000000000000e+01)
            self.assertEqual(road.attrib["id"], "1")
            self.assertEqual(road.attrib["junction"], "-1")
            self.assertEqual(road.attrib["rule"], "RHT")
            self.assertIsNone(road.type)
            self.assertIsNone(road.predecessor)
            self.assertIsNone(road.successor)
            
            g = road.plan_view[0]
            self.assertIsInstance(g, Geometry)
            self.assertEqual(g.attrib["s"], 0)
            self.assertEqual(g.attrib["x"], 0)
            self.assertEqual(g.attrib["y"], 0)
            self.assertEqual(g.attrib["hdg"], 1.5707963267948966e+00)
            self.assertEqual(g.attrib["length"], 5.0000000000000000e+01)
            self.assertIsNone(g.type)

            e = road.elevation_profile[0]
            self.assertIsInstance(e, Elevation)
            self.assertEqual(e.attrib["s"],0)
            self.assertEqual(e.attrib["a"],0)
            self.assertEqual(e.attrib["b"],0)
            self.assertEqual(e.attrib["c"],0)
            self.assertEqual(e.attrib["d"],0)

            self.assertIsNone(road.lateral_profile.super_elevation)
            self.assertEqual(len(road.lateral_profile.shapes), 0)

    def test_lanes(self):
        for key in self.parser.data.roads:
            r = self.parser.data.roads[key]
            lanes = r.lanes
            self.assertIsInstance(lanes, Lanes)

            self.assertEqual(len(lanes.lane_sections), 1)

            ls = lanes.lane_sections[0]
            self.assertEqual(ls.attrib["s"],0)
            self.assertEqual(ls.attrib["single_side"],False)

            lls = ls.left_lanes
            self.assertEqual(len(lls),7)
            ll = lls[0]
            self.assertEqual(ll.attrib["id"],7)
            self.assertEqual(ll.attrib["type"],"sidewalk")
            self.assertEqual(ll.attrib["level"],False)

            self.assertIsInstance(ll.width, Lane_Width)
            self.assertEqual(ll.width.attrib["s_offset"],0)
            self.assertEqual(ll.width.attrib["a"],3.0000000000000000e+00)
            self.assertEqual(ll.width.attrib["b"],0)
            self.assertEqual(ll.width.attrib["c"],0)
            self.assertEqual(ll.width.attrib["d"],0)

            self.assertIsInstance(ll.height, Lane_Height)
            self.assertEqual(ll.height.attrib["s_offset"],0)
            self.assertEqual(ll.height.attrib["inner"],1.2000000000000000e-01)
            self.assertEqual(ll.height.attrib["outer"],1.2000000000000000e-01)

            self.assertIsNone(ll.predecessor_id)
            self.assertIsNone(ll.successor_id)
            self.assertIsNone(ll.border)
            self.assertIsNone(ll.road_mark)
            self.assertIsNone(ll.material)
            self.assertIsNone(ll.visibility)
            self.assertIsNone(ll.speed)
            self.assertIsNone(ll.access)
            self.assertIsNone(ll.rule)

            ll = lls[6]
            self.assertEqual(ll.attrib["id"],1)
            self.assertEqual(ll.attrib["type"],"driving")
            self.assertEqual(ll.attrib["level"],False)

            self.assertIsInstance(ll.width, Lane_Width)
            self.assertEqual(ll.width.attrib["s_offset"],0)
            self.assertEqual(ll.width.attrib["a"],3.2500000000000000e+00)
            self.assertEqual(ll.width.attrib["b"],0)
            self.assertEqual(ll.width.attrib["c"],0)
            self.assertEqual(ll.width.attrib["d"],0)

            self.assertIsNone(ll.predecessor_id)
            self.assertIsNone(ll.successor_id)
            self.assertIsNone(ll.height)
            self.assertIsNone(ll.border)
            self.assertIsNone(ll.road_mark)
            self.assertIsNone(ll.material)
            self.assertIsNone(ll.visibility)
            self.assertIsNone(ll.speed)
            self.assertIsNone(ll.access)
            self.assertIsNone(ll.rule)

    def test_junctions(self):
        for key in self.parser.data.junctions:
            j = self.parser.data.junctions[key]
            self.assertIsInstance(j, Junction)
            self.assertEqual(j.attrib["name"], "")
            self.assertEqual(j.attrib["id"], "1")
            self.assertEqual(j.attrib["type"], "default")
            
            self.assertEqual(len(j.connections),1)
            c = j.connections[0]
            self.assertEqual(c.attrib["id"], "0")
            self.assertEqual(c.attrib["incoming_road"], "6")
            self.assertEqual(c.attrib["connecting_road"], "2")
            self.assertEqual(c.attrib["contact_point"], "start")
            self.assertIsNone(c.predecessor)
            self.assertIsNone(c.successor)

            self.assertEqual(len(c.lane_links), 3)
            ll = c.lane_links[0]
            self.assertEqual(ll.attrib["from_id"], 1)
            self.assertEqual(ll.attrib["to_id"], -1)

            self.assertEqual(len(j.controllers), 4)
            c = j.controllers[0]
            self.assertEqual(c.attrib["id"], "2")
            self.assertEqual(c.attrib["type"], "0")

    def test_objects(self):
        objs = self.parser.data.roads["1"].objects
        o = objs.objects[0]
        self.assertIsInstance(o, Object)
        self.assertEqual(o.attrib["type"], "crosswalk")
        self.assertEqual(o.attrib["id"], "10")
        self.assertEqual(o.attrib["s"], 10.0)
        self.assertEqual(o.attrib["t"], 0.0)
        self.assertEqual(o.attrib["z_offset"], 0.0)
        self.assertEqual(o.attrib["orientation"], "none")
        self.assertEqual(o.attrib["length"], 10.0)
        self.assertEqual(o.attrib["width"], 7.0)
        self.assertEqual(o.attrib["hdg"], 0.0)
        self.assertEqual(o.attrib["pitch"], 0.0)
        self.assertEqual(o.attrib["roll"], 0.0)
        self.assertEqual(o.attrib["name"], "")
        self.assertEqual(o.attrib["height"], 0.0)
        self.assertEqual(o.attrib["radius"], 0.0)
        self.assertEqual(o.attrib["subtype"], "")

        outline = o.outlines[0]
        self.assertIsInstance(outline, Object_Outline)
        self.assertEqual(outline.attrib["id"], "0")
        cr = outline.corner_roads[0]
        self.assertIsInstance(cr, Object_Outline_Corner_Road)
        self.assertEqual(cr.attrib["s"], 5.0)
        self.assertEqual(cr.attrib["t"], 3.5)
        self.assertEqual(cr.attrib["dz"], 0.0)
        self.assertEqual(cr.attrib["height"], 0.0)
        self.assertEqual(cr.attrib["id"], "0")

        marking = o.markings[0]
        self.assertIsInstance(marking, Object_Marking)
        self.assertEqual(marking.attrib["width"], 0.1)
        self.assertEqual(marking.attrib["color"], "white")
        self.assertEqual(marking.attrib["z_offset"], 0.005)
        self.assertEqual(marking.attrib["space_length"], 0.05)
        self.assertEqual(marking.attrib["line_length"], 0.2)
        self.assertEqual(marking.attrib["start_offset"], 0.0)
        self.assertEqual(marking.attrib["stop_offset"], 0.0)
        cr_id = marking.corner_references[0]
        self.assertEqual(cr_id, "0")

    def test_signals(self):
        sgnls = self.parser.data.roads["1"].signals
        s = sgnls["1"]
        self.assertIsInstance(s, Signal)
        self.assertEqual(s.attrib["s"], 1.0000000000000000e+01)
        self.assertEqual(s.attrib["t"], -0.0000000000000000e+00)
        self.assertEqual(s.attrib["id"], "1")
        self.assertEqual(s.attrib["name"], "Crosswalk")
        self.assertEqual(s.attrib["dynamic"], "no")
        self.assertEqual(s.attrib["orientation"], "none")
        self.assertEqual(s.attrib["z_offset"], 0.0000000000000000e+00)
        self.assertEqual(s.attrib["type"], "1000003")
        self.assertEqual(s.attrib["country"], "OpenDRIVE")
        self.assertEqual(s.attrib["country_revision"], "2013")
        self.assertEqual(s.attrib["subtype"], "-1")
        self.assertEqual(s.attrib["value"], 4.0000000000000000e+00)
        self.assertEqual(s.attrib["unit"], "m")
        self.assertEqual(s.attrib["h_offset"], 0)
        self.assertEqual(s.attrib["pitch"], 0)
        self.assertEqual(s.attrib["roll"], 0)
        self.assertEqual(s.attrib["height"], 0.01)
        self.assertEqual(s.attrib["width"], 10.40)

    def test_controllers(self):
        controllers = self.parser.data.controllers
        c = controllers["1"]
        self.assertIsInstance(c, Controller)
        self.assertEqual(c.attrib["id"], "1")
        self.assertEqual(c.attrib["name"], "ctrl001")
        sc = c.signal_control_records[0]
        self.assertIsInstance(sc, Controller_Signal_Control)
        self.assertEqual(sc.attrib["signal_id"], "8")
        self.assertEqual(sc.attrib["type"], "0")

    def test_railroad(self):
        r = self.parser.data.roads["1"].railroad
        self.assertIsInstance(r, Railroad)

        s = r.switches["32"]
        self.assertIsInstance(s, Railroad_Switch)
        self.assertEqual(s.attrib["position"], "dynamic")
        self.assertEqual(s.attrib["id"], "1")
        self.assertEqual(s.attrib["name"], "Switch32")


        mt = r.main_track
        self.assertIsInstance(mt, Railroad_Track)
        self.assertEqual(mt.attrib["id"], "3")
        self.assertEqual(mt.attrib["s"], 1.0000000000000000e+01)
        self.assertEqual(mt.attrib["dir"], "+")

        st = r.side_track
        self.assertIsInstance(st, Railroad_Track)
        self.assertEqual(mt.attrib["id"], "2")
        self.assertEqual(mt.attrib["s"], 3.4898261533109149e+01)
        self.assertEqual(mt.attrib["dir"], "-")

        ps = r.switch_parter
        self.assertIsInstance(ps, Railroad_Switch_Partner)
        self.assertEqual(mt.attrib["name"], "Switch12")
        self.assertEqual(mt.attrib["id"], "12")

    def test_station(self):
        s = self.parser.data.stations["12"]
        self.assertIsInstance(s, Station)
        self.assertEqual(s.attrib["id"], "12")
        self.assertEqual(s.attrib["name"], "H12")
        self.assertEqual(s.attrib["type"], "small")

        p = s.platforms[0]
        self.assertIsInstance(p, Station_Platform)
        self.assertEqual(p.attrib["id"], "12-1")
        self.assertEqual(p.attrib["name"], "platform1")

        seg = p.segments[0]
        self.assertIsInstance(seg, Station_Platform_Segment)
        self.assertEqual(seg.attrib["road_id"], "2")
        self.assertEqual(seg.attrib["s_start"], 1.6500000000000000e+01)
        self.assertEqual(seg.attrib["s_end"], 5.1000000000000000e+01)
        self.assertEqual(seg.attrib["side"], "right")

    def test_junction_group(self):
        jg = self.parser.data.junction_groups["1"]
        self.assertIsInstance(jg, Junction_Group)
        self.assertEqual(jg.attrib["id"], "1")
        self.assertEqual(jg.attrib["name"], "ExampleRoundabout")
        self.assertEqual(jg.attrib["type"], "roundabout")

        r = jg.junction_references[0]
        self.assertIsInstance(r, str)
        self.assertEqual(r, "42")



       

        

        



            







            






            









        