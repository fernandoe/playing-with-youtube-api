import json

from django.core.management.base import BaseCommand

from youtube.iterables import SubscriptionsIterable


class Command(BaseCommand):
    def handle(self, *args, **options):
        iterable = SubscriptionsIterable()
        for i in iterable:
            # print(i['snippet']['title'])
            print(json.dumps(i['snippet']))
