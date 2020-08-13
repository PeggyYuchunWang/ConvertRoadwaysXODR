from tests.parser_tests import ParserTests
from tests.curve_tests import CurveTests

import unittest


def suite():
    suite = unittest.TestSuite()

    # Run parser related tests
    suite.addTest(ParserTests("test_header"))
    suite.addTest(ParserTests("test_road"))
    suite.addTest(ParserTests("test_lanes"))
    suite.addTest(ParserTests("test_objects"))
    suite.addTest(ParserTests("test_signals"))
    suite.addTest(ParserTests("test_junctions"))
    # suite.addTest(ParserTests("test_controllers"))
    # suite.addTest(ParserTests("test_station"))
    # suite.addTest(ParserTests("test_junction_group"))

    # Run curve related tests
    suite.addTest(CurveTests("test_curves"))


    return suite


runner = unittest.TextTestRunner()
runner.run(suite())
