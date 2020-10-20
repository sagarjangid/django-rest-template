"""
Movie endpoints.
"""

from rest_framework import viewsets
from service.apps.movie import models as movie_models
from ..serializers import movie as movie_serializers
from logging import getLogger
from ..paginations import BasicPagination
from oauth2_provider.contrib.rest_framework import OAuth2Authentication
from ..permissions import IsValidAdmin

logger = getLogger(__name__)


class MovieViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'put', 'post']
    authentication_classes = (OAuth2Authentication, )
    pagination_class = BasicPagination
    model = movie_models.Movie
    queryset = movie_models.Movie.objects.all()
    serializer_class = movie_serializers.MovieSerializer
    search_fields = ('name', 'director__name', 'genres__name')

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = ()
        else:
            permission_classes = (IsValidAdmin, )
        return [permission() for permission in permission_classes]

