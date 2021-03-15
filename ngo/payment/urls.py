from django.urls import path

from .views import(PaymentManagement,MakePayment)

app_name = 'payment'

urlpatterns = [
    path('payment/',PaymentManagement.as_view()),
    path('new/',MakePayment.as_view())
]