from django.contrib.gis.db import models

class Location(models.Model):
    address = models.CharField(max_length=200)
    point = models.PointField()
    objects = models.GeoManager()
    def __unicode__(self):
        return self.address


class Neighborhoods(models.Model):
    neighborhoods = models.CharField(max_length=255)
    

class Places(models.Model):
    places = models.TextField()
    class Meta:
        verbose_name_plural = "places"
