from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework.views import APIView
from .models import Payment
class PaymentManagement(LoginRequiredMixin,ListView):
    model = Payment
    template_name = 'donations/payment.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        payments = Payment.objects.all()
        if(user.is_staff()):
            print("something happened")
        else:
            xyz = Payment.objects.filter.filter(pk=user._id)
            print(xyz)

        context['payments'] = payments
        return context

class MakePayment(LoginRequiredMixin,CreateView):
    model = Payment
    fields = ['payment_id']
# Create your views here.
