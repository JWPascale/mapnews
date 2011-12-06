from mapnews.place.models import Place
from mapnews.story.models import Story
from django.shortcuts import render_to_response

def place(request):
    place = Place.objects.order_by('place')
    return render_to_response('homepage.html', {
        'place': place,
    })

def place_list(request):
    place_list= Place.objects.order_by('name')
    return render_to_response('place_list.html', {
        'place_list': place_list,
    })

def place_detail(request, place_id):
    hood = Place.objects.get(id=place_id)
    stories = Story.objects.filter(location = place_id)
    return render_to_response('place_detail.html', {
        'hood' : hood,
        'stories' : stories,
    })
