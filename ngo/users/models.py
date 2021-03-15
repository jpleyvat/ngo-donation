from time import time

# Django
import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver


from .managers import UserManager

# Create your models here.
def get_id():
    return int(time())

class Profile(models.Model):
    profile_id = models.IntegerField(primary_key=True, editable=False)
    first_name = models.CharField(max_length = 66, null=True, blank=True)
    last_name = models.CharField(max_length = 66, null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    cma_num = models.IntegerField( null = True, blank=True)
    phone = models.CharField(max_length = 12, null=True, blank=True)
    addressLineOne = models.CharField(max_length = 60,  null = True, blank=True)
    addressLineTwo = models.CharField(max_length = 60,  null = True, blank=True)
    city = models.CharField(max_length = 60,  null = True, blank=True)
    state = models.CharField(max_length = 60,  null = True, blank=True)
    zip_code = models.CharField(max_length = 60,  null = True, blank=True)
    country = models.CharField(max_length = 60,   null = True, blank=True)
    urbanization = models.CharField(max_length = 60,  null = True, blank=True)

    def save(self, *args, **kwargs):
        '''Unique ID'''
        if not self.profile_id:
            self.profile_id = get_id()
        super(Profile, self).save(*args, **kwargs)

    def __str__(self):
        return ' '.join((self.first_name, self.last_name)) if self.first_name and self.last_name else str(self.profile_id)

class CustomUser(AbstractUser):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable = False)
    username = models.CharField(max_length=40, unique=False, default='') 
    email = models.EmailField(_('email address'), unique = True)
    is_staff = models.BooleanField(_('staff status'), default=False, help_text=_('Determines if user can access the admin site'))

    is_active = models.BooleanField(_('is active'), default = True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add = True)
    password = models.CharField(max_length = 60, editable=False, default = '')
    profile = models.OneToOneField(Profile, unique=True, on_delete=models.DO_NOTHING, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password', 'is_staff']

    def __str__(self):
        return self.username

    #gives users with is_staff permissions
    def has_perm(self, perm, obj=None):
        return self.is_staff


   

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        ordering = ['-last_name']

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    '''Creates profile after user creation.'''
    if created:
        profile = Profile.objects.create()
        instance.profile = profile
        instance.save()


#fix this
# @receiver(post_save, sender=CustomUser)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()
