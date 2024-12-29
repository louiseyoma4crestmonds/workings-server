from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Celebrities)
admin.site.register(PromoCode)
admin.site.register(ActivityLog)
admin.site.register(Message)