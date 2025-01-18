from .views import *
from django.urls import path

urlpatterns = [
    path('is-trackingId-valid/<str:tracking_id>', validate_tracking_id),
    path('get/<str:tracking_id>', get_tracking_id),
    path('<str:tracking_id>/history', get_tracking_id_history),

]