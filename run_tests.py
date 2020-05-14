import unittest
from tests.parser_tests import ParserTests


def suite():
    suite = unittest.TestSuite()
    suite.addTest(ParserTests("test_header"))

    return suite


runner = unittest.TextTestRunner()
runner.run(suite())
