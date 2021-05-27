from django.contrib import admin
from .models import Movie, Comment_movie
# Register your models here.

admin.site.register(Movie)
admin.site.register(Comment_movie)