import uuid

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver

from .managers import UserManager

# Create your models here.
class Profile(models.Model):
    _id = models.IntegerField(primary_key=True, editable=False, default=0)
    cma_num = models.IntegerField(blank = True, null = True,  default = 0)
    phone = models.CharField(max_length = 12, blank = True, default = '')
    email = models.CharField(max_length = 60 , blank = True , null=True,default='')
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
        return str(self._id)

class CustomUser(AbstractUser):
    username = models.CharField(max_length=40, unique=False, default='')    #removing this raises an error when creating a user. This is a required field.
    first_name = models.CharField(_('first name '),max_length = 66, default = '')
    last_name = models.CharField(_('last name'),max_length = 66, default = '')
    email = models.EmailField(_('email address'), unique = True)

    #Change role to boolean is_staff so validations can be made easier
    # role = models.CharField(max_length = 20, choices = CHOICES)
    is_admin = models.BooleanField(_('admin status'), default=False, help_text=_('Determines if user can access the admin site'))
    date_joined = models.DateTimeField(_('date joined'), auto_now_add = True)
    password = models.CharField(max_length = 60, default = '')
    profile = models.ForeignKey(Profile, on_delete=models.DO_NOTHING, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','first_name', 'last_name', 'is_admin']

    def __str__(self):
        return self.username

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
