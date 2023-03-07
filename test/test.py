import unittest

from client_test import TestGetDataPoint, TestGetRatio

if __name__ == '__main__':
    unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(TestGetDataPoint())
    suite.addTest(TestGetRatio())
    runner = unittest.TextTestRunner()
    runner.run(suite)
