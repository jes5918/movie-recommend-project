from django.db import models
from django.conf import settings

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    pubDate = models.IntegerField()
    director = models.CharField(max_length=200)
    actor = models.CharField(max_length=200)
    userRating = models.FloatField()
    genre = models.CharField(max_length=200)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')
    
class Comment_movie(models.Model):    
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    rank = models.IntegerField()  
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)