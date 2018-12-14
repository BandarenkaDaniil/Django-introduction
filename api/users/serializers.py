from django.contrib.auth import password_validation
from django.core.validators import validate_email, ValidationError
from django.core import exceptions

from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'email', 'first_name', 'last_name',
            'created_at', 'updated_at'
        )
        read_only_fields = ('id', 'created_at', 'updated_at',)


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

