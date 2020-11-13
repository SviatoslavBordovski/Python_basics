from ohrm.Locators.locators import Locators

class LoginPage():
    
    def __init__(self, driver): #function that defines locators to be clicked
        self.driver = driver
        
        self.username_textbox_id = Locators.username_textbox_id
        self.password_textbox_id = Locators.password_textbox_id
        self.login_button_id = Locators.login_button_id
        
    def enter_username(self, username): #function that cleans the field and types username in the field with specified id of the element
        self.driver.find_element_by_id(Locators.username_textbox_id).clear()
        self.driver.find_element_by_id(Locators.username_textbox_id).send_keys(username)
        
    def enter_password(self, password): #function that cleans the field and types password in the field with specified id of the element
        self.driver.find_element_by_id(Locators.password_textbox_id).clear()
        self.driver.find_element_by_id(Locators.password_textbox_id).send_keys(password)
        
    def click_login(self): #function that clicks on the button with specified id
        self.driver.find_element_by_id(Locators.login_button_id).click()
