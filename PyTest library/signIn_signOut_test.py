from selenium import webdriver
import time
import pytest
import sys # import has a strict order, this is the 1st line
import os # import has a strict order, this is the 2nd line
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..')) # import has a strict order, this is the 3rd line
from selenium.webdriver.common.keys import Keys
from lib2to3.pgen2 import driver # line of code which is resolving import errors in VS Code IDE but you can use PyCharm and see zero errors :D

@pytest.fixture()
def test_setup(): # setup and teardown for all tests
    global driver # defined webdriver globally
    driver = webdriver.Chrome(executable_path='/home/incognito/Downloads/drivers/chromedriver')
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield # using a 'yield' statement instead of 'return' statement, all code would run after a 'yield' statement as teardown
    driver.close()
    driver.quit()
    print('All tests passed!')

def test_validLoginLogout(test_setup):
    driver.get('https://opensource-demo.orangehrmlive.com/')
    driver.find_element_by_id('txtUsername').send_keys('Admin')
    driver.find_element_by_id('txtPassword').send_keys('admin123')
    driver.find_element_by_id('btnLogin').click()
    time.sleep(5)
    driver.find_element_by_id('welcome').click()
    driver.find_element_by_link_text('Logout').click()
    x = driver.title
    assert x == 'OrangeHRM' # check for 'True' title value on the page which should be read from HTML tree
    print('This test is skipped!')
    
@pytest.mark.skip(reason='test is not in scope of this sprint') # current test would be skipped, reason could be specified in brackets
def test_invalid_login_logout(test_setup):
    driver.get('https://opensource-demo.orangehrmlive.com/')
    driver.find_element_by_id('txtUsername').send_keys('admin')
    driver.find_element_by_id('txtPassword').send_keys('admin123')
    driver.find_element_by_id('btnLogin').click()
    time.sleep(5)
    driver.find_element_by_id('welcome').click()
    driver.find_element_by_link_text('Logout').click()
    time.sleep(5)
    x = driver.title
    assert x == 'OrangeHRM'
    print('Login_Logout test has been passed')
