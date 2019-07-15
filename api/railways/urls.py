from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from api.railways import views

urlpatterns = [
    path('rides/', views.SpecificRidesAPI.as_view()),
    path('stations/', views.StationListAPI.as_view()),
    path('tickets/', views.TicketListAPI.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
