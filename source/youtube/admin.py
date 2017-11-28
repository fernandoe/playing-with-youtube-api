from django.contrib import admin

from .models import Channel


@admin.register(Channel)
class ChannelModelAdmin(admin.ModelAdmin):
    list_display = ('get_uuid', 'title', 'channel_id', 'subscriber_count', 'video_count', 'view_count', 'published_at',
                    'get_youtube_url')
    ordering = ('title',)

    def get_youtube_url(self, obj):
        return '<a href="https://www.youtube.com/channel/%s">youtube</a>' % obj.channel_id
    get_youtube_url.allow_tags = True
