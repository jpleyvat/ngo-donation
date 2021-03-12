'''Donations models.'''
from time import time

# Django
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
def get_id():
    return int(time())
class DonationType(models.Model):
    '''Donation types models.'''
    _id = models.IntegerField(primary_key=True, auto_created=True, editable=False)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Donation(models.Model):
    '''Donations models.'''
    _id = models.IntegerField(primary_key=True, editable=False, default=0)
    _type = models.ForeignKey(DonationType, on_delete=models.CASCADE, blank=False, null=False)
    date = models.DateField(auto_created=True, auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField(blank=False, null=False)
    completed = models.BooleanField(default=False,auto_created=True, editable=False)
    # profile = models.ForeignKey()
    # gifts = models.ForeignKey()

    def save(self, *args, **kwargs):
        '''Unique ID'''
        self._id = get_id()
        super(Donation, self).save(*args, **kwargs)

    def __str__(self):
        return str(self._id)

    class Meta:
        ordering = ['-date']
