from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from api.users import views
from api.railways.views import UserTickets

urlpatterns = [
    path('', views.UserListAPI.as_view()),
    path('tickets/', UserTickets.as_view()),
    path('login/', views.Login.as_view()),
    path('logout/', views.Logout.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
