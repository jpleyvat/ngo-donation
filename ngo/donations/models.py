'''Donations models.'''
from time import time

# Django.
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Models.
from users.models import Profile
# Create your models here.
def get_id():
    '''Returns unique ID.'''
    return int(time())

class Charity(models.Model):
    '''Donation types models.'''
    charity_id = models.IntegerField(primary_key=True, auto_created=True, editable=False)
    name = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    donations = models.ManyToManyField('Donation', related_name='+', blank=True)

    def save(self, *args, **kwargs):
        '''Sets unique ID'''
        if not self.charity_id:
            self.charity_id = get_id()

        super().save(*args, **kwargs)

    @property
    def raised(self):
        raised = 0
        for donation in self.donations.all():
            raised += donation.amount
        return raised

    def __str__(self):
        return str(self.name)

    class Meta:
        '''Meta class.'''
        ordering = ['name']
        verbose_name = _('charity')
        verbose_name_plural = _('charities')


class Donation(models.Model):
    '''Donations models.'''
    donation_id = models.IntegerField(primary_key=True, editable=False, default=0)
    charity = models.ForeignKey(Charity, on_delete=models.DO_NOTHING)
    date = models.DateField(auto_created=True, auto_now=True)
    amount = models.IntegerField(blank=False, null=False)
    completed = models.BooleanField(default=False,auto_created=True,editable=False)
    profile = models.ForeignKey(Profile, on_delete=models.DO_NOTHING, )
    # gifts = models.ForeignKey()

    def save(self, *args, **kwargs):
        '''Sets unique ID'''
        if not self.donation_id:
            self.donation_id = get_id()

        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.donation_id)

    class Meta:
        '''Meta class.'''
        ordering = ['-date']
