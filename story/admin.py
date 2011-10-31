from story.models import Story
from place.models import Places
from django.contrib import admin

class StoryAdmin(admin.ModelAdmin):
    list_display = ('headline', 'pubdate')

admin.site.register(Story, StoryAdmin)

