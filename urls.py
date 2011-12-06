from django.conf.urls.defaults import patterns, include,url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'mapnews.story.views.homepage'),
    url(r'^$', 'mapnews.story.views.search'),
   #url(r'^$', 'mapnews.about'),
   #url(r'^$', 'mapnews.contact'),
    url(r'^story/$', 'mapnews.story.views.story_list'),
    url(r'^place/$', 'mapnews.place.views.place_list'),
    url(r'^story/(?P<story_id>[-\w]+)/$', 'mapnews.story.views.story_detail'),    
    url(r'^place/(?P<place_id>[-\w]+)/$', 'mapnews.place.views.place_detail'), 
    url(r'^admin/', include(admin.site.urls)),
)

#how to get a search bar on homepage
#create additional URLs for places/neighborhoods/belmont or is that a query?
#RSS feed, open calisis, map?
