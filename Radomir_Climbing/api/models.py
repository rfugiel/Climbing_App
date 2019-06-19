from django.db import models

class Route(models.Model):
    name = models.CharField(max_length=100)
    grade = models.CharField(max_length=10)
    MP_rating = models.FloatField() # Refers to rating on mountain project
    location = models.CharField(max_length=2) # Refers to a USA state. eg: IL,CO,MN, etc...
    area_name = models.CharField(max_length=100) # Refers to the "crag." eg: Red River Gorge, Devil's Lake
    longitude = models.FloatField()
    latitude = models.FloatField()

    def __str__(self):
        return self.name
