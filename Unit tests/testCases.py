import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

class JustSimpleTestCase(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls): #Preconditions that would run for each test case
        cls.driver = webdriver.Chrome(executable_path='/home/incognito/Downloads/drivers/chromedriver') #Path to the driver
        cls.driver.implicitly_wait(10) #Wait until element becomes visible for interaction
        cls.driver.maximize_window() #Make browser window opened fully
       
    def test_openWebsite(self):
        self.driver.get('https://bordovski.pp.ua')
        time.sleep(5)
        print('Personal blog detected')
        
    @classmethod
    def tearDownClass(cls): #Conditions that run after every test execution
        cls.driver.close()
        cls.driver.quit()

if __name__== '__main__': #Simplicity of test run in the terminal
    unittest.main()
