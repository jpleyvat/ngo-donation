from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid

from .managers import UserManager

# Create your models here.
class CustomUser(AbstractUser):
      CHOICES = (
         ('Admin', 'Admin'),
         ('User', 'User'),
      )

      UserID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable = False)
      username = models.CharField(max_length=40, unique=False, default='')    #removing this raises an error when creating a user. This is a required field.
      first_name = models.CharField(_('first name '),max_length = 66, default = '')
      last_name = models.CharField(_('last name'),max_length = 66, default = '')
      email = models.EmailField(_('email address'), unique = True)
      role = models.CharField(max_length = 20, choices = CHOICES)
      is_active = models.BooleanField(_('is active'), default = True)
      date_joined = models.DateTimeField(_('date joined'), auto_now_add = True)
      password = models.CharField(max_length = 60, default = '')


# These fields are optional only require them to be filled out when user is donating for the first time.

      CMA_Num = models.IntegerField(blank = True, null = True,  default = 0)
      Phone = models.CharField(max_length = 12, blank = True, default = '')
      AddressLineOne = models.CharField(max_length = 60, blank = True, null = True, default = '')
      AddressLineTwo = models.CharField(max_length = 60, blank = True, null = True, default = '')
      City = models.CharField(max_length = 60, blank = True, null = True, default = '')
      State = models.CharField(max_length = 60, blank = True, null = True, default = '')
      Zip = models.CharField(max_length = 60, blank = True, null = True, default = '')
      Country = models.CharField(max_length = 60, blank = True,  null = True, default = '')
      Urbanization = models.CharField(max_length = 60, blank = True, null = True, default = '')

      objects = UserManager()
      USERNAME_FIELD = 'email'
      REQUIRED_FIELDS = ['first_name', 'last_name', 'password', 'role']




      def __str__(self):
            return self.email

      class Meta:
            verbose_name = _('user')
            verbose_name_plural = _('users')
            ordering = ['-last_name']


class UserProfile(models.Model):
      user = models.OneToOneField(settings.AUTH_USER_MODEL,related_name = 'Profile', on_delete=models.CASCADE)
      bio = models.TextField(max_length=500, blank=True)
      location = models.CharField(max_length=30, blank=True)
      birth_date = models.DateField(null=True, blank=True)




@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


#fix this
# @receiver(post_save, sender=CustomUser)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()

