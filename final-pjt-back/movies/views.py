from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Movie, Comment_movie
from .serializers import MovieListSerializer, MovieSerializer, ReviewListSerializer, ReviewSerializer
from rest_framework import status
from django.http import JsonResponse
import json
import urllib.request
# Create your views here.

@api_view(['GET'])
def index(request):
    movies = Movie.objects.all()
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def detail(request, movie_id):    
    movie = get_object_or_404(Movie, id=movie_id)
    serializer = MovieSerializer(movie)                    
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def review(request, movie_pk):      
    movie = get_object_or_404(Movie, pk=movie_pk)        
    if request.method == 'GET':
        reviews = Comment_movie.objects.filter(movie_id=movie_pk)         
        serializer = ReviewListSerializer(reviews, many=True)        
        return Response(serializer.data)
    elif request.method == 'POST':
        if request.user.is_authenticated:
            serializer = ReviewSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):            
                serializer.save(user=request.user, movie=movie)
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        
        return Response(status=status.HTTP_401_UNAUTHORIZED)
        

@api_view(['DELETE', 'PUT'])
@permission_classes([IsAuthenticated])
def review_change(request, movie_pk, review_pk):      
    movie = get_object_or_404(Movie, pk=movie_pk)       
    review = get_object_or_404(Comment_movie, pk=review_pk)       
    if request.user == review.user:
        if request.method == 'PUT':
            serializer = ReviewSerializer(instance=review, data=request.data)                
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            review.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)            
    return Response(status=status.HTTP_403_FORBIDDEN)


@permission_classes([IsAuthenticated])
def check_review(request, movie_pk, review_pk):      
    review = get_object_or_404(Comment_movie, pk=review_pk)       
    if review.user==request.user:
        return Response({true})
    return Response(status=status.HTTP_403_FORBIDDEN)




def search(request):
    if request.method == 'GET':
        client_id = 'gnW5GgGzsAYsjTq8UCY5'
        client_secret = 'XP2YI4352O'
        q = request.GET['query']
        print(q)
        encText = urllib.parse.quote("{}".format(q))
        url = "https://openapi.naver.com/v1/search/movie?query=" + encText 
        movie_api_request = urllib.request.Request(url)
        movie_api_request.add_header("X-Naver-Client-Id", client_id)
        movie_api_request.add_header("X-Naver-Client-Secret", client_secret)
        response = urllib.request.urlopen(movie_api_request)
        rescode = response.getcode()
        if (rescode == 200):
            response_body = response.read()
            result = json.loads(response_body.decode('utf-8'))
            items = result.get('items')
            context = {
                'items': items
            }
            return JsonResponse(context)