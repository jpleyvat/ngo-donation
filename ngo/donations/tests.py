'''Models tests.'''

# Django
from django.test import TestCase

# Models
from .models import (Charity, 
                     Donation)

# Create your tests here.
class CharityTest(TestCase):
    '''Donation type test.'''
    def setUp(self):
        Charity.objects.create('Dogs')

class DonationTest(TestCase):
    '''Donation test.'''
    def setUp(self):
        Donation.objects.create(ammount=1000, 
                                _type=Charity.objects.get(name='dogs'))
