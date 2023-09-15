from django.contrib import admin
from cast.models import Person
from movies.models import Movie, Character

# Register your models here.
admin.site.register(Person)
admin.site.register(Movie)
admin.site.register(Character)