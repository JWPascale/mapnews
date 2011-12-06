from mapnews.story.models import Story
from mapnews.place.models import Place
from django.shortcuts import render_to_response

def homepage(request):
    story = Story.objects.order_by('headline')
    place = Place.objects.order_by('place')
    return render_to_response('homepage.html', {
        'story': story,
        'place': place,
   })

def search(request):
    story = Story.objects.order_by('headline')
    place = Place.objects.order_by('place')
    return render_to_response('search.html', {
        'story': story,
        'place': place,
   })

def story_list(request):
    story = Story.objects.order_by('headline')
    return render_to_response('story_list.html', {
        'story' : story,
    })

def story_detail(request, story_id):
    story = Story.objects.get(id=story_id)
    return render_to_response('story_detail.html', {
        'story': story,
    })
