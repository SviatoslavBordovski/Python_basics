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
        
    def test_openDropdown(self):
        self.driver.get('https://www.seleniumeasy.com/test/') #Open website
        self.driver.find_element_by_class_name('dropdown').click()
        self.driver.find_element_by_xpath("//ul[@class='dropdown-menu']//a[contains(text(),'Simple Form Demo')]").click() #Click on 'Simple Form Demo' button
        time.sleep(3) #Verify loaded page
        self.driver.find_element_by_id('at-cv-lightbox-close').click()
        self.driver.find_element_by_id('user-message').send_keys('Selenium Python')
        self.driver.find_element_by_class_name('btn').click()
        time.sleep(3)
        print('Message showed')
        
    def test_ajaxFormSubmit(self):
        self.driver.get('https://www.seleniumeasy.com/test/') #Open website
        self.driver.find_element_by_class_name('dropdown').click()
        self.driver.find_element_by_xpath("//ul[@class='dropdown-menu']//a[contains(text(),'Ajax Form Submit')]").click()
        time.sleep(3)
        self.driver.find_element_by_id('title').send_keys('Sviatoslav Bordovski')
        self.driver.find_element_by_id('description').send_keys('Test form submission')
        self.driver.find_element_by_id('btn-submit').click()
        print('Form submitted')
        
    @classmethod
    def tearDownClass(cls): #Conditions that run after every test execution
        cls.driver.close()
        cls.driver.quit()

if __name__== '__main__': #Simplicity of test run in the terminal
    unittest.main()
