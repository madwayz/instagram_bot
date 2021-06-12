from scrapper.login.forms import LoginForm
from scrapper.index.page import IndexPage
from scrapper.login.page import LoginPage


class Profile:
    def __init__(self, browser):
        self.browser = browser

    def is_authorized(self):
        page = LoginPage(self.browser)
        return page.check_authorization()

    def has_saved_account(self):
        page = LoginPage(self.browser)
        return page.check_exist_account()

    def authorize(self, username=None, password=None, as_existing=False):
        if as_existing:
            page = LoginPage(self.browser)
            page.auth_as_exist()
            print(f'Авторизован')
        else:
            form = LoginForm(self.browser)
            form.input_username(username)
            form.input_password(password)
            form.submit_form()

            index = IndexPage(self.browser)
            index.save_data()

    def disable_notifications(self):
        form = IndexPage(self.browser)
        form.disable_notifications()

    def logout(self):
        page = IndexPage(self.browser)
        page.logout()

    def stats(self):
        pass

