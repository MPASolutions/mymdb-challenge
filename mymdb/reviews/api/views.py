from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from datetime import datetime

from reviews.models import Review
from movies.models import Movie, Character
from reviews.api.serializers import ReviewSerializer 

class ReviewCreateAPIView(APIView):
    
    def get(self, request):
        review = Review.objects
        serializer = ReviewSerializer(review, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            #match(serializer.validated_data["content_type"]):
            #    case 1: serializer.validated_data["content_type"] = Movie
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReviewDetailAPIView(APIView):
  
    def get_review(self, pk):
        review= get_object_or_404(Review, pk=pk)
        return review
    
    def get(self, request, pk):
        review = self.get_review(pk)
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    
    def put(self, request, pk):
        review = self.get_review(pk)
        serializer = ReviewSerializer(review, data=request.data)
        
        if serializer.is_valid():
            serializer.validated_data["updated_at"] = datetime.now()
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        review = self.get_review(pk)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)