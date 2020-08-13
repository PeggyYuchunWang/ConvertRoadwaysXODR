from pyxodr.parser.open_drive_parser import OpenDriveParser

import unittest


class CurveTests(unittest.TestCase):
    def setUp(self):
        self.parser = OpenDriveParser()
        self.parser.parse_file(
            filename="test_data/OpenDriveExs/Ex_Straight-Road.xodr",
            parse_curves=True
        )

    def tearDown(self):
        self.parser = None

    def test_curves(self):
        key = ("1", 0, -1)
        curve_points = self.parser.curves[key].curve_points
        self.assertEqual(curve_points[0].pos, [0.0, 0.0])
        self.assertEqual(curve_points[1].pos, [200.0, 0.0])