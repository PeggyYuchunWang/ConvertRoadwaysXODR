from pyxodr.parser.open_drive_parser import OpenDriveParser

import unittest


class CurveTests(unittest.TestCase):
    def setUp(self):
        self.parser = OpenDriveParser()
        self.parser.parse_file(
            filename="test_data/OpenDriveExs/Ex_Line-Spiral-Arc.xodr",
            parse_curves=True
        )

    def tearDown(self):
        self.parser = None

    def test_line_curves(self):
        print("Running curves test - Lines")

        # Check values for road 1, first lane section and lane id of 3
        # (The only road, first line planView geometry and furthest left lane)
        key = ("1", 0, 3)
        curve_points = self.parser.curves[key].curve_points

        # Start position
        self.assertAlmostEqual(curve_points[0].pos[0], -59.22845240)
        self.assertAlmostEqual(curve_points[0].pos[1], -26.59487346)
        self.assertAlmostEqual(curve_points[0].theta, 0.331898)
        self.assertEqual(curve_points[0].k, 0.0)
        self.assertEqual(curve_points[0].kd, 0.0)

        # End position

        # Check values for road 1, first lane section and lane id of 2
        # (The only road, first line planView geometry and second left lane)
        key = ("1", 0, 2)
        curve_points = self.parser.curves[key].curve_points

        # Start position
        self.assertAlmostEqual(curve_points[0].pos[0], -57.97700374)
        self.assertAlmostEqual(curve_points[0].pos[1], -30.22522818)
        self.assertAlmostEqual(curve_points[0].theta, 0.331898)
        self.assertEqual(curve_points[0].k, 0.0)
        self.assertEqual(curve_points[0].kd, 0.0)

        # End position

        # Check values for road 1, first lane section and lane id of 1
        # (The only road, first line planView geometry and first left lane)
        key = ("1", 0, 1)
        curve_points = self.parser.curves[key].curve_points

        # Start position
        self.assertAlmostEqual(curve_points[0].pos[0], -57.12136569)
        self.assertAlmostEqual(curve_points[0].pos[1], -32.70686256)
        self.assertAlmostEqual(curve_points[0].theta, 0.331898)
        self.assertEqual(curve_points[0].k, 0.0)
        self.assertEqual(curve_points[0].kd, 0.0)

        # End position

        # Check values for road 1, first lane section and lane id of 1
        # (The only road, first line planView geometry and first left lane)
        key = ("1", 0, -1)
        curve_points = self.parser.curves[key].curve_points

        # Start position
        self.assertAlmostEqual(curve_points[0].pos[0], -54.85219128)
        self.assertAlmostEqual(curve_points[0].pos[1], -36.08206477)
        self.assertAlmostEqual(curve_points[0].theta, 0.331898)
        self.assertEqual(curve_points[0].k, 0.0)
        self.assertEqual(curve_points[0].kd, 0.0)

        # End position
