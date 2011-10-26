from django.db import models
from place.models import Location

class Byline(models.Model):
    name_slug = models.SlugField(max_length=50)
    def __unicode__(self):
        return self.name

class Section(models.Model):
    name = models.CharField(max_length=200)
    name_slug = models.SlugField(max_length=50)
    def __unicode__(self):
        return self.name

class Story(models.Model):
    headline = models.CharField(max_length=200)
    byline = models.ManyToManyField(blank=True, null=True)
    pubdate = models.DateField('date published')
    location = models.CharField(max_length=200)
    url = models.URLField(max_length=200)
    section = models.ForeignKey(Section)


