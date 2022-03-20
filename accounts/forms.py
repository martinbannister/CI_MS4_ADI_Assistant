from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + (
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
                                                )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields
