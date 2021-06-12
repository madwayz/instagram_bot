from base.statuses import Status
from profile.model import Profile
from scrapper.profile.page import ProfilePage
from base.exceptions import ProfileIsPrivate
import traceback


class Worker:
    def __init__(self, browser):
        self.browser = browser
        self.profile = None
        self.quantity_posts = None
        self.task = None

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.browser.close()
        self.browser.quite()

    def add_task(self, task):
        self.task = task

    def run(self):
        try:
            profile_page = ProfilePage(self.browser, self.task.profile)

            if not profile_page.is_subscribed():
                profile_page.subscribe()

            if profile_page.is_private():
                raise ProfileIsPrivate('Не могу обработать закрытый профиль')

            profile_page.handle_posts(quantity=self.task.quantity_posts)
            posts = profile_page.get_posts()

            self.task.upload_post_data(posts)
            return Status.COMPLETED
        except Exception:
            traceback.print_exc()
            return Status.ERROR
