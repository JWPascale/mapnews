from story.models import Story, Section, Byline
from place.models import Places
from django.contrib import admin

class StoryAdmin(admin.ModelAdmin):
    list_display = ('headline', 'pubdate')

admin.site.register(Story, StoryAdmin)
admin.site.register(Section)
admin.site.register(Byline)
