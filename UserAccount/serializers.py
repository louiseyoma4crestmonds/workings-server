from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from .models import ApplicationUserAccount

# Serializer Sign-in data
class SigninSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    user_model = get_user_model()

    def validate(self, data):
        user = authenticate(**data)

        if user and user.is_active:
            return user
        

# User Serializer.
class ApplicationUserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationUserAccount
        fields = "__all__"

# User Serializer
class AccountRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationUserAccount
        fields = [
            'email',
        ]