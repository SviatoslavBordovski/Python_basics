from ohrm.Locators.locators import Locators

class HomePage():
    
    def __init__(self,driver): #function that defines locators to be clicked
        self.driver = driver
        
        self.welcome_link_id = Locators.welcome_link_id
        self.logout_link_linkText = Locators.logout_link_linkText
        
    def click_welcome(self): #function that makes click on the button with a specified id
        self.driver.find_element_by_id(Locators.welcome_link_id).click()
        
    def click_logout(self): #function that makes click on the button with a specified link text
        self.driver.find_element_by_link_text(Locators.logout_link_linkText).click()
