from tasks.provider import Provider


class Processor:
    def __init__(self):
        self.provider = Provider()

    def get_next_task(self, offset):
        return self.provider.get_next_task(offset)

    def update_status(self, status, profile):
        return self.provider.update_status(status, profile)

    def add_task(self, profile, quantity_posts):
        return self.provider.add_task(profile, quantity_posts)

    def upload_post_data(self, profile, post):
        post.update({'profile': profile})
        post_url_dict = {'url': post.get('url')}
        if self.provider.is_uploaded(post_url_dict):
            return

        self.provider.add_post_data(post)
