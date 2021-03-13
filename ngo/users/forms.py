from django import forms
from .models import CustomUser,Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#Extend the UserCreationForm
class CustomUserForm(forms.ModelForm):
    # first_name = forms.CharField(max_length = 66, required=False, help_text='Optional.')
    # last_name = forms.CharField(max_length = 66, required=False, help_text='Optional.')
    # email = forms.EmailField(max_length = 66, help_text='Required. Enter a valid email.')
    # role = forms.CharField(max_length = 20, required=True,  help_text='Required. Choose a role.')
    # password = forms.CharField(max_length = 66, required=True, help_text = 'Required. Enter a password.')

    class Meta:
        model = CustomUser
        fields = '__all__'


class UpdateCustomUserForm(forms.ModelForm):
    #first_name = forms.CharField()
    #last_name = forms.CharField()
    #email = forms.EmailField()
    #Password = forms.CharField()

    # Ask user before allowing them to update these fields
    CMA_Num = forms.IntegerField()
    Phone = forms.CharField()
    AddressLineOne = forms.CharField()
    AddressLineTwo = forms.CharField()
    City = forms.CharField()
    State = forms.CharField()
    Zip = forms.CharField()
    Country = forms.CharField()
    Urbanization = forms.CharField()
