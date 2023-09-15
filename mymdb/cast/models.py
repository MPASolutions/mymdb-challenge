from django.db import models
from datetime import datetime

class Person(models.Model):
    first_name = models.CharField(max_length=20, default='')
    last_name = models.CharField(max_length=20, default='') 
    biography = models.CharField(max_length=20000, default='')
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)
