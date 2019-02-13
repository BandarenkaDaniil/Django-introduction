from django.contrib.auth import authenticate, login
from django.http import JsonResponse

from rest_framework import generics
from rest_framework.authtoken.views import Token
from rest_framework.views import APIView

from api.users.serializers import UserLoginSerializer, UserSerializer
from users.models import User


class UserListAPI(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class Login(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        password = serializer.validated_data['password']

        user = authenticate(email=email, password=password)

        if user:
            login(request, user)
            token, _ = Token.objects.get_or_create(user=user)

            return JsonResponse(
                {'token': token.key},
                status=200
            )
        else:
            return JsonResponse(
                {
                    'password': 'There\'s no user with credentials '
                                'provided or password is incorrect'
                },
                status=400
            )


class Logout(APIView):
    def post(self, request):
        Token.objects.get(user=request.user).delete()

        return JsonResponse({
            'logout status': True
        })
