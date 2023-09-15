from django.db import models
from movies.models import Movie, Character
from cast.models import Person
from datetime import datetime
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType

class Review(models.Model):
    review = models.CharField(max_length=20000, default='')
    movie = models.ForeignKey(Movie, on_delete=models.DO_NOTHING, default=None, related_name="reviews")
    #tags = GenericRelation(Movie, related_query_name="reviews")
    #content_type = models.ForeignKey(ContentType,
    #   on_delete=models.DO_NOTHING,
    #   related_name="reviews"
    #
    #bject_id = models.PositiveIntegerField()
    #bj = GenericForeignKey('content_type', 'object_id')
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)