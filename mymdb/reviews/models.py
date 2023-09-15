from django.db import models
from movies.models import Movie, Character
from cast.models import Person
from datetime import datetime
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType

class Review(models.Model):
    review = models.CharField(max_length=20000, default='')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, default=None, related_name="reviews")
    #tags = GenericRelation(Movie, related_query_name="reviews")
    #content_type = models.ForeignKey(ContentType,
    #   on_delete=models.https://github.com/Fb1234566/mymdb-challenge/pull/4/conflict?name=mymdb%252Freviews%252Fapi%252Fviews.py&base_oid=d45e075fb5b04a76617c2636e3f28eea83cde2ba&head_oid=ac249ad0fef0793b645edcbe531d8a38b3ae3f57DO_NOTHING,
    #   related_name="reviews"
    #
    #bject_id = models.PositiveIntegerField()
    #bj = GenericForeignKey('content_type', 'object_id')
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)
