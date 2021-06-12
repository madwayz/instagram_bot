import selenium.common.exceptions

from base.xpath_entities import IndexPageXpaths


class IndexPage:
    def __init__(self, browser):
        self.browser = browser

    def logout(self):
        self.header_profile_menu()
        self.browser.find_element_by_xpath(IndexPageXpaths.button_logout).click()

    def disable_notifications(self):
        try:
            self.browser.find_element_by_xpath(IndexPageXpaths.button_disable_notifications).click()
        except selenium.common.exceptions.NoSuchElementException:
            pass

    def save_data(self):
        self.browser.find_element_by_xpath(IndexPageXpaths.button_save_data).click()

    def header_profile_menu(self):
        self.browser.find_element_by_xpath(IndexPageXpaths.menu_header_profile).click()

