from mapnews.story.models import Place
from django.shortcuts import render_to_response

def homepage(request):
    location = Location.objects.order_by('name')
    return render_to_response('homepage.html', {
        'locations': location,
    })

def location(request):
     = Location.objects.order_by('Location')
    return render_to_response('location.html', {
        'locations': location,
    })

