from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .forms import GroupAdminForm
from .forms import UserAccountCreationForm, UserAccountChangeForm
from .models import ApplicationUserAccount

# Register your models here..

# Unregister the original Group admin.
admin.site.unregister(Group)

class GroupAdmin(admin.ModelAdmin):
    # Use our custom form.
    form = GroupAdminForm
    # Filter permissions horizontal as well.
    filter_horizontal = ['permissions']

# Register the new Group ModelAdmin.
admin.site.register(Group, GroupAdmin)



class UserAccountAdmin(UserAdmin):
    add_form = UserAccountCreationForm
    form = UserAccountChangeForm
    model = ApplicationUserAccount
    list_display = ( "email",)
    list_filter = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'last_name', 'first_name', 'country')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', )}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(ApplicationUserAccount, UserAccountAdmin)