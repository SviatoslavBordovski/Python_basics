import unittest
from unittest_file import Burito

# Run unit tests in this file through Linux terminal to execute the result with the following command:
# python3 -m unittest test_cases.py

class MyTestCase(unittest.TestCase):

    def test_add(self): #Quick test that values would be added and result is calculated
        result = Burito.add(self, 10, 20)
        self.assertEqual(result, 30)
