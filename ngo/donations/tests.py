'''Models tests.'''

# Django
from django.test import TestCase

# Models
from .models import (Donation,
                     DonationType)

# Create your tests here.
class DonationTypeTest(TestCase):
    '''Donation type test.'''
    def setUp(self):
        DonationType.objects.create('Dogs')

class DonationTest(TestCase):
    '''Donation test.'''
    def setUp(self):
        Donation.objects.create(ammount=1000, 
                                _type=DonationType.objects.get(name='dogs'))
