"""Donations admin"""

# Django.
from django.contrib import admin

# Models.
from .models import Charity, Donation

admin.site.register(Charity)
admin.site.register(Donation)
