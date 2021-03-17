'''Models tests.'''

# Django
from django.test import TestCase

# Models
from .models import  (Donation,Charity)

class CharityTest(TestCase):
    def setUp(self):
        DonationType.objects.create('Dogs')
        
class DonationTest(TestCase):
    '''Donation test.'''
    def setUp(self):
        Donation.objects.create(amount=30, 
                                _type=Charity.objects.get(name='dogs'))
