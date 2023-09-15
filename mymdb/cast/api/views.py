from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from datetime import datetime

from cast.models import Person
from cast.api.serializers import PersonSerializer

class PersonCreateAPIView(APIView):
    
    def get(self, request):
        person = Person.objects
        serializer = PersonSerializer(person, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PersonDetailAPIView(APIView):

    def get_person(self, pk):
        person= get_object_or_404(Person, pk=pk)
        return person
    
    def get(self, request, pk):
        person = self.get_person(pk)
        serializer = PersonSerializer(person)
        return Response(serializer.data)
    
    def put(self, request, pk):
        person = self.get_person(pk)
        serializer = PersonSerializer(person, data=request.data)
        
        
        if serializer.is_valid():
            serializer.validated_data["updated_at"] = datetime.now()
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        person = self.get_person(pk)
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)