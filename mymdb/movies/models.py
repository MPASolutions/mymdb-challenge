from django.db import models
from cast.models import Person

class Movie(models.Model):
    title = models.CharField(50, default='')
    description = models.CharField(20000, default='')
    director = models.ForeignKey(Person , on_delete=models.CASCADE)
    created_at = models.DateField()
    updated_at = models.DateField()
    
class Character(models.Model):
    character = models.CharField(50, default='')
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    created_at = models.DateField()
    updated_at = models.DateField()