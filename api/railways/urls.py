from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from api.railways import views

urlpatterns = [
    path('ride/', views.SpecificRidesAPI.as_view()),

    path('tickets/', views.TicketListAPI.as_view()),
    path('buy_ticket/', views.BuyTicket.as_view()),
    path('user_tickets/', views.UserTicket.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
