from django.db import models
from django.utils.timezone import now


class MovieDirector(models.Model):
    name = models.CharField(max_length=500, db_index=True)

    class Meta:
        db_table = "movie_director"


class Genre(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "genre"


class Movie(models.Model):
    name = models.CharField(max_length=500, db_index=True)
    popularity = models.FloatField()
    director = models.ForeignKey(MovieDirector, on_delete=models.DO_NOTHING)
    imdb_score = models.FloatField()
    genres = models.ManyToManyField(Genre, through='MovieGenre')
    created = models.DateTimeField(default=now)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "movie"


class MovieGenre(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    class Meta:
        db_table = "movie_genre"