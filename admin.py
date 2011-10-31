from story.models import story
from place.models import place
from django.contrib import admin

class StoryAdmin(admin.ModelAdmin):
    list_display = ('headline', 'pubdate')

admin.site.register(Story, StoryAdmin)
admin.site.register(Place, PlaceAdmin)


