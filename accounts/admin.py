from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

from profiles.models import UserProfile


class ProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'User Profile'
    fk_name = 'user'


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        'email',
        'username',
        'account_type',
        'is_staff',
    ]
    fieldsets = UserAdmin.fieldsets + (
        (None, {
            "fields": (
                'account_type',
            ),
        }),
    )
    add_fieldsets = UserAdmin.fieldsets

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.register(CustomUser, CustomUserAdmin)
