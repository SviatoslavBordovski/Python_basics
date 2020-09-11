from selenium import webdriver
import time
import pytest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from selenium.webdriver.common.keys import Keys
from lib2to3.pgen2 import driver #This code snippet resolves importing errors in VS code IDE, but use PyCharm and see no errors :D

@pytest.fixture() #Less code == more value ^_^
def test_setup(): #setup and clean up after test finished
    global driver #Defined driver globally
    driver = webdriver.Chrome(executable_path='/home/incognito/Downloads/drivers/chromedriver')
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield #By using a 'yield' statement instead of 'return' statement, all the code after the 'yield' statement serves as the teardown code
    driver.close()
    driver.quit()
    print('Test mission accomplished!')

def test_validLoginLogout(test_setup): #simple steps and quick results
    driver.get('https://opensource-demo.orangehrmlive.com/')
    driver.find_element_by_id('txtUsername').send_keys('Admin')
    driver.find_element_by_id('txtPassword').send_keys('admin123')
    driver.find_element_by_id('btnLogin').click()
    time.sleep(3)
    driver.find_element_by_id('welcome').click()
    driver.find_element_by_link_text('Logout').click()
    x = driver.title
    assert x == 'OrangeHRM' #Check for the True value of the page title read from the HTML
    print('Mission accomplished!')
    
@pytest.mark.skip(reason='not in scope of the sprint') #this test would be skipped 
def test_invalid_login_logout(test_setup):
    driver.get('https://opensource-demo.orangehrmlive.com/')
    driver.find_element_by_id('txtUsername').send_keys('admin')
    driver.find_element_by_id('txtPassword').send_keys('admin123')
    driver.find_element_by_id('btnLogin').click()
    time.sleep(3)
    driver.find_element_by_id('welcome').click()
    driver.find_element_by_link_text('Logout').click(
    time.sleep(3)
    x = driver.title
    assert x == 'OrangeHRM'
    print('Passed Test')
