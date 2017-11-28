from django.core.management.base import BaseCommand

from youtube.iterables import SubscriptionsIterable
from youtube.models import Channel


class Command(BaseCommand):
    def handle(self, *args, **options):
        Channel.objects.all().delete()
        iterable = SubscriptionsIterable()
        for i in iterable:
            Channel.objects.create(
                channel_id=i['snippet']['resourceId']['channelId'],
                title=i['snippet']['title'],
                published_at=i['snippet']['publishedAt'],
                thumbnails_default=i['snippet']['thumbnails']['default']['url'],
                thumbnails_medium=i['snippet']['thumbnails']['medium']['url'],
                thumbnails_high=i['snippet']['thumbnails']['high']['url'],
            )
