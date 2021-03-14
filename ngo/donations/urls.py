'''Donations urls.'''

# Django
from django.urls import path

# Views
from . import views

app_name = 'donations'

urlpatterns = [
    path('', views.ListDonations.as_view(), name='list'),
    path('donate/', views.CreateDonation.as_view(), name='create'),
    # path('donate/', views.CreateDonation.as_view(), name='create'),
    # path('<int:pk>/mock/', views.MockPayment.as_view(), name='mock'),
    path('<int:pk>/mock/', views.mock_payment, name='mock'),
]
