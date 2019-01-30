from django.urls import path, include

from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('api/', include('railways.api_urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
