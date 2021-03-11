'''Donations views.'''
# Django
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Django REST Framework
from rest_framework.views import APIView

# Models
from .models import Donation

# Create your views here.

class DonationManagement(LoginRequiredMixin, ListView):
    '''List donations view'''
    model = Donation
    template_name = 'donations/management.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        donations = Donation.objects.all()\
            if user.is_staff\
            else Donation.objects.filter(pk=user._id)

        context['donations'] = donations
        return context

class MakeDonation(LoginRequiredMixin, CreateView):
    model = Donation
    fields = ['ammount']
