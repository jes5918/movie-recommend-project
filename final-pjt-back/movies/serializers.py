from rest_framework import serializers
from .models import Movie, Comment_movie
from accounts.serializers import UserSerializer


class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'



class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class ReviewListSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    movie = MovieSerializer()
    created_at = serializers.DateTimeField(format="%Y.%m.%d %H:%M:%S", required=False, read_only=True)
    updated_at = serializers.DateTimeField(format="%Y.%m.%d %H:%M:%S", required=False, read_only=True)

    class Meta:
        model = Comment_movie
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    movie = MovieSerializer(required=False)
    created_at = serializers.DateTimeField(format="%Y.%m.%d %H:%M:%S", required=False, read_only=True)
    updated_at = serializers.DateTimeField(format="%Y.%m.%d %H:%M:%S", required=False, read_only=True)
    
    class Meta:
        model = Comment_movie
        fields = '__all__'
        read_only_fields = ('id', 'user', 'created_at', 'updated_at')
