import unittest

from src.parser.open_drive_parser import OpenDriveParser
from src.data.header import Header

class ParserTests(unittest.TestCase):
    def setUp(self):
        self.parser = OpenDriveParser()
        self.parser.parse_file("test_data/OpenDriveExs/Ex_Crosswalk.xodr")

    def tearDown(self):
        self.parser = None

    def test_header(self):
        header = self.parser.data.header
        self.assertIsInstance(header, Header)
        self.assertEqual(header.revMajor, 1)
        self.assertEqual(header.revMinor, 6)
        self.assertEqual(header.name, "")
        self.assertEqual(header.version, "1.00")
        self.assertEqual(header.date, "Wed Feb 26 17:41:13 2020")
        self.assertAlmostEqual(header.north, 0.0)
        self.assertAlmostEqual(header.south, 0.0)
        self.assertAlmostEqual(header.east, 0.0)
        self.assertAlmostEqual(header.west, 0.0)
        self.assertEqual(header.vendor, "")
        