from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from api.railways import views

urlpatterns = [
    # path('route_items/', views.RouteItemListAPI.as_view()),
    # path('route_items/<int:pk>/', views.RouteItemDetailAPI.as_view()),

    path('rides/', views.RideListAPI.as_view()),
    path('rides/<int:pk>/', views.RideDetailAPI.as_view()),

    path('routes/', views.RouteListAPI.as_view()),
    path('routes/<int:pk>/', views.RouteDetailAPI.as_view()),

    path('stations/', views.StationListAPI.as_view()),
    path('stations/<int:pk>/', views.StationDetailAPI.as_view()),

    path('tickets/', views.TicketListAPI.as_view()),
    path('tickets/<int:pk>/', views.TicketDetailAPI.as_view()),

    path('trains/', views.TrainListAPI.as_view()),
    path('trains/<int:pk>/', views.TrainDetailAPI.as_view()),

    path('tracks/', views.TrackListAPI.as_view()),
    path('tracks/<int:pk>/', views.TrackDetailAPI.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
