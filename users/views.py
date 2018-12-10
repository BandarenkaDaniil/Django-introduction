from django.shortcuts import render
from rest_framework import generics

from users.serializers import UserSerializer

from users.models import User


class UserListAPI(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
