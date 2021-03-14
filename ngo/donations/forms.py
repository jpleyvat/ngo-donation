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
        fields = '__all__'
        exclude = ['bio']

    # def __init__(self, *args, **kwargs):
    #     exclude = kwargs.pop('exclude', [])
    #     initial = kwargs.pop('initial', [])
    #     print(kwargs)
    #     super(ProfileForm, self).__init__(*args, **kwargs)
    #     # if not first_name_check:
    #     for _ in exclude:
    #         del self.fields[_]
    #     # for _ in exclude:
    #     #     del self.fields[_]
    #         # del self.fields['first_name']


class DonationForm(ModelFormSetView):
    model = Donation
    fields = ['amount']
    # template_name = 'item_formset.html'
