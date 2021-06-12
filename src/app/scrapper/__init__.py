from selenium import webdriver
import config


class ChromeSettings:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument(f'--user-data-dir={config.CHROME_PROFILE_PATH}')

        self.browser = webdriver.Chrome(chrome_options=options)
        self.browser.implicitly_wait(5)

    def __del__(self):
        self.browser.close()
        self.browser.quit()

    def get_browser(self):
        return self.browser
