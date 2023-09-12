from django.db import models

class Person(models.Model):
    firstName = models.CharField(max_length=20, default='')
    lastName = models.CharField(20, default='') 
    biography = models.CharField(20000, default='')      
    created_at = models.DateField()
    updated_at = models.DateField()
