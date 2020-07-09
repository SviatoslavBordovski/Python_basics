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
    def setUpClass(cls): #SETTINGS OF THE TEST
        cls.driver = webdriver.Chrome(executable_path='/home/incognito/Downloads/drivers/chromedriver')
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()
        
    def test_2_invalidLoginLogout(self):
        driver = self.driver
        driver.get('https://opensource-demo.orangehrmlive.com/')
        
        #Wrong password specified to check the validation work
        login = LoginPage(driver)
        login.enter_username('Admin')
        login.enter_password('admin12345')
        login.click_login()
        
        #Correct password sent
        if login.enter_password('admin12345') is not True:
            login.enter_username('Admin')
            login.enter_password('admin123')
            login.click_login()
            print('Correct credentials ¯\_(ツ)_/¯')
        
        #If none of those match prigram will report this message through HtmlTestRunner
        else:
            print('Contact support team!')
        
        #Logout steps
        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()
        
        time.sleep(3)
        print(' & Test for Login and Logout is successfully completed!')
        
    @classmethod
    def tearDownClass(cls): #Test finish
        cls.driver.close()
        cls.driver.quit()

if __name__== '__main__': #Makes separate report after every test run in the specified folder
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/home/incognito/Downloads/everything/projects/reports'))
