from django.urls import path, include


urlpatterns = [
    path('railways/', include('api.railways.urls')),
    path('users/', include('api.users.urls')),
]
