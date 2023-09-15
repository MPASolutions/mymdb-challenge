from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from datetime import datetime
import json

from movies.models import Character, Movie
from cast.models import Person
from reviews.models import Review
from reviews.api.serializers import ReviewMovieSerializer
from cast.api.serializers import PersonMovieSerializer
from movies.api.serializers import CharacterSerializer, CharacterMovieSerializer,MovieSerializer, MoviePostSerializer

class CharacterCreateAPIView(APIView):

    def get(self, request):
        character = Character.objects
        serializer = CharacterSerializer(character, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CharacterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CharacterDetailAPIView(APIView):

    def get_character(self, pk):
        character= get_object_or_404(Character, pk=pk)
        return character
    
    def get(self, request, pk):
        character = self.get_character(pk)
        serializer = CharacterSerializer(character)
        return Response(serializer.data)
    
    def put(self, request, pk):
        character = self.get_character(pk)
        serializer = CharacterSerializer(character, data=request.data)
        
        
        if serializer.is_valid():
            serializer.validated_data["updated_at"] = datetime.now()
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        character = self.get_character(pk)
        character.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
def format_movie(i):
    k = 0
    q = 0
    j = 0

    try:
        dir = PersonMovieSerializer(Person.objects.get(id=int(i["director"]))).data
    except:
        dir = json.loads("{}")

    i['director'] = dir
    for a in i["actors"]:
        try:
            act = CharacterMovieSerializer(Character.objects.get(id=a[q])).data
            act["person"] = PersonMovieSerializer(Person.objects.get(id=int(act["person"]))).data
        except:
            act = json.loads("{}")
        i['actors'][q] = act
        q += 1
    for s in i['scripts']:
        try:
            per = PersonMovieSerializer(Person.objects.get(id=s)).data
        except:
            per = json.loads("{}")
        i["scripts"][k] = per
        k += 1
    print (i)
    for r in i["reviews"]:
        print(Review.objects.all())
        
        try:
            rev = ReviewMovieSerializer(Review.objects.get(id=r)).data
            print(1)
        except:
            print(2)
            rev = json.loads("{}")
        i["reviews"][j] = rev
        
        j+=1
    return i
class MovieCreateAPIView(APIView):

    def get(self, request):
        movie = Movie.objects
        serializer = MovieSerializer(movie, many=True)
        for i in serializer.data:
            format_movie(i)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = MoviePostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MovieDetailAPIView(APIView):

    def get_movie(self, pk):
        movie= get_object_or_404(Movie, pk=pk)
        return movie
    
    def get(self, request, pk):
        movie = self.get_movie(pk)
        serializer = MovieSerializer(movie)
        
        return Response(format_movie(serializer.data))
    
    def put(self, request, pk):
        movie = self.get_movie(pk)
        serializer = MoviePostSerializer(movie, data=request.data)
        
        if serializer.is_valid():
            serializer.validated_data["updated_at"] = datetime.now()
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        movie = self.get_movie(pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)