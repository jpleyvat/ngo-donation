from time import time

# Django
import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver

from .managers import UserManager

# Create your models here.
def get_id():
    return int(time())

class Profile(models.Model):
    _id = models.IntegerField(primary_key=True, editable=False, default=0)
    first_name = models.CharField(max_length = 66, default = '', blank= True)
    last_name = models.CharField(max_length = 66, default = '', blank= True)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    cma_num = models.IntegerField(blank = True, null = True,  default = 0)
    phone = models.CharField(max_length = 12, blank = True, default = '')
    addressLineOne = models.CharField(max_length = 60, blank = True, null = True, default = '')
    addressLineTwo = models.CharField(max_length = 60, blank = True, null = True, default = '')
    city = models.CharField(max_length = 60, blank = True, null = True, default = '')
    state = models.CharField(max_length = 60, blank = True, null = True, default = '')
    zip_code = models.CharField(max_length = 60, blank = True, null = True, default = '')
    country = models.CharField(max_length = 60, blank = True,  null = True, default = '')
    urbanization = models.CharField(max_length = 60, blank = True, null = True, default = '')

    def save(self, *args, **kwargs):
        '''Unique ID'''
        self._id = get_id()
        super(Profile, self).save(*args, **kwargs)

    def __str__(self):
        return ' '.join((self.first_name, self.last_name))

class CustomUser(AbstractUser):
    _id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable = False)
    username = models.CharField(max_length=40, unique=False, default='')    #removing this raises an error when creating a user. This is a required field.

    email = models.EmailField(_('email address'), unique = True)

    #Change role to boolean is_staff so validations can be made easier
    # role = models.CharField(max_length = 20, choices = CHOICES)
    is_staff = models.BooleanField(_('staff status'), default=False, help_text=_('Determines if user can access the admin site'))

    is_active = models.BooleanField(_('is active'), default = True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add = True)
    password = models.CharField(max_length = 60, default = '')
    profile = models.ForeignKey(Profile, on_delete=models.DO_NOTHING, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password', 'is_staff']

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        ordering = ['-last_name']


# @receiver(post_save, sender=CustomUser)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)


#fix this
# @receiver(post_save, sender=CustomUser)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()
