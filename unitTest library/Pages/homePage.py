class HomePage():
    
    def __init__(self,driver): #function that defines locators to be clicked
        self.driver = driver
        
        self.welcome_link_id = 'welcome'
        self.logout_link_linkText = 'Logout'
        
    def click_welcome(self): #function that makes click for the button with a specified id
        self.driver.find_element_by_id(self.welcome_link_id).click()
        
    def click_logout(self): #function that makes click for the button with a specified link text
        self.driver.find_element_by_link_text(self.logout_link_linkText).click()
