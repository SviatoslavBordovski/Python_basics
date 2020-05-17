import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class JustSimpleTestCase(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='/home/incognito/Downloads/drivers/chromedriver')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        
        
        
    def tearDown(self):
        self.driver.close()
        self.driver.quit()
