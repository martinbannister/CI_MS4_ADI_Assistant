from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + (
                                                 'account_type',
                                                )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields


# class SignupForm(forms.Form):
#     account_type = forms.CharField()

#     def signup(self, request, user):
#         user.account_type = self.cleaned_data['account_type']
#         user.save()
