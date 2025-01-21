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
    

class ConsignmentUser(models.Model):
    user=models.ForeignKey(ApplicationUserAccount, on_delete=models.CASCADE)
    date=models.DateTimeField(default=timezone.now)
    secreteQuestion=models.TextField()
    secreteAnswer=models.TextField()
    address1=models.TextField()
    address2=models.TextField()
    company=models.CharField(default="GlobeGoExpress", max_length=255)
    country=models.CharField(default="Japan", max_length=255)
    postal_code=models.CharField(default="232323", max_length=255)
    province=models.CharField(default="MIT", max_length=255)
    phone=models.CharField(default="+1234567890", max_length=255)
    city=models.CharField(default="New Jersey", max_length=255)
    terms=models.BooleanField(default=True)

    def __str__(self):
        return str(self.user.email)

class BusinessAccount(models.Model):
    email=models.EmailField(default="admin@globegoexpress.com", max_length=255)
    first_name=models.CharField(default="GlobeGoExpress", max_length=255)
    last_name=models.CharField(default="GlobeGoExpress", max_length=255)
    address=models.TextField()
    message=models.TextField()
    company=models.CharField(default="GlobeGoExpress", max_length=255)
    country=models.CharField(default="Japan", max_length=255)
    postal_code=models.CharField(default="232323", max_length=255)
    vat=models.CharField(default="MIT", max_length=255)
    phone=models.CharField(default="+1234567890", max_length=255)
    city=models.CharField(default="New Jersey", max_length=255)
    terms=models.BooleanField(default=True)

    def __str__(self):
        return str(self.email)
