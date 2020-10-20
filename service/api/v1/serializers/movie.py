"""
Movie serializers
"""
from rest_framework import serializers
from service.apps.movie import models as movie_models
from logging import getLogger
from django.db import transaction
logger = getLogger(__name__)


class MovieDirectorSerializer(serializers.ModelSerializer):

    class Meta:
        model = movie_models.MovieDirector
        fields = ('name', )


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = movie_models.Genre
        fields = ('name', )


class MovieSerializer(serializers.ModelSerializer):
    director = MovieDirectorSerializer(many=False)
    genres = GenreSerializer(many=True)

    class Meta:
        model = movie_models.Movie
        fields = ('id', 'name', 'popularity', 'director', 'genres', 'imdb_score')

    @transaction.atomic
    def create(self, validated_data):
        genres = validated_data.pop("genres")
        director, created = movie_models.MovieDirector.objects.get_or_create(**validated_data.pop('director'))
        movie = movie_models.Movie.objects.create(director=director, **validated_data)
        for genre in genres:
            genre, created = movie_models.Genre.objects.get_or_create(**genre)
            movie_models.MovieGenre.objects.create(movie=movie, genre=genre)
        return movie

    @transaction.atomic
    def update(self, instance, validated_data):
        genres = validated_data.pop("genres")
        director, created = movie_models.MovieDirector.objects.get_or_create(**validated_data.pop('director'))
        validated_data.update(dict(director=director))
        movie_models.MovieGenre.objects.filter(movie=instance).delete()
        for genre in genres:
            genre, created = movie_models.Genre.objects.get_or_create(**genre)
            movie_models.MovieGenre.objects.create(movie=instance, genre=genre)
        super(MovieSerializer, self).update(instance, validated_data)
        return instance



