from django.db import models
from django.urls import reverse
from donations.models import DonationType,Donation

class Payment(models.Model):
    payment_id = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    donation_type = models.ForeignKey(DonationType,related_name='donation_type',on_delete=models.CASCADE)
    monthly_recurring = models.BooleanField(default=False)
    donation = models.ForeignKey(Donation,related_name='donation', on_delete=models.CASCADE)

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return self.payment_id



# Create your models here.
