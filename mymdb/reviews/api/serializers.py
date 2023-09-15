from rest_framework import serializers
from reviews.models import Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ("id", "review", "movie")
        
class ReviewMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ("review",)