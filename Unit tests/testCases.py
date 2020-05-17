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
       
    def test_search(self):
        self.driver.get('http://www.google.com') #Open website
        self.driver.find_element_by_name('q').send_keys('Python documentation') #Type search keys
        self.driver.find_element_by_name('btnK').click() #Click on 'Google search' button
        self.driver.find_element_by_class_name('LC20lb').click() #Navigate to the selected link
        time.sleep(3) #Verify loaded page
        print('Python documentation detected!') #Execute test case result in the terminal
        
    def tearDown(self):
        self.driver.close()
        self.driver.quit()
