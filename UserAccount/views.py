import logging
from django.http import JsonResponse


from rest_framework.decorators import api_view
from rest_framework import status


from .serializers import (
    ApplicationUserAccountSerializer,
    SigninSerializer,
)

from BBConsignment.models import BusinessAccount, ConsignmentUser

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
    print(request.data)
    if not ApplicationUserAccount.objects.filter(email=request.data['email']).exists():
        user_account = ApplicationUserAccount(
            email=request.data['email'], 
            first_name=request.data['firstName'], 
            last_name=request.data['lastName'],
            country=request.data['country']
        )
        if(request.data['password']==request.data['confirmPassword']):
            password=request.data['password']
            user_account.set_password(password)
            user_account.save()
        else:
            return JsonResponse({
                "status": "Password Mismatch",
                "code": status.HTTP_406_NOT_ACCEPTABLE,
            })
        
        consignment_user=ConsignmentUser(
            user=user_account,
            secreteQuestion=request.data['secreteQuestion'],
            secreteAnswer=request.data['secreteAnswer'],
            address1=request.data['address1'],
            address2=request.data['address2'],
            company=request.data['company'],
            country=request.data['country'],
            postal_code=request.data['postalCode'],
            province=request.data['province'],
            phone=request.data['phone'],
            city=request.data['city'],
        )
        consignment_user.save()

        email_context = {
            'name': user_account.first_name,
            'email': user_account.email,
            'password': password,
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



@api_view(['POST'])
def request_business_account(request):
    if not BusinessAccount.objects.filter(email=request.data['email']).exists():
        try:
            business_account = BusinessAccount(
                email=request.data['email'], 
                first_name=request.data['firstName'], 
                last_name=request.data['lastName'],
                address=request.data['address1'],
                message=request.data['message'],
                company=request.data['company'],
                postal_code=request.data['postalCode'],
                vat=request.data['vat'],
                phone=request.data['phone'],
                city=request.data['city'],
            )
            business_account.save()
        except KeyError:
            return JsonResponse({
                "status": "All fields are required",
                "code": status.is_client_error,
            })
        else:
            return JsonResponse({
                "status": "success",
                "code": status.HTTP_201_CREATED,
            })
    else:
        return JsonResponse({
            "status": "Request with email already exists",
            "code": status.HTTP_406_NOT_ACCEPTABLE,
        })

