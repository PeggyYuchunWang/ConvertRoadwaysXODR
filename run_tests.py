import unittest
from tests.parser_tests import ParserTests


def suite():
    suite = unittest.TestSuite()
    suite.addTest(ParserTests("test_header"))
    suite.addTest(ParserTests("test_road"))
    suite.addTest(ParserTests("test_lanes"))
    suite.addTest(ParserTests("test_junctions"))
    suite.addTest(ParserTests("test_objects"))
    suite.addTest(ParserTests("test_signals"))
    suite.addTest(ParserTests("test_controllers"))
    suite.addTest(ParserTests("test_station"))
    suite.addTest(ParserTests("test_junction_group"))


    return suite


runner = unittest.TextTestRunner()
runner.run(suite())
