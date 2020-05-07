import unittest
from unittest_file import Burito

# Run Python unit tests in this file through Linux terminal to execute the result with the specified command:
# 'python3 -m unittest test_cases.py' (it confirms usage of 3rd Python version since 2nd version is not supported anymore)

class MyTestCase(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls): #Will run always before test cases/test suites/specified methods
        print('Start the project test suite to verify the code works properly')
    
    @classmethod
    def tearDownClass(cls): #Will run always after all passed test cases/test suites/specified methods
        print('Good job. Finish line of the project unittests!')
    
    def setUp(self): #will run the result before every method run
        print('Test started successfully')
    
    def tearDown(self): #will run the result after every method run
        print('Test passed successfully')

    def test_add(self): #quick test that shows values which would be added and result would be calculated
        self.assertEqual(Burito.add(self, 10, 20), 30)
        self.assertEqual(Burito.add(self, 0, 0), 0)
        self.assertEqual(Burito.add(self, -1, 1), 0)

    def test_sub(self): #one more quick test to calculate the result
        result = Burito.sub(self, 100, 50)
        self.assertEqual(result, 50)

    def test_notSimilar(self): #Check values do not match
        self.assertIsNot(Burito.notSimilar(self, 50, 60), 50)
