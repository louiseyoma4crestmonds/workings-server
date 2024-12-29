import logging
from django.http import JsonResponse


from rest_framework.decorators import api_view
from rest_framework import status


from .serializers import (
    ApplicationUserAccountSerializer,
    SigninSerializer,
)

from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import generics, permissions, status
from django.core.exceptions import ObjectDoesNotExist

from django.utils import timezone
from datetime import timedelta

from as_plugin_conf import *

# Imports from third parties
from knox.models import AuthToken
from knox.auth import TokenAuthentication

from .models import ApplicationUserAccount
from celebritymanagement .models import PromoCode


# Get an instance of a logger
logger = logging.getLogger(__name__)

# Create your views here.

def home(request):
    return("Welcome to User Account")






@api_view(['POST'])
def sign_in(request):
    serializer=SigninSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data
    token = AuthToken.objects.create(user)[1]

    authenticated_user = {
        'email': user.email,
        'is_staff':user.is_staff,
        'is_superuser':user.is_superuser,
        'first_name': user.first_name,
        'last_name': user.last_name,
    }
    # Initialize Response
    response = {
        'status': '',
        'code': '',
        'message': '',
        'data': []
    }
    response['data'] = [{"user": authenticated_user, "token": token}]
    response['status'] = 'Success'
    response['code'] = status.HTTP_200_OK

    return JsonResponse(response)



@api_view(['POST'])
def register(request):
    if not ApplicationUserAccount.objects.filter(email=request.data['email']).exists():
        user_account = ApplicationUserAccount(
            email=request.data['email'], first_name=request.data['firstName'], last_name=request.data['lastName']
        )
        password=generate_random_string(8, "letters")
        user_account.save()
        user_account.set_password(password)
        user_account.save()

        code=generate_random_string(8, "letters")
        new_promo_code=PromoCode(user=user_account, name=code)
        new_promo_code.save()

        email_context = {
            'name': user_account.first_name,
            'email': user_account.first_name,
            'password': password
        }
        try:
            send_email_to_user(
                user_account.email,
                email_context,
                            "email/account_creation.html",
                            "email/account_creation.txt",
                            "Account Creation"
            )
        except Exception as e:
            return JsonResponse({
                "error": "Error sending email",
                "code": 500
            })
        return JsonResponse({
            "status": "success",
            "code": status.HTTP_201_CREATED,
        })
    else:
        return JsonResponse({
            "status": "Account with email already exist",
            "code": status.HTTP_406_NOT_ACCEPTABLE,
        })





