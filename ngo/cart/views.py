from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from donations.models import Donation
from cart.cart import Cart
from cart.forms import CartAddDonationForm

@require_POST
def cart_add(request,donation_id):
    cart = Cart(request)
    donation = get_object_or_404(Donation,id=donation_id)
    cart.add(donation=donation)
    form = CartAddDonationForm(request.POST)
    if form.is_valid():

        cd = form.cleaned_data
        cart.add(donation=donation,quantity=cd['quantity'],update_quantity=cd['update'])
    return redirect('cart:cart_detail')

def cart_remove(request,donation_id):
    cart = Cart(request)
    donation = get_object_or_404(Donation,id=donation_id)
    cart.remove(donation)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddDonationForm(initial={'quantity' : item['quantity'], 'update': True})
    cart_products = [item['donation'] for item in cart]
    return render(request,'cart/detail.html', {'cart', cart })

# Create your views here.
