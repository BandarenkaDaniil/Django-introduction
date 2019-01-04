from django.urls import path, include

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi


api_info = openapi.Info(
    title='Railways API',
    default_version='v0.0',
    description='Test description',
    terms_of_service="https://www.google.com/policies/terms/",
    contact=openapi.Contact(email="danik@example.com"),
    license=openapi.License(name="BSD License"),
)

schema_view = get_schema_view(
    api_info,
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    # swagger urls
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('swagger<str:format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),

    # main urls
    path('railways/', include('api.railways.urls')),
    path('users/', include('api.users.urls')),
]
