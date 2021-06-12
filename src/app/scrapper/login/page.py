from base.xpath_entities import LoginFormXpaths
from selenium.common.exceptions import NoSuchElementException


class LoginPage:
    def __init__(self, browser):
        self.browser = browser

    def check_authorization(self):
        self.browser.get('https://instagram.com/accounts/login/')
        return not ('not-logged-in' in self.browser.page_source)

    def check_exist_account(self):
        self.browser.get('https://instagram.com/')

        try:
            self.browser.find_element_by_xpath(LoginFormXpaths.button_has_account)
            return True
        except NoSuchElementException:
            return False

    def auth_as_exist(self):
        self.browser.get('https://instagram.com/')
        button = self.browser.find_element_by_xpath(LoginFormXpaths.button_has_account)
        if button:
            button.click()
