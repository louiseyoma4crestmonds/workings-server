from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import ApplicationUserAccount
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from django.contrib.admin.widgets import FilteredSelectMultiple

User = get_user_model()

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
        

class GroupAdminForm(forms.ModelForm):
    class Meta:
        model = Group
        exclude = []

    # Add the users field
    users = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        required=False,
        # Use the pretty 'filter_horizontal widget'
        widget=FilteredSelectMultiple('users', False)
    )

    def __init__(self, *args, **kwargs):
        # Normal for initialization
        super(GroupAdminForm, self).__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['users'].initial = self.instance.user_set.all()

    def save_m2m(self):
        self.instance.user_set.set(self.cleaned_data['users'])

    def save(self, *args, **kwargs):
        # Default save
        instance = super(GroupAdminForm, self).save()
        # Save many-to-many data
        self.save_m2m()
        return instance