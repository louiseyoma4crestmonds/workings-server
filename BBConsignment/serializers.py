from rest_framework import serializers
from .models import *

# Serializer Sign-in data
class TrackingIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackingId
        fields = "__all__"

# Serializer Sign-in data
class TrackingIdHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackingIdHistory
        fields = "__all__"