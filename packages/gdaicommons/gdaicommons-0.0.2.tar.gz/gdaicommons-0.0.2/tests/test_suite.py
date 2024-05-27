import unittest

from tests.text_classification import TextClassificationTest

test_suite = unittest.TestSuite()
test_suite.addTest(unittest.makeSuite(TextClassificationTest))

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(test_suite)
