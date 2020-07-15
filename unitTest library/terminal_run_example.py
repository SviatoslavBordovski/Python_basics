import unittest
from unittest_file import Burito

# Run Python tests with 'unittest' library in this file through any Linux terminal to execute the result with the specified bash command:
# 'python3 -m unittest test_cases.py' (it confirms usage of 3rd Python version since 2nd version is not supported from 2020)

class MyTestCase(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls): #will run always before test cases/test suites/specified methods
        print('Start the project test suite to verify the code works properly')
    
    @classmethod
    def tearDownClass(cls): #will run always after all test cases/test suites/specified methods run
        print('Good job. Finish line of project unittests!')
    
    def setUp(self): #will run the result before every method run
        print('Test started successfully')
    
    def tearDown(self): #will run the result after every method run
        print('Test passed successfully')

    def test_add(self): #quick test that shows values which would be added and what result would be calculated
        self.assertEqual(Burito.add(self, 10, 20), 30)
        self.assertEqual(Burito.add(self, 0, 0), 0)
        self.assertEqual(Burito.add(self, -1, 1), 0)

    def test_sub(self): #one more quick test to calculate an expected result
        result = Burito.sub(self, 100, 50)
        self.assertEqual(result, 50)

    def test_notSimilar(self): #check if values match or not match
        self.assertIsNot(Burito.notSimilar(self, 50, 60), 50)https://nv.ua/ukr/style/kultura/amazon-prime-video-pokazhe-dva-ukrajinski-filmi-novini-ukrajini-50094707.html
        
    def test_falseValue(self): #check if the expected value is really 'False'
        self.assertFalse(Burito.falseValue(self, 'z', 'q'), False)
