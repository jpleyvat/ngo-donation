from decimal import Decimal
from django.conf import settings
from donations.models import Donation 


class Cart(object):
    def __init__(self,request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def __iter__(self):
        donation_ids = self.cart.keys()
        donations = Donation.objects.filter(id__in=donation_ids)
        for donation in donations:
            self.cart[str(donation.id)]['donation'] = donation 

        for item in self.cart.values():
            item['amount'] = Decimal(item['amount'])
            item['total_price'] = item['amount'] * item['quantity']
            yield item

    def add(self,product,quantity=1,update_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'amount' : str(product.amount)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def remove(self,product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def clear(self):
        self.session[settings.CART_SESSION_ID] = {}
        self.session.modified = True

    


    def get_total_price(self):
        return sum(Decimal(item['amount']) * item['quantity'] for item in self.cart.values())

    