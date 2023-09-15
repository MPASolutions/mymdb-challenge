from django.db import models
from cast.models import Person
from datetime import datetime
from django.contrib.contenttypes.fields import GenericRelation



class Movie(models.Model):
    title = models.CharField(50, default='')
    description = models.CharField(max_length=20000, default='')
    director = models.ForeignKey(Person, on_delete=models.DO_NOTHING)
    scripts = models.JSONField(default=None)
    object_id = GenericRelation("reviews.Review")
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)
    
    
class Character(models.Model):
    character = models.CharField(max_length=50, default='')
    person = models.ForeignKey(Person, on_delete=models.DO_NOTHING)
    movie = models.ForeignKey(Movie, on_delete=models.DO_NOTHING, related_name="actors", default=None)
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)
    