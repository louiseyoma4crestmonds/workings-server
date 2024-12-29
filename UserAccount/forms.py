from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import ApplicationUserAccount

class UserAccountCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta(UserCreationForm):
        model = ApplicationUserAccount
        fields = ('email',)


class UserAccountChangeForm(UserChangeForm):

    class Meta:
        model = ApplicationUserAccount
        fields = (
                  'is_staff',
                  'is_active',
                  'last_name',
                  )
        

