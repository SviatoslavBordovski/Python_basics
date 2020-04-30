import unittest
from unittest_file import Burito

# Run Python unit tests in this file through Linux terminal to execute the result with the specified command:
# <code>$python3 -m unittest test_cases.py</code> (it confirms usage of 3rd Python version since 2nd version is not supported anymore)

class MyTestCase(unittest.TestCase):

    def test_add(self): #quick test that shows values which would be added and result would be calculated
        result = Burito.add(self, 10, 20)
        self.assertEqual(result, 30)
