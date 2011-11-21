from django.conf.urls.defaults import patterns, include,url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'mapnews.story.views.homepage'),
    url(r'^story/$', 'mapnews.story.views.headline_list'),
    url(r'^place/$', 'mapnews.place.views.place_list'),
    url(r'^story/(?P<story_id>[-\w]+)/$', 'mapnews.story.views.story_detail'),    
    url(r'^place/(?P<place_id>[-\w]+)/$', 'mapnews.place.views.place_detail'), 
    url(r'^admin/', include(admin.site.urls)),
)

#newsnearyou.com/Lincoln/homepage.html
#newsnearyou.com/Lincoln/search_results.html
#newsnearyou.com/Lincoln/stories.html
#newsnearyou.com/Lincoln/places.html
#newsnearyou.com/Lincoln/places/place_list/neighborhoods.html
#newsnearyou.com/Lincoln/places/place_list/neighborhoods/story_list.html
#newsnearyou.com/Lincoln/places.html




#how to get a search bar and map on homepage
#create additional URLs for places/neighborhoods/belmont or is that a query?
#RSS feed, open calisis, map?
