from django.core.management.base import BaseCommand

from youtube.iterables import SubscriptionsIterable
from youtube.models import Channel
import os
import requests


AUTHORIZATION_TOKEN = os.environ.get('AUTHORIZATION_TOKEN', None)


class Command(BaseCommand):
    def handle(self, *args, **options):
        channels = Channel.objects.all().filter(subscriber_count__isnull=True)
        for c in channels:
            data = {
                'part': 'statistics',
                'id': c.channel_id
            }
            url = 'https://www.googleapis.com/youtube/v3/channels'
            r = requests.get(url, data, headers={'Authorization': 'Bearer %s' % AUTHORIZATION_TOKEN})
            print(r.text)
            result_as_json = r.json()['items'][0]
            c.comment_count = result_as_json['statistics']['commentCount']
            c.subscriber_count = result_as_json['statistics']['subscriberCount']
            c.video_count = result_as_json['statistics']['videoCount']
            c.view_count = result_as_json['statistics']['viewCount']
            c.save()
