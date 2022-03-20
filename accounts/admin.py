from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        'email',
        'username',
        'subscription',
        'sub_duration',
        'sub_start_date',
        'sub_end_date',
        'address1',
        'address2',
        'town',
        'county',
        'postcode',
        'country',
        'is_staff',
    ]
    fieldsets = UserAdmin.fieldsets + (
        (None, {
            "fields": (
                'subscription',
                'sub_duration',
                'sub_start_date',
                'sub_end_date',
                'address1',
                'address2',
                'town',
                'county',
                'postcode',
                'country',
            ),
        }),
    )
    add_fieldsets = UserAdmin.fieldsets + (
        (None, {
            "fields": (
                'subscription',
                'sub_duration',
                'sub_start_date',
                'sub_end_date',
                'address1',
                'address2',
                'town',
                'county',
                'postcode',
                'country',
            ),
        }),
    )
    

admin.site.register(CustomUser, CustomUserAdmin)
