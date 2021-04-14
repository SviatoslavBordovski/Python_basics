class Locators():
    
    #Login page
    username_textbox_id = 'txtUsername'
    password_textbox_id = 'txtPassword'
    login_button_id = 'btnLogin'
    
    #Home page
    welcome_link_id = 'welcome'
    logout_link_linkText = 'Logout'
    
    #Adding new user
    view_users_button_id = 'menu_admin_viewAdminModule'
    add_user_button_id = 'btnAdd'
    userRole_dropdown_id = 'systemUser_userType'
    userRole_option_xpath_admin = '//*[@id="systemUser_userType"]/option[1]'
    employeeName_textbox_id = 'systemUser_employeeName_empName'
    new_username_textbox_id = 'systemUser_userName'
    userStatus_dropdown_id = 'systemUser_status'
    userStatus_option_xpath_enabled = '//*[@id="systemUser_status"]/option[1]'
    new_user_password_textbox_id = 'systemUser_password'
    confirm_password_textbox_id = 'systemUser_confirmPassword'
    save_newUser_button_id = 'btnSave'
