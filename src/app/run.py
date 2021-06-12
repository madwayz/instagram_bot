from config import USERNAME, PASSWORD
from profile.model import Profile
from scrapper.index.page import IndexPage
from scrapper import ChromeSettings
from tasks.runner import task_runner

if __name__ == '__main__':
    settings = ChromeSettings()
    browser = settings.get_browser()

    profile = Profile(browser)

    if not profile.is_authorized():
        if profile.has_saved_account():
            profile.authorize(as_existing=True)
        else:
            profile.authorize(USERNAME, PASSWORD)

    index = IndexPage(browser)
    index.disable_notifications()

    task_runner(browser)
    # profile.logout()