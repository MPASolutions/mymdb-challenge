from django.db import models
from movies.models import Movie, Character
from cast.models import Person
class Reviews(models.Model):
    review = models.CharField(20000, default='')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    created_at = models.DateField()
    updated_at = models.DateField()