import unittest

from src.parser.open_drive_parser import OpenDriveParser
from src.data.header import Header
from src.data.geo_reference import Geo_Reference
from src.data.offset import Offset

class ParserTests(unittest.TestCase):
    def setUp(self):
        self.parser = OpenDriveParser()
        self.parser.parse_file("test_data/OpenDriveExs/Ex_Crosswalk.xodr")

    def tearDown(self):
        self.parser = None

    def test_header(self):
        header = self.parser.data.header
        self.assertIsInstance(header, Header)
        self.assertEqual(header.attrib["revMajor"], 1)
        self.assertEqual(header.attrib["revMinor"], 6)
        self.assertEqual(header.attrib["name"], "")
        self.assertEqual(header.attrib["version"], "1.00")
        self.assertEqual(header.attrib["date"], "Wed Feb 26 17:41:13 2020")
        self.assertAlmostEqual(header.attrib["north"], 0.0)
        self.assertAlmostEqual(header.attrib["south"], 0.0)
        self.assertAlmostEqual(header.attrib['east'], 0.0)
        self.assertAlmostEqual(header.attrib["west"], 0.0)
        self.assertEqual(header.attrib["vendor"], "")
        self.assertIsNone(header.geoReference)
        self.assertIsNone(header.offset)

    def test_road(self):
        print('testing road')
        