'''Donations admin'''

# Django.
from django.contrib import admin

# Models.
from .models import DonationType, Donation

# Register your models here.
admin.site.register(DonationType)
admin.site.register(Donation)
