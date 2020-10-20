from django.conf.urls import url, include
from django.conf import settings
from django.contrib import admin
from django.urls import path


admin.site.site_header = 'Template Administration'
urlpatterns = [
    url(r'v1/', include('service.api.v1.urls', namespace='api-v1')),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    from rest_framework_swagger.views import get_swagger_view
    urlpatterns += [
        url(r'^swagger-docs/', get_swagger_view(title='Template API')),
    ]
