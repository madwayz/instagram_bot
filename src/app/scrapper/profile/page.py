import selenium.common.exceptions

from base.xpath_entities import ProfilePageXpaths


class ProfilePage:
    def __init__(self, browser, profile):
        self.browser = browser
        self.profile = profile

        self.browser.get(self.instagram_url)
        self.posts = []

    @property
    def instagram_url(self):
        return f'https://www.instagram.com/{self.profile}'
    
    def is_private(self):
        try:
            self.browser.find_element_by_xpath(ProfilePageXpaths.visibility_profile)
            return True
        except selenium.common.exceptions.NoSuchElementException:
            return False

    def is_subscribed(self):
        try:
            self.browser.find_element_by_xpath(ProfilePageXpaths.button_send_message)
            return True
        except selenium.common.exceptions.NoSuchElementException:
            return False

    def is_liked(self):
        text = 'Не нравится'
        button = self.browser.find_element_by_xpath(ProfilePageXpaths.post_like_status)
        return text == button.get_attribute('aria-label')

    def subscribe(self):
        try:
            self.browser.find_element_by_xpath(ProfilePageXpaths.button_subscribe).click()
        except selenium.common.exceptions.InvalidSelectorException:
            pass

    def like_post(self):
        self.browser.find_element_by_xpath(ProfilePageXpaths.button_post_like).click()

    def get_post_time(self):
        return self.browser.find_element_by_xpath(ProfilePageXpaths.post_time).get_attribute('datetime')

    def get_post_url(self, index):
        href = self.browser.find_element_by_xpath(ProfilePageXpaths.post_url_template.format(index))
        return href.get_attribute('href')

    def get_likes(self):
        likes = self.browser.find_element_by_xpath(ProfilePageXpaths.post_likes_counter).text
        return int(likes.replace(' ', ''))

    def open_post(self, index):
        self.browser.find_element_by_xpath(ProfilePageXpaths.post_template.format(index)).click()

    def close_post(self):
        self.browser.find_element_by_xpath(ProfilePageXpaths.button_close_post).click()

    def handle_posts(self, quantity):
        for i in range(1, quantity + 1):
            self.open_post(i)

            url = self.get_post_url(i)
            post_time = self.get_post_time()
            likes = self.get_likes()

            if not self.is_liked():
                self.like_post()
            else:
                print(f'Пост {url} уже лайкнут. Пропускаю.')

            self.close_post()

            self.posts.append({
                'url': url,
                'post_time': post_time,
                'likes': likes
            })

    def get_posts(self):
        return self.posts
