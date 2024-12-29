from rest_framework import serializers
from .models import *

# Serializer Sign-in data
class CelebritiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Celebrities
        fields = "__all__"

# Serializer PromoCode
class PromoCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PromoCode
        fields = "__all__"

# Serializer PromoCode
class ActivityLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityLog
        fields = "__all__"