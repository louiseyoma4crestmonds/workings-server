from django.db import models
from django.utils import timezone
from UserAccount.models import ApplicationUserAccount



# Choices for activities
LOG_DETAILS = [
    ('Order Paid Successfully', 'Order Paid Successfully'),
    ('Package is being packed', 'Package is being packed'),
    ('Awaiting Shipment', 'Awaiting Shipment'),
    ('Package Shipped', 'Package Shipped'),
    ('Package Arrived at Airport', 'Package Shipped'),
    ('Package Shipped', 'Package Shipped'),
]

# Create your models here.
class TrackingId(models.Model):
    tracking_id=models.CharField(max_length=12, default="FGSHWEQO", unique=True)
    user=models.ForeignKey(ApplicationUserAccount, on_delete=models.CASCADE)
    longitude = models.CharField(max_length=255, default="0")
    latitude = models.CharField(max_length=255, default="0")

    def __str__(self):
        return self.tracking_id
    
class TrackingIdHistory(models.Model):
    tracking_id=models.ForeignKey(TrackingId, on_delete=models.CASCADE)
    date=models.DateTimeField(default=timezone.now)
    activity=models.TextField()
    activity_status=models.BooleanField(default=False)

    def __str__(self):
        return self.tracking_id.tracking_id + "|" + self.activity