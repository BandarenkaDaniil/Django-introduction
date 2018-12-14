from django.contrib.auth import authenticate, login
from django.http import JsonResponse

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.views import Token

from api.users.serializers import UserLoginSerializer, UserSerializer

from users.models import User


class UserListAPI(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class Login(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        password = serializer.validated_data['password']

        user = authenticate(email=email, password=password)

        if user is not None:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)

            return JsonResponse(
                {'login status': True, 'token': token.key}
            )
        else:
            return JsonResponse(
                {'login status': False},
                status=400
            )















