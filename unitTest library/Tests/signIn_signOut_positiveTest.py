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
    def setUpClass(cls): #Set of the browser settings before it's opening
        cls.driver = webdriver.Chrome(executable_path='/home/incognito/Downloads/drivers/chromedriver')
        cls.driver.implicitly_wait(5) #Wait until the element would be visible
        cls.driver.maximize_window() #Maximize opened window to avoid responsiveness issue
        
    def test_1_validLoginLogout(self): #Test case for sing in and sign out
        driver = self.driver
        driver.get('https://opensource-demo.orangehrmlive.com/')
        
        login = LoginPage(driver)
        login.enter_username('Admin')
        login.enter_password('admin123')
        login.click_login()
        
        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()
        
        time.sleep(5)
        print('Test case for Login and Logout was successfully completed!')
        
    @classmethod
    def tearDownClass(cls): #Finish line of the test case
        cls.driver.close()
        cls.driver.quit()

if __name__== '__main__': #Generating the HTML report to the specified folder path
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/home/incognito/Downloads/everything/projects/reports'))
