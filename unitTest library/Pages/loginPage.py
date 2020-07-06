class LoginPage():
    
    def __init__(self, driver):  #function that defines locators to be clicked
        self.driver = driver
        
        self.username_textbox_id = 'txtUsername'
        self.password_textbox_id = 'txtPassword'
        self.login_button_id = 'btnLogin'
        
    def enter_username(self, username): #function that cleans the field and types username in the field with specified id of the element
        self.driver.find_element_by_id(self.username_textbox_id).clear()
        self.driver.find_element_by_id(self.username_textbox_id).send_keys(username)
        
    def enter_password(self, password): #function that cleans the field and types password in the field with specified id of the element
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)
        
    def click_login(self): #function that clicks button with specified id
        self.driver.find_element_by_id(self.login_button_id).click()
