'''Donations admin'''

# Django.
from django.contrib import admin

# Models.
from .models import Donation

admin.site.register(Donation)
