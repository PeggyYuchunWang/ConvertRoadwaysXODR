import unittest

from src.parser.open_drive_parser import OpenDriveParser
from src.data.header import Header
from src.data.geo_reference import Geo_Reference
from src.data.offset import Offset
from src.data.road import Road
from src.data.geometry import Geometry
from src.data.elevation import Elevation

from src.data.lanes import Lanes

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

            e = road.elevation_profile
            self.assertIsInstance(e, Elevation)
            self.assertEqual(e.attrib["s"],0)
            self.assertEqual(e.attrib["a"],0)
            self.assertEqual(e.attrib["b"],0)
            self.assertEqual(e.attrib["c"],0)
            self.assertEqual(e.attrib["d"],0)

            self.assertIsNone(road.lateral_profile["super_elevation"])
            self.assertEqual(road.lateral_profile["shapes"], [])


    def test_lanes(self):
        for key in self.parser.data.roads:
            r = self.parser.data.roads[key]
            lanes = r.lanes
            self.assertIsInstance(lanes, Lanes)

            self.assertEqual(len(lanes.lane_sections), 1)

            ls = lanes.lane_sections[0]
            self.assertEqual(ls.attrib["s"],0)
            self.assertEqual(ls.attrib["single_side"],False)

            









        