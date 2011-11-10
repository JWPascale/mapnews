from mapnews.story.models import Story
from django.shortcuts import render_to_response

def homepage(request):
    story = Story.objects.order_by('headline')
    return render_to_response('homepage.html', {
        'story': story,
    })

def headline(request):
    headline = Headline.objects.order_by('headline')
    return render_to_response('headline.html', {
        'headlines': headlines,
    })

def detail(request):
    detail = Story.objects
    return render_to_response('detail.html', {
        'detail': detail,
    })
