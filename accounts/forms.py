from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

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


class SignupForm(forms.Form):
    address1 = forms.CharField()
    address2 = forms.CharField()
    town = forms.CharField()
    county = forms.CharField()
    postcode = forms.CharField()
    country = forms.CharField()

    def signup(self, request, user):
        user.subscription = self.cleaned_data['subscription']
        user.address1 = self.cleaned_data['address1']
        user.address2 = self.cleaned_data['address2']
        user.town = self.cleaned_data['town']
        user.county = self.cleaned_data['county']
        user.postcode = self.cleaned_data['postcode']
        user.country = self.cleaned_data['country']
        user.save()
