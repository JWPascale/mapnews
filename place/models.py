from django.contrib.gis.db import models

class Location(models.Model):
    address = models.CharField(max_length=200)
    point = models.PointField()
    objects = models.GeoManager()
    def __unicode__(self):
        return self.address
    def get_absolute_url(self):
        return "/Location/%s/" %self.slug


class Neighborhoods(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(blank=True, null=True)
    mpoly = models.MultiPolygonField()
    objects = models.GeoManager()
    class Meta:
        verbose_name_plural = "neighborhoods"
    def __unicode__(self):
        return self.address
    def get_absolute_url(self):
        return "/Neighborhoods/%s/" %self.slug

class Place(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(blank=True, null=True)
    mpoly = models.MultiPolygonField()
    objects = models.GeoManager()
    class Meta:
        verbose_name_plural = "places"
    def __unicode__(self):
        return self.name
    def get_absolute_url(self):
        return "/place/%i/" % self.id
