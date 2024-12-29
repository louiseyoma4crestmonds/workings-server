# All global imports for this file goes in this section(all procedures that..
# are used more than once go here)
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from django.utils import timezone
import os
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

##############################################################################............



"""
1.) Replace 'account' with the name of the django application
    that houses the user model.
2.) Replace 'CustomUser' with the name of the user model 
    of the destination application.
"""
from UserAccount.models import ApplicationUserAccount

APPLICATIONS_USER_MODEL = ApplicationUserAccount



"""
Access this function from any application or any where in the django project..
to get a user instance tied to an authentication token.
"""
from knox.models import AuthToken
import string
import random





def generate_random_string(length, expected_string_type):
    string_values = ""
    if expected_string_type == "number":
        string_values = "123456789"

    if expected_string_type=="letters":
        string_values = string.ascii_uppercase

    random_string = ''.join(random.choice(string_values) for i in range(length))
    return (random_string)


def get_token_user(token):
    token_user=""
    try:
        all_tokens=AuthToken.objects.all()
        for each_token in all_tokens:
            if each_token.token_key.startswith(token):
                token_user=APPLICATIONS_USER_MODEL.objects.get(email=each_token.user)
    except ObjectDoesNotExist:
        return ("Invalid Token")
    else:
        return token_user


    
def handle_uploaded_file(file, user_email):
    # Create a directory in media folder named payment_receipts if it doesnt exist
    file_name=user_email + generate_random_string(8, "letters")
    if not os.path.exists(os.path.join(settings.MEDIA_ROOT, 'payment_receipts')):
        os.makedirs(os.path.join(settings.MEDIA_ROOT, "payment_receipts"))

    # Save file to media/ppayment_receipts directory
    image_file = os.path.join(
        settings.MEDIA_ROOT, 'payment_receipts/' + file_name + ".png")
    with open(image_file, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    return (image_file)


def send_email_to_user(email, email_context, email_html_template, email_text_template, subject):
    # send an e-mail to the user
    try:
        context = {
            'email': email,
            'email_context': email_context,
        }

        # render email text
        email_html_message = render_to_string(
            email_html_template, context['email_context'])
        email_plaintext_message = render_to_string(
            email_text_template, context['email_context'])

        msg = EmailMultiAlternatives(
            # title:
            "{title}".format(title=subject),
            # message:
            email_plaintext_message,
            # from:
            "support@thanerivers-management.primarypros.com",
            # to:
            [context['email']]
        )
        msg.attach_alternative(email_html_message, "text/html")
        msg.send()
    except Exception as e:
        print(e)
        return ("error")
    else:
        return ("success")