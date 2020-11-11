from selenium import webdriver
import time
import pytest
import sys #import has strict order, this is 1st line
import os #this is 2nd line
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..')) #this is 3rd line
from selenium.webdriver.common.keys import Keys
from lib2to3.pgen2 import driver #line of code which resolves importing errors in VS code IDE but you can use PyCharm and see no errors :D

@pytest.fixture()
def test_setup(): #setup and clean up after finished test
    global driver #defined driver globally
    driver = webdriver.Chrome(executable_path='/home/incognito/Downloads/drivers/chromedriver')
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield #using 'yield' statement instead of 'return' statement, all the code after 'yield' statement serves as the teardown
    driver.close()
    driver.quit()
    print('Test completed!')

def test_validLoginLogout(test_setup):
    driver.get('https://opensource-demo.orangehrmlive.com/')
    driver.find_element_by_id('txtUsername').send_keys('Admin')
    driver.find_element_by_id('txtPassword').send_keys('admin123')
    driver.find_element_by_id('btnLogin').click()
    time.sleep(5)
    driver.find_element_by_id('welcome').click()
    driver.find_element_by_link_text('Logout').click()
    x = driver.title
    assert x == 'OrangeHRM' #check for 'True' value of the page title which is read from the page HTML
    print('This test should be skipped ;)')
    
@pytest.mark.skip(reason='test is not in scope of the sprint') #this test would be skipped, reason could be specified in brackets
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
    print('Passed Test')
