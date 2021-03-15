# Django.
from django import forms

# Models.
from users.models import Profile
from .forms import Donation 


class ProfileForm(forms.ModelForm):
    '''Profile form.'''

    class Meta():
        '''Meta Class'''
        model = Profile
        fields = '__all__'
        exclude = ['bio']

class DonationForm(forms.ModelForm):
    class Meta():
        model = Donation