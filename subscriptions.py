#!/usr/bin/env python
import os
import requests

AUTHORIZATION_TOKEN = os.environ.get('AUTHORIZATION_TOKEN', None)
url = 'https://www.googleapis.com/youtube/v3/subscriptions'

r = requests.get(url, {
    'part': 'snippet',
    'mine': True,
    'maxResults': 50
}, headers={'Authorization': 'Bearer %s' % AUTHORIZATION_TOKEN})

result = r.json()

for item in result['items']:
    print(item['snippet']['title'])


# T https://www.googleapis.com/youtube/v3/channels?part=contentDetails&mine=true
