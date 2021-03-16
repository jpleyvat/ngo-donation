from decimal import Decimal 
from django.conf import settings 
from django.core.urlresolvers import reverse 
from django.shortcuts import render,get_object_or_404
from paypal.standard.forms import PayPalPaymentsForm

from .models import Payment
from donations.models import Donation,Charity 
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def payment_done(request):
    return render(request,'payment/done.html')

@csrf_exempt
def payment_canceled(request):
    return render(request,'payment/canceled.html')


def payment_process(request):
    
    charity_id = request.session.get('charity_id')
    charity_obj = get_object_or_404(Charity,id=charity_id)
    host = request.get_host()
    donations_inside_charity = charity_obj.donations.all()
    for o in donations_inside_charity:
        if o.completed == False:
            paypal_dict = {
                'business': settings.PAYPAL_RECEIVER_EMAIL,
                'amount': '%.2f' % Decimal(o.amount),
                'item_name': 'Order {}'.format(donations_inside_charity),
                'invoice': str(o.donation_id), 
                'currency_code': 'USD',
                'notify_url': 'http://{}{}'.format(host,reverse('paypal-ipn')),
                'return_url': 'http://{}{}'.format(host,reverse('payment:done')),
                'cancel_return': 'http://{}{}'.format(host,reverse('payment:canceled')),
            }
        form = PayPalPaymentsForm(initial=paypal_dict)
        return render(request, 'payment/process.html',{'charity':charity_obj, 'form':form})

  




