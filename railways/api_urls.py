from django.urls import path, include

from rest_framework.urlpatterns import format_suffix_patterns

from railways import views


urlpatterns = [
    path('trains/', views.TrainListAPI.as_view()),
    path('trains/<int:pk>/', views.TrainDetailAPI.as_view()),
    path('stations/', views.StationListAPI.as_view()),
    path('stations/<int:pk>/', views.StationDetailAPI.as_view()),
    path('rides/', views.RideListAPI.as_view()),
    path('rides/<int:pk>/', views.RideDetailAPI.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
