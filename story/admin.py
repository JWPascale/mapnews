from Story.models import story
from Place.models import place
from django.contrib import admin

class PlaceAdmin(admin.ModelAdmin):
    list_display = ('headline', 'pubdate')

admin.site.register(story, storyAdmin)

