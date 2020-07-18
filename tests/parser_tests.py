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
from src.data.junction_predecessor_successor import Junction_Predecessor_Successor
from src.data.junction_group import Junction_Group
from src.data.junction_controller import Junction_Controller

class ParserTests(unittest.TestCase):
    def setUp(self):
        self.parser = OpenDriveParser()
        self.parser.parse_file("test_data/OpenDriveExs/Ex_Crosswalk.xodr")

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
            self.assertIsNone(c.connections.predecessor)
            self.assertIsNone(c.connections.successor)

            self.assertEqual(len(c.lane_links), 3)
            ll = c.lane_links[0]
            self.assertEqual(ll.attrib["from_id"], 1)
            self.assertEqual(ll.attrib["to_id"], -1)

            self.assertEqual(len(j.controllers), 4)
            c = j.controllers[0]
            self.assertEqual(ll.attrib["id"], "2")
            self.assertEqual(ll.attrib["type"], "0")



            






            









        