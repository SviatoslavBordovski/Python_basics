from ohrm.Locators.locators import Locators

#List of functions that should be invoked in tests using the class below

class CreateUser():
    def __init__(self, driver):
        self.driver = driver
        
        self.view_users_button_id = Locators.view_users_button_id
        self.add_user_button_id = Locators.add_user_button_id
        self.userRole_option_xpath_admin = Locators.userRole_option_xpath_admin
        self.employeeName_textbox_id = Locators.employeeName_textbox_id
        self.new_username_textbox_id = Locators.new_username_textbox_id
        self.userStatus_dropdown_id = Locators.userStatus_dropdown_id
        self.userStatus_option_xpath_enabled = Locators.userStatus_option_xpath_enabled
        self.new_user_password_textbox_id = Locators.new_user_password_textbox_id
        self.confirm_password_textbox_id = Locators.confirm_password_textbox_id
        self.save_newUser_button_id = Locators.save_newUser_button_id
        
    def adminSection_click(self):
        self.driver.find_element_by_id(Locators.view_users_button_id).click()
    
    def addUser_click(self):
        self.driver.find_element_by_id(Locators.add_user_button_id).click()
    
    def userRole(self):
        self.driver.find_element_by_xpath(Locators.userRole_option_xpath_admin).click()
    
    def newEmployeeName(self, user):
        self.driver.find_element_by_id(Locators.employeeName_textbox_id).clear()
        self.driver.find_element_by_id(Locators.employeeName_textbox_id).send_keys(user)
        
    def newUsername(self, employee):
        self.driver.find_element_by_id(Locators.new_username_textbox_id).clear()
        self.driver.find_element_by_id(Locators.new_username_textbox_id).send_keys(employee)
        
    def status_enabled(self):
        self.driver.find_element_by_id(Locators.userStatus_dropdown_id).click()
        self.driver.find_element_by_xpath(Locators.userStatus_option_xpath_enabled).click()
        
    def new_user_password(self, password):
        self.driver.find_element_by_id(Locators.new_user_password_textbox_id).clear()
        self.driver.find_element_by_id(Locators.new_user_password_textbox_id).send_keys(password)
   
    def new_user_confirm_password(self, new_password):
        self.driver.find_element_by_id(Locators.confirm_password_textbox_id).clear()
        self.driver.find_element_by_id(Locators.confirm_password_textbox_id).send_keys(new_password)
        
    def click_save_user(self):
        self.driver.find_element_by_id(Locators.save_newUser_button_id).click()
