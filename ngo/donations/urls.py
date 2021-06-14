"""Donations urls."""

# Django
from django.urls import path

# Views
from . import views

app_name = "donations"

urlpatterns = [
    path("", views.ListDonations.as_view(), name="list"),
    path("charities/", views.ListCharities.as_view(), name="list_charities"),
    path("charities/create", views.CreateCharity.as_view(), name="create_charity"),
    path("mydonations/", views.ListDonations.as_view(), name="list_my_donations"),
    path("donate/", views.CreateDonation.as_view(), name="create"),
    path("<int:pk>/mock/", views.mock_payment, name="mock"),
]
