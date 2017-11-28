from django.db import models
from fe_core.base_models import UUIDModel


class Channel(UUIDModel):
    channel_id = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    published_at = models.DateTimeField()
    thumbnails_default = models.URLField()
    thumbnails_medium = models.URLField()
    thumbnails_high = models.URLField()

    comment_count = models.IntegerField(null=True)
    subscriber_count = models.IntegerField(null=True)
    video_count = models.IntegerField(null=True)
    view_count = models.IntegerField(null=True)

    def __str__(self):
        return self.title
