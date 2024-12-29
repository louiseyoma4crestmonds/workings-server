
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings as conf_settings
from knox.models import AuthToken

import environ

# Initialise environment variables
ENV = environ.Env()
environ.Env.read_env()
    
"""
    Catch users post_save signal so that every user will have
    an automtically generated token that can be used for their initial login.
"""


@receiver(post_save, sender=conf_settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance, created=False, **kwargs):
    if created:
        # send an e-mail to the user
        password = "8iu7*IU&"
        instance.set_password(password)
        instance.save()
        AuthToken.objects.create(instance)
        context = {
            'user_email': instance.email,
            'user_password': password,
            'user_firstname': instance.first_name,
            'tenant_name': "instance.tenant.name",
        }
        # render email text

        

