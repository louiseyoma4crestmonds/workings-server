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

from .models import TrackingId
from as_plugin_conf import *
from .serializers import *
from as_plugin_conf import handle_uploaded_file

# Create your views here.


@api_view(['GET'])
def validate_tracking_id(request, tracking_id):
    tracking_id_is_valid=''

    tracking_id_is_valid = TrackingId.objects.filter(tracking_id=tracking_id).exists()

    return JsonResponse({
        "status": "success",
        "code": status.HTTP_200_OK,
        "data": tracking_id_is_valid
    })

@api_view(['GET'])
def get_tracking_id(request, tracking_id):
    try:
        tracking_id = TrackingId.objects.get(tracking_id=tracking_id)
    except ObjectDoesNotExist:
        return JsonResponse({
            "status": "Failed",
            "code": status.HTTP_404_NOT_FOUND,
        })
    else:
        serialized_data = TrackingIdSerializer(tracking_id,many=False)

        return JsonResponse({
            "status": "success",
            "code": status.HTTP_200_OK,
            "data": serialized_data.data
        })
    
@api_view(['GET'])
def get_tracking_id_history(request, tracking_id):
    try:
        tracking_id_history = TrackingIdHistory.objects.filter(tracking_id__tracking_id=tracking_id).order_by('-id')
    except ObjectDoesNotExist:
        return JsonResponse({
            "status": "Failed",
            "code": status.HTTP_404_NOT_FOUND,
        })
    else:
        serialized_data = TrackingIdHistorySerializer(tracking_id_history,many=True)

        return JsonResponse({
            "status": "success",
            "code": status.HTTP_200_OK,
            "data": serialized_data.data
        })