'''Donations models.'''

# Django
from django.db import models
import ngo 
#User = ngo.settings.AUTH_USER_MODEL

#from django.contrib.auth.models import User

# Create your models here.
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
    _id = models.IntegerField(primary_key=True, auto_created=True, editable=False)
    date = models.DateField(auto_created=True, auto_now=True)
    amount = models.IntegerField(blank=False, null=False)
    _type = models.ForeignKey(DonationType, on_delete=models.CASCADE, blank=False, null=False)
    #current_user = User  
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    # profile = models.ForeignKey()
    # gifts = models.ForeignKey()

    def __str__(self):
        return str(self.date)


    class Meta:
        ordering = ['-date']
