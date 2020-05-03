import unittest
from unittest_file import Burito

# Run Python unit tests in this file through Linux terminal to execute the result with the specified command:
# 'python3 -m unittest test_cases.py' (it confirms usage of 3rd Python version since 2nd version is not supported anymore)

class MyTestCase(unittest.TestCase):

    def test_add(self): #quick test that shows values which would be added and result would be calculated
        self.assertEqual(Burito.add(self, 10, 20), 30)
        self.assertEqual(Burito.add(self, 0, 0), 0)
        self.assertEqual(Burito.add(self, -1, 1), 0)

    def test_sub(self):
        result = Burito.sub(self, 100, 50)
        self.assertEqual(result, 50)
