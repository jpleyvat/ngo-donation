'''Donations urls.'''

# Django
from django.urls import path

# Views
from .views import (DonationManagement, 
                    MakeDonation)

app_name = 'donations'

urlpatterns = [
    path('management/', DonationManagement.as_view()),
    path('new/', MakeDonation.as_view())
]
