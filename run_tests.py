import unittest
from tests.parser_tests import ParserTests


def suite():
    suite = unittest.TestSuite()
    suite.addTest(ParserTests("test_header"))
    #suite.addTest(ParserTests("test_geo_reference"))
    #suite.addTest(ParserTests("test_offset"))
    #suite.addTest(ParserTests("test_road"))

    return suite


runner = unittest.TextTestRunner()
runner.run(suite())
