from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from service.api.v1.resources import movie

from .resources import swagger

router = DefaultRouter()
router.register(r'movie', movie.MovieViewSet, basename='movie')
app_name = 'api-v1'

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api_docs/$', swagger.SwaggerSchemaView.as_view()),
]

