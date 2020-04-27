import unittest
from unittest_file import Burito

# Run unit tests in this file through Linux terminal with the following command:
# python -m unittest testcases_for_unitests.py


class MyTestCase(unittest.TestCase):

    def test_add(self):
        result = Burito.add(self, 10, 20)
        self.assertEqual(result, 30)
