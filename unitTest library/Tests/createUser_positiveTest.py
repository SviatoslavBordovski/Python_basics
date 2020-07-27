from selenium import webdriver
import unittest
import HtmlTestRunner
import time
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from ohrm.Pages.loginPage import LoginPage
from ohrm.Pages.homePage import HomePage
from ohrm.Pages.createUserPage import CreateUser
#from ohrm.Tests.signIn_signOut_positiveTest import positiveSignIn <--- we need that test if want to run it before the created in this file
#from ohrm.Tests.signIn_signOut_negativeTest import negativeSignIn <--- we need that test if want to run it before the created in this file
from selenium.webdriver.common.keys import Keys

class userManagement(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='/home/incognito/Downloads/drivers/chromedriver')
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()        
        
    def test_3_createValidUser(self):
        driver = self.driver
        driver.get('https://opensource-demo.orangehrmlive.com/')
        
        #Login to the HRM system
        newUser = LoginPage(driver)
        newUser.enter_username('admin')
        newUser.enter_password('admin123')
        newUser.click_login()
        
        #Create new User
        newUser = CreateUser(driver)
        newUser.adminSection_click()
        newUser.addUser_click()
        newUser.userRole()
        newUser.newEmployeeName('Hello world')
        newUser.newUsername('Superuser26')
        newUser.status_enabled()
        newUser.new_user_password('Superuser2020!')
        newUser.new_user_confirm_password('Superuser2020!')
        newUser.click_save_user()
        
        # driver.find_element_by_id('menu_admin_viewAdminModule').click()
        # driver.find_element_by_id('btnAdd').click()
        # driver.find_element_by_id('systemUser_userType').click()
        # driver.find_element_by_xpath('//*[@id="systemUser_userType"]/option[1]').click()
        # driver.find_element_by_id('systemUser_employeeName_empName').send_keys('Hello world')
        # driver.find_element_by_id('systemUser_userName').send_keys('Superuser25')
        # driver.find_element_by_id('systemUser_status').click()
        # driver.find_element_by_xpath('//*[@id="systemUser_status"]/option[1]').click()
        # driver.find_element_by_id('systemUser_password').send_keys('Superuser2020!')
        # driver.find_element_by_id('systemUser_confirmPassword').send_keys('Superuser2020!')
        # driver.find_element_by_id('btnSave').click()
        time.sleep(5)
        
        confirmationLink = 'https://opensource-demo.orangehrmlive.com/index.php/admin/viewSystemUsers'
        
        if driver.current_url == confirmationLink:
            print(confirmationLink + ' / New user was created successfully!')
        else:
            #return error('User not created')
            self.fail('Refactor me')
        
        #Logout from the HRM system
        newUser = HomePage(driver)
        newUser.click_welcome()
        newUser.click_logout()
        
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__== '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/home/incognito/Downloads/everything/projects/reports'))
