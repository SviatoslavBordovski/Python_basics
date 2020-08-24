from selenium import webdriver
import time
import sys
import os
import pytest
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from selenium.webdriver.common.keys import Keys
from lib2to3.pgen2 import driver #snippet that resolves the errors in vs code

@pytest.fixture()
def test_setup():
    global driver
    driver = webdriver.Chrome(executable_path='/home/incognito/Downloads/drivers/chromedriver')
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield
    driver.close()
    driver.quit()
    print('Mission accomplished')

def test_validLoginLogout(test_setup):
    driver.get('https://opensource-demo.orangehrmlive.com/')
    driver.find_element_by_id('txtUsername').send_keys('Admin')
    driver.find_element_by_id('txtPassword').send_keys('admin123')
    driver.find_element_by_id('btnLogin').click()
    time.sleep(3)
    driver.find_element_by_id('welcome').click()
    driver.find_element_by_link_text('Logout').click()
    time.sleep(3)
    x = driver.title
    assert x == 'OrangeHRM'
    print('Passed Test')
