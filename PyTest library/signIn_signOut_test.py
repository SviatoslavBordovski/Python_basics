from selenium import webdriver
import time
import pytest
import sys #import has strict order, this is the 1st line
import os #import has strict order, this is the 2nd line
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..')) #import has strict order, this is the 3rd line
from selenium.webdriver.common.keys import Keys
from lib2to3.pgen2 import driver #line of code which  is resolving import errors in VS Code IDE but you can use PyCharm and see no errors :D

@pytest.fixture()
def test_setup(): #setup and clean up
    global driver #defined driver globally
    driver = webdriver.Chrome(executable_path='/home/incognito/Downloads/drivers/chromedriver')
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield #using a 'yield' statement instead of a 'return' statement, all code would run after the 'yield' statement as teardown
    driver.close()
    driver.quit()
    print('All tests were finished!')

def test_validLoginLogout(test_setup):
    driver.get('https://opensource-demo.orangehrmlive.com/')
    driver.find_element_by_id('txtUsername').send_keys('Admin')
    driver.find_element_by_id('txtPassword').send_keys('admin123')
    driver.find_element_by_id('btnLogin').click()
    time.sleep(3)
    driver.find_element_by_id('welcome').click()
    driver.find_element_by_link_text('Logout').click()
    x = driver.title
    assert x == 'OrangeHRM' #check for 'True' value of the page title which is read from the HTML
    print('This test should be skipped!')
    
@pytest.mark.skip(reason='test is not in scope of the sprint') #test would be skipped, reason could be specified in the brackets
def test_invalid_login_logout(test_setup):
    driver.get('https://opensource-demo.orangehrmlive.com/')
    driver.find_element_by_id('txtUsername').send_keys('admin')
    driver.find_element_by_id('txtPassword').send_keys('admin123')
    driver.find_element_by_id('btnLogin').click()
    time.sleep(3)
    driver.find_element_by_id('welcome').click()
    driver.find_element_by_link_text('Logout').click()
    time.sleep(3)
    x = driver.title
    assert x == 'OrangeHRM'
    print('Passed Test')
