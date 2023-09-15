from rest_framework import serializers
from movies.models import Character,Movie
from reviews.models import Review
from reviews.api.serializers import ReviewMovieSerializer

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ("id", "person", "character", "movie")

class CharacterMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ("person", "character")

#class MovieObjectRelatedField(serializers.RelatedField):
#    def to_representation(self, value):
#        serializer = ReviewMovieSerializer(value)
#        return serializer.data
    
class MovieSerializer(serializers.ModelSerializer):
    #reviews = MovieObjectRelatedField(many = True, queryset=Review.objects.all())
    class Meta:
        model = Movie
        fields = ("id", "title", "description", "director","scripts", "actors" , "reviews")

class MoviePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ("id", "title", "description", "director","scripts" )
        
