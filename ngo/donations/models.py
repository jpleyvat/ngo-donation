'''Donations models.'''

# Django
from django.db import models

# Create your models here.
class DonationType(models.Model):
    '''Donation types models.'''
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ['name']

class Donation(models.Model):
    '''Donations models.'''
    _id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=40, default='Anonym')
    date = models.DateField(auto_created=True, auto_now=True)
    amount = models.IntegerField()
    _type = models.ForeignKey(DonationType, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date']
