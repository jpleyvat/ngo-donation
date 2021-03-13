'''Donations admin'''

# Django.
from django.contrib import admin

# Models.
from .models import Charity, Donation

# Register your models here.
admin.site.register(Charity)
admin.site.register(Donation)
