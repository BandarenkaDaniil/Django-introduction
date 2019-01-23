from django.urls import path, include

from .views import HomePage, Register

app_name = 'railways'

urlpatterns = [
    path('', HomePage.as_view(), name='home_page'),
    path('register/', Register.as_view(), name='register'),
]
