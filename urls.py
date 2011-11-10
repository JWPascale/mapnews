from django.conf.urls.defaults import*
from django.contrib import admin
from django.http import Http404
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'mapnews.story.views.homepage'),
    (r'^mapnews/$', 'story.views.headlines'),
    (r'^mapnews/(?P<story_id>[-\w]+)/$', 'story.views.headlines.story_id'),
    (r'^admin/', include(admin.site.urls)),
)

def detail(request, story_id):
    try:
        p = Poll.objects.get(pk=poll_id)
    except Story.DoesNotExist:
        raise Http404
    return render_to_response('mapnews/detail.html', {'story': p})
