# Restframework Imports
from rest_framework.decorators import (
    api_view,
    parser_classes,
    permission_classes,
    authentication_classes,
)


from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser

from rest_framework import (
    permissions,
    status,
)

from knox.auth import TokenAuthentication

from django.http import JsonResponse

from .models import Celebrities, PromoCode
from as_plugin_conf import *
from .serializers import *
from as_plugin_conf import handle_uploaded_file

# Create your views here.


@api_view(['GET'])
def get_celebrities(request):
    celebrities = Celebrities.objects.all()
    serialized_data = CelebritiesSerializer(celebrities, many=True)

    if serialized_data.is_valid:
        return JsonResponse({
            "status": "Success",
            "code": status.HTTP_200_OK,
            "data": [serialized_data.data]
        })
    else:
        return JsonResponse({
            "status": "Failed",
            "code": status.HTTP_400_BAD_REQUEST,
        })

@api_view(['GET'])
def get_celebrity(request, celebrityId):
    celebrity = Celebrities.objects.get(id=celebrityId)
    serialized_data = CelebritiesSerializer(celebrity, many=False)

    if serialized_data.is_valid:
        return JsonResponse({
            "status": "Success",
            "code": status.HTTP_200_OK,
            "data": [serialized_data.data]
        })
    else:
        return JsonResponse({
            "status": "Failed",
            "code": status.HTTP_400_BAD_REQUEST,
        })
    

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def get_promo_code(request, code):
    current_user = get_token_user(request.headers["Authorization"].split()[1][:8])
    try:
        promo_code = PromoCode.objects.get(name=code, user=current_user)
    except ObjectDoesNotExist:
        return JsonResponse({
            "status": "Failed",
            "code": status.HTTP_404_NOT_FOUND,
        })   
    else:
        serialized_data = PromoCodeSerializer(promo_code, many=False)
        
        if serialized_data.is_valid:
            return JsonResponse({
                "status": "Success",
                "code": status.HTTP_200_OK,
                "data": [serialized_data.data]
            })
        else:
            return JsonResponse({
                "status": "Failed",
                "code": status.HTTP_400_BAD_REQUEST,
            })
        

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def verify_users_promo_code(request):
    current_user = get_token_user(request.headers["Authorization"].split()[1][:8])
    promo_code_is_active = PromoCode.objects.filter(user=current_user, active=True).exists()
    return JsonResponse({
        "status": "Success",
        "code": status.HTTP_200_OK,
        "data": [promo_code_is_active]
    })
        

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
@parser_classes([MultiPartParser])
def upload_celebrity_receipt(request):
    current_user = get_token_user(request.headers["Authorization"].split()[1][:8])

    try:
        image_file = request.data['file']
        uploaded_file_path = handle_uploaded_file(
            image_file, current_user.email)
    except KeyError:
        response = {
            'status': 'Upload Failed',
            'code': status.HTTP_400_BAD_REQUEST,
            'message': 'Profile image has not been attached. No file resource found'
        }
        return JsonResponse(response)
    except ObjectDoesNotExist:
        # Construct response for exception.
        response = {
            'status': 'Upload Failed',
            'code': status.HTTP_400_BAD_REQUEST,
            'message': 'Email not found'
        }
    else:
        log=ActivityLog(user=current_user, file_path=uploaded_file_path, name=request.data["uploadPurpose"] )
        log.save()
        response = {
            'status': 'Success',
            'code': status.HTTP_201_CREATED,
            'message': 'File Uploaded Successfully'
        }
    return JsonResponse(response)

@api_view(['POST'])
def send_message(request):
    try:
        message = Message(name=request.data['name'], email=request.data['email'], message=request.data['message'])
        message.save()
    except KeyError:
        response = {
            'status': 'Failed to send message',
            'code': status.HTTP_400_BAD_REQUEST,
            'message': 'Email not sent'
        }
        return JsonResponse(response)
    else:
        response = {
            'status': 'Success',
            'code': status.HTTP_201_CREATED,
            'message': 'Message sent'
        }
    return JsonResponse(response)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def get_activity_log(request):
    current_user = get_token_user(request.headers["Authorization"].split()[1][:8])

    try:
        activity_log = ActivityLog.objects.filter(user=current_user)
    except ObjectDoesNotExist:
        return JsonResponse({
            "status": "Failed",
            "code": status.HTTP_404_NOT_FOUND,
        })   
    else:
        serialized_data = ActivityLogSerializer(activity_log, many=True)
        
        if serialized_data.is_valid:
            return JsonResponse({
                "status": "Success",
                "code": status.HTTP_200_OK,
                "data": [serialized_data.data]
            })
        else:
            return JsonResponse({
                "status": "Failed",
                "code": status.HTTP_400_BAD_REQUEST,
            })