'''Donations views.'''

# Django
from django.urls import reverse
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

# Django REST Framework
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.decorators import api_view, renderer_classes

# Extra views.
from extra_views import CreateWithInlinesView, InlineFormSetFactory

# Models
from users.models import Profile
from .models import Donation

# Forms
from .forms import ProfileForm

# Create your views here.
class ListDonations(LoginRequiredMixin, ListView):
    '''List donations view'''
    model = Donation
    template_name = 'donations/list.html'

    def get_context_data(self, **kwargs):
        
        user = self.request.user
        context = super().get_context_data(**kwargs)
        if self.request.get_full_path() == '/donations/mydonations/':
            donations = Donation.objects.filter(profile=user.profile.profile_id)
        elif self.request.get_full_path() == '/donations/':
            donations = Donation.objects.all()\
                if user.is_staff\
                else Donation.objects.filter(profile=user.profile.profile_id)

        context['donations'] = donations
        return context

class DonationInline(InlineFormSetFactory):
    '''Donation Inline.'''
    model = Donation
    fields = '__all__'
    formset_kwargs = {'form_kwargs': {}}
    factory_kwargs = {'extra': 1, 'max_num': 1,
                      'can_order': False, 'can_delete': False,}

    def get_formset_kwargs(self):
        '''Brings pending donation.'''
        kwargs = super().get_formset_kwargs()

        define_user_and_profile(self)

        if self.profile:
            donations = Donation.objects\
                .filter(profile = self.profile.profile_id)\
                .filter(completed=False)

            #Modifies kwargs if pending donation.
            if donations:
                kwargs['form_kwargs'].update({'instance': donations[0]})

        return kwargs

class CreateDonation(CreateWithInlinesView):
    '''Creates new donation'''

    model = Profile
    inlines = [DonationInline]
    template_name = 'donations/create.html'
    form_class = ProfileForm

    def get_form(self, form_class=None):
        """Return an instance of the form to be used in this view."""

        define_user_and_profile(self)

        if form_class is None:
            form_class = self.get_form_class()
        # Brings user profile.
        kwargs = self.get_form_kwargs()
        kwargs.update({'instance': self.profile})
        return form_class(**kwargs)

    def get_success_url(self):
        '''Sends to payment'''
        return reverse('donations:mock', args=(self.profile.profile_id, ))

@api_view(['GET'])
@renderer_classes([TemplateHTMLRenderer])
def mock_payment(request, **kwargs):
    '''Mock payment.'''
    complete_donation(kwargs['pk'])
    return Response({'status': '200'}, template_name='donations/mock.html')

def define_user_and_profile(instance):
    '''Defines user and profile.'''
    instance.user = instance.request.user
    if instance.user.profile:
        instance.profile = instance.user.profile

def complete_donation(primary_key):
    '''Completes a donation'''
    import ipdb
    ipdb.set_trace()
    profile_id = primary_key
    donation = Donation.objects.filter(profile=profile_id).get(completed=False)
    donation.completed = True
    donation.save()
