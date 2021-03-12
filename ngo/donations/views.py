'''Donations views.'''
# Django
from django.urls import reverse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Django REST Framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer

# Models
from .models import Donation

# Create your views here.

class ListDonations(LoginRequiredMixin, ListView):
    '''List donations view'''
    model = Donation
    template_name = 'donations/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        donations = Donation.objects.all()\
            if user.is_staff\
            else Donation.objects.filter(pk=user._id)

        context['donations'] = donations
        return context

class CreateDonation(LoginRequiredMixin, CreateView):
    '''Creates new donation'''
    model = Donation
    fields = '__all__'
    template_name = 'donations/create.html'
    # success_url = reverse_lazy('donations:mock', kwargs={'pk': })

    def get_success_url(self):
        return reverse('donations:mock', args=(self.object._id, ))

class MockPayment(APIView):
    '''Mock payment.'''
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'donations/mock.html'

    def get(self, request, **kwargs):
        donation = Donation.objects.get(pk=kwargs['pk'])
        donation.completed = True
        donation.save()
        return Response({'status': '200'})
