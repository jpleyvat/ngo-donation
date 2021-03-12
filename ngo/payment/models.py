from django.db import models
from django.urls import reverse
from ngo.donations.models import DonationType

class Payment(models.Model):
    payment_id = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    donation_type = models.ForeignKey(DonationType,related_name='payments',on_delete=models.CASCADE)

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return self.payment_id

# Create your models here.
