'''Donations admin'''

# Django.
from django.contrib import admin

# Models.
from .models import DonationType, Donation

# Register your models here.
admin.register(DonationType)
admin.register(Donation)
