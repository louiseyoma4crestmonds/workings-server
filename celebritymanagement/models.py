from django.db import models
from UserAccount.models import ApplicationUserAccount

# Create your models here.

class Celebrities(models.Model):
    name=models.CharField(max_length=32, default="Thane Rivers")
    photo=models.CharField(max_length=255, default="http://google.com")
    description=models.TextField()

    def __str__(self):
        return self.name
    

class PromoCode(models.Model):
    name=models.CharField(max_length=8, default="FGSHWEQO", unique=True)
    user=models.ForeignKey(ApplicationUserAccount, on_delete=models.CASCADE)
    cost=models.IntegerField(default=199)
    active=models.BooleanField(default=False)
    balance=models.IntegerField(default=199)

    def __str__(self):
        return self.name
    
class ActivityLog(models.Model):
    name=models.CharField(max_length=255, default="")
    user=models.ForeignKey(ApplicationUserAccount, on_delete=models.CASCADE)
    status=models.CharField(default="pending", max_length=255, blank=False)
    file_path=models.CharField(max_length=255, default="")

    def __str__(self):
        return str(self.user.email) + "|"+ self.name
    

class Message(models.Model):
    name=models.CharField(max_length=64, default="Thane Rivers")
    email=models.CharField(max_length=255, default="http://google.com")
    message=models.TextField()

    def __str__(self):
        return self.name