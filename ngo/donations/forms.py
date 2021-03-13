# Django.
from django import forms

# Extra views.
from extra_views import FormSetView, ModelFormSetView

# Models.
from .models import Donation
from users.models import Profile

# class CreateForm(forms.ModelForm):

#     class meta():
#         model = Donation
#         fiels = '__all__'

# class ProfileForm(FormSetView):
#     form_class = CreateForm
#     template_name = 'donatons/create.html'

# class

# class ProfileForm(ModelFormSetView):
#     model = Profile
#     fields = '__all__'
#     template_name = 'donatons/create.html'

class ProfileForm(forms.ModelForm):

    class Meta():
        model = Profile
        fields = ['city']


class DonationForm(ModelFormSetView):
    model = Donation
    fields = ['amount']
    # template_name = 'item_formset.html'
