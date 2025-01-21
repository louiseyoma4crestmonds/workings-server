from knox import views as knox_views
from .views import *
from django.urls import path

urlpatterns = [
    path('', home, name='user_account_home'),
    path('logoutall', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('sign-in', sign_in),
    path('register', register),
    path('business-account/request', request_business_account),

    
]