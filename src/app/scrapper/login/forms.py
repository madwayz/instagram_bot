from base.xpath_entities import LoginFormXpaths


class LoginForm:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get('https://instagram.com/accounts/login/')

    def input_username(self, username):
        input_username = self.browser.find_element_by_xpath(LoginFormXpaths.input_username)
        input_username.send_keys(username)

    def input_password(self, password):
        input_password = self.browser.find_element_by_xpath(LoginFormXpaths.input_password)
        input_password.send_keys(password)

    def submit_form(self):
        self.browser.find_element_by_xpath(LoginFormXpaths.button_submit).click()