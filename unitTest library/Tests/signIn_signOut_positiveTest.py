from selenium import webdriver
import unittest
import HtmlTestRunner
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
import time
from Pages.loginPage import LoginPage
from Pages.homePage import HomePage
from selenium.webdriver.common.keys import Keys

class signInTests(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls): #Chosen browser settings before it's launch
        cls.driver = webdriver.Chrome(executable_path='/home/incognito/Downloads/drivers/chromedriver')
        cls.driver.implicitly_wait(8) #Wait until searching element would be visible for driver
        cls.driver.maximize_window() #Maximize browser window to avoid any issues related to website responsiveness/locator search
        
    def test_1_validLoginLogout(self): #Test case for sing in and sign out to HRM system
        driver = self.driver
        driver.get('https://opensource-demo.orangehrmlive.com/')
        
        login = LoginPage(driver)
        login.enter_username('Admin')
        login.enter_password('admin123')
        login.click_login()
        
        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()
        
        time.sleep(10)
        print('Test case for Login and Logout was successfully completed!')
        
    @classmethod
    def tearDownClass(cls): #Test case finish
        cls.driver.close()
        cls.driver.quit()

if __name__== '__main__': #Generating HTML report to specified folder path
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/home/incognito/Downloads/everything/projects/reports'))
