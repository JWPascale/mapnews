from django.db import models
from place.models import Location

class Byline(models.Model):
    name = models.CharField(max_length=200)
    name_slug = models.SlugField(max_length=50)
    def get_absolute_url(self):
        return "/Byline/%s/" % self.slug
    def __unicode__(self):        
        return self.name

class Section(models.Model):
    name = models.CharField(max_length=200)
    name_slug = models.SlugField(max_length=50)
    def __unicode__(self):
        return self.name    
    def get_absolute_url(self):
        return "/Section/%s/" % self.slug
        

class Story(models.Model):
    headline = models.CharField(max_length=200)
    byline = models.ManyToManyField(Byline, blank=True, null=True)
    pubdate = models.DateField('date published')
    location = models.CharField(max_length=200)
    url = models.URLField(max_length=200)
    section = models.ManyToManyField(Section, blank=True, null=True)
    class Meta:
        verbose_name_plural = "stories"
    def __unicode__(self):
        return self.headline
    def get_absolute_url(self):
        return "/story/%i/" % self.id
