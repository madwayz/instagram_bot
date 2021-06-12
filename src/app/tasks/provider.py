from base.provider import BaseProvider


class Provider(BaseProvider):
    def __init__(self):
        super().__init__('tasks')

    def update_status(self, status, profile):
        return self.exec_by_file('update_status.sql', {
            'status': status,
            'profile': profile,
        })

    def add_task(self, profile, quantity_posts):
        return self.exec_by_file('insert.sql', {'profile': profile, 'quantity_posts': quantity_posts})[0].get('id')

    def get_next_task(self, offset):
        response = self.exec_by_file('get_next.sql', {'offset': offset})
        return response[0] if any(response) else None

    def add_post_data(self, post_data):
        return self.exec_by_file('add_post_data.sql', post_data)

    def is_uploaded(self, post_data):
        return bool(self.exec_by_file('is_uploaded.sql', post_data)[0].get('id'))
