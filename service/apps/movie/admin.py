from django.contrib import admin
from .models import Movie, MovieDirector, MovieGenre, Genre

admin.site.register(Movie)
admin.site.register(MovieDirector)
admin.site.register(Genre)
admin.site.register(MovieGenre)
