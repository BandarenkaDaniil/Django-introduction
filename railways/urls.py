from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from railways import views


urlpatterns = [
    path('trains/', views.TrainList.as_view()),
    path('trains/<int:pk>/', views.TrainDetail.as_view()),
    path('stations/', views.StationList.as_view()),
    path('stations/<int:pk>/', views.StationDetail.as_view()),
    path('rides/', views.RideList.as_view()),
    path('rides/<int:pk>/', views.RideDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
