'''Donations views.'''
# Django
from django.urls import reverse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


from django.forms.models import inlineformset_factory, modelformset_factory


# Django REST Framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer

# Extra views.
from extra_views import CreateWithInlinesView, UpdateWithInlinesView, InlineFormSetFactory, NamedFormsetsMixin

# Models
from .models import Donation
from users.models import Profile, CustomUser

# Forms
from .forms import ProfileForm, DonationForm
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

class DonationInline(InlineFormSetFactory):
    model = Donation
    # formset_kwargs = {'form_kwargs': {'initial': {'amount': 1000}}}
    factory_kwargs = {'extra': 1, 'max_num': 1,
                      'can_order': False, 'can_delete': False}

    fields = ['amount', 'charity']
    exclude = ['DELETE']

    def get_formset_kwargs(self):
        kwargs = super(DonationInline, self).get_formset_kwargs()
        # modify kwargs here
        print(kwargs)
        return kwargs

    def get_factory_kwargs(self):
        kwargs = super(DonationInline, self).get_factory_kwargs()
        # modify kwargs here
        return kwargs

class CreateDonation(LoginRequiredMixin, NamedFormsetsMixin, CreateWithInlinesView):
    '''Creates new donation'''
    # model = Donation
    # inlines = [ProfileInline]
    # fields = '__all__'
    # template_name = 'donations/create.html'
    # success_url = reverse_lazy('donations:mock', kwargs={'pk': })
    model = Profile
    inlines = [DonationInline]
    inlines_names = ['Donation', ]
    template_name = 'donations/create.html'
    form_class = ProfileForm


    # def get_context_data(self, **kwargs):
    #     for inline in self.inlines:
    #         print(dir(inline))
    #     context =  super().get_context_data(**kwargs)
    #     print(self.request.user)
    #     return context

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
