"""django_introduction URL Configuration"""

from django.contrib import admin
from django.urls import path, include

from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth', obtain_jwt_token),
    path('api-token-verify', verify_jwt_token),
    path('api/', include([
        path('railways/', include('railways.urls.api_urls')),
        path('users/', include('users.urls.api_urls'))
    ])),
    path('railways/', include('railways.urls')),
    path('users/', include('users.urls')),
]
