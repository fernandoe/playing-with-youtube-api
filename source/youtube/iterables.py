import os

import requests

AUTHORIZATION_TOKEN = os.environ.get('AUTHORIZATION_TOKEN', None)


class BaseIterable(object):
    def __init__(self, **kwargs):
        self.current_page = 0
        self.page_token = None
        self.items = []

    def __iter__(self):
        return self

    def __next__(self):
        if not self.items:
            if self.current_page == 0:
                self.page_token, self.items = self.get_items()
                self.current_page = self.current_page + 1
            elif self.page_token is not None:
                self.page_token, self.items = self.get_items(next_page_token=self.page_token)
                self.current_page = self.current_page + 1
            else:
                raise StopIteration
        return self.items.pop()


class SubscriptionsIterable(BaseIterable):
    def get_items(self, next_page_token=None):
        data = {
            'part': 'snippet',
            'mine': True,
            'maxResults': 50
        }
        if next_page_token is not None:
            data['pageToken'] = next_page_token
        url = 'https://www.googleapis.com/youtube/v3/subscriptions'
        r = requests.get(url, data, headers={'Authorization': 'Bearer %s' % AUTHORIZATION_TOKEN})
        result_as_json = r.json()
        page_token, items = result_as_json.get('nextPageToken', None), result_as_json['items']
        return page_token, items
