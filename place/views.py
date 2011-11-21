from mapnews.place.models import Place
from mapnews.story.models import Story
from django.shortcuts import render_to_response

def place(request):
    place = Place.objects.order_by('place')
    return render_to_response('homepage.html', {
        'place': place,
    })

def place_list(request):
    place_list= places_list.objects.order_by('place')
    return render_to_response('place_list.html', {
        'place_list': place_list,
    })

def place_detail(request, neighborhood):
    place_detail = place_detail.objects.get.order_by('place')
    stories = story.objects.filter(location__point__within = hood)
    return render_to_response('place_detail.html', {
        'place_detail' : place_detail
    })
