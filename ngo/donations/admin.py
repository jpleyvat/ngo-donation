'''Donations admin'''

# Django.
from django.contrib import admin

# Models.
from .models import Donation, Charity 

admin.site.register(Charity)
admin.site.register(Donation)
