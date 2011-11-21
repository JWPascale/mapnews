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

def headline_list(request):
    headline_list = headline_list.objects.order_by('headline')
    return render_to_response('headline_list.html', {
        'headline_list': headline_list,
    })

def story_detail(request, story_id):
    story = Story.objects.get(id=story_id)
    return render_to_response('story_detail.html', {
        'story': story,
    })
