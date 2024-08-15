# diary/models.py

from django.db import models

class Travel(models.Model):
    location = models.CharField(max_length=255)
    latitude = models.FloatField(null=True, blank=True)  # Геопозиция (широта)
    longitude = models.FloatField(null=True, blank=True)  # Геопозиция (долгота)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    cultural_heritage_sites = models.TextField(null=True, blank=True)
    places_to_visit = models.TextField(null=True, blank=True)
    convenience_rating = models.IntegerField(null=True, blank=True)
    safety_rating = models.IntegerField(null=True, blank=True)
    population_density_rating = models.IntegerField(null=True, blank=True)
    vegetation_rating = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.location
