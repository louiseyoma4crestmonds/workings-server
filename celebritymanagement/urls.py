from .views import *
from django.urls import path

urlpatterns = [
    path('get-celebrities', get_celebrities),
    path('contact/developer', send_message),
    path('get-celebrity/<str:celebrityId>', get_celebrity),
    path('get-promo-code/<str:code>', get_promo_code),
    path('active-promo-code/verify', verify_users_promo_code),
    path('upload-celebrity-receipt', upload_celebrity_receipt),
    path('activity-log', get_activity_log)
]