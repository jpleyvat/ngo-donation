'''Donations models.'''
from time import time

# Django.
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Models.
from users.models import Profile
# Create your models here.
def get_id():
    return int(time())

class Charity(models.Model):
    '''Donation types models.'''
    cause_id = models.IntegerField(primary_key=True, auto_created=True, editable=False)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = _('charity')
        verbose_name_plural = _('charities')


class Donation(models.Model):
    '''Donations models.'''
    donation_id = models.IntegerField(primary_key=True, editable=False, default=0)
    charity = models.ForeignKey(Charity, on_delete=models.CASCADE, blank=False, null=False)
    date = models.DateField(auto_created=True, auto_now=True)
    # user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    amount = models.IntegerField(blank=False, null=False)
    completed = models.BooleanField(default=False,auto_created=True, editable=False)
    # profile = models.ForeignKey()
    profile = models.ForeignKey(Profile, on_delete=models.DO_NOTHING, )
    # gifts = models.ForeignKey()

    def save(self, *args, **kwargs):
        '''Unique ID'''
        if not self.donation_id:
            self.donation_id = get_id()

        super(Donation, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.donation_id)

    class Meta:
        ordering = ['-date']
