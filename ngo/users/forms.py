from django import forms
from .models import CustomUser, Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#Extend the UserCreationForm
class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            'first_name',
            'last_name',
            'email',
            'password',
            'is_staff',
        ]


class UpdateCustomUserForm(forms.ModelForm):
    #first_name = forms.CharField()
    #last_name = forms.CharField()
    #email = forms.EmailField()
    #Password = forms.CharField()


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'bio',
            'location',
            'birth_date',
            'cma_num',
            'phone',
            'addressLineOne',
            'addressLineTwo',
            'city',
            'state',
            'zip_code',
            'country',
            'urbanization',
        ]


class UpdateProfile(forms.ModelForm):
    bio = forms.CharField()
    location = forms.CharField()
    birth_date = forms.DateField()
    cma_num = forms.IntegerField()
    phone = forms.CharField()
    addressLineOne = forms.CharField()
    addressLineTwo = forms.CharField()
    city = forms.CharField()
    state = forms.CharField()
    zip_code = forms.CharField()
    country = forms.CharField()
    urbanization = forms.CharField()
