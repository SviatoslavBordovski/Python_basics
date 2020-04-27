import unittest
from unittest_file import Burito

# Run unit tests in this file through Linux terminal with the following command:
# python -m unittest testcases_for_unitests.py


class MyTestCase(unittest.TestCase):

    def test_add(self): #Quick test of the values result when they are added, we expect that values would be added and result is calculated
        result = Burito.add(self, 10, 20)
        self.assertEqual(result, 30)
