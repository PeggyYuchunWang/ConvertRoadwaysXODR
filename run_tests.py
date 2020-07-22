import unittest
from tests.parser_tests import ParserTests


def suite():
    suite = unittest.TestSuite()
    suite.addTest(ParserTests("test_header"))
    #suite.addTest(ParserTests("test_geo_reference"))
    #suite.addTest(ParserTests("test_offset"))
    suite.addTest(ParserTests("test_road"))
    suite.addTest(ParserTests("test_lanes"))
    suite.addTest(ParserTests("test_junctions"))
    suite.addTest(ParserTests("test_objects"))
    suite.addTest(ParserTests("test_signals"))
    suite.addTest(ParserTests("test_controllers"))


    return suite


runner = unittest.TextTestRunner()
runner.run(suite())
