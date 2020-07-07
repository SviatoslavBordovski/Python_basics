from selenium import webdriver
import unittest
import HtmlTestRunner
import time
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from ohrm.Pages.loginPage import LoginPage
from ohrm.Pages.homePage import HomePage
from selenium.webdriver.common.keys import Keys

class signInTests(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='/home/incognito/Downloads/drivers/chromedriver')
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()
        
    def test_1_validLoginLogout(self):
        driver = self.driver
        driver.get('https://opensource-demo.orangehrmlive.com/')
        
        login = LoginPage(driver)
        login.enter_username('Admin')
        login.enter_password('admin123')
        login.click_login()
        
        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()
        
        #self.driver.find_element_by_id('txtUsername').send_keys('Admin')
        #self.driver.find_element_by_id('txtPassword').send_keys('admin123')
        #self.driver.find_element_by_id('btnLogin').click()
        #time.sleep(3)
        #self.driver.find_element_by_id('welcome').click()
        #self.driver.find_element_by_link_text('Logout').click()
        time.sleep(3)
        print('Test for Login and Logout is successfully completed!')
        
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__== '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/home/incognito/Downloads/everything/projects/reports'))
