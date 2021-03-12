from django.db import models

ROLE_CHOICES = (('admin','ADMIN'),('user','USER'))
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
class UserManager(BaseUserManager):
    def create_user(self,UserID,email,password=None,is_admin=False):
        if not UserID:
            raise ValueError("Users must have an UserID")
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            UserID = UserID,
            email = self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self,UserID,email,password):
        user = self.create_user(
            UserID=UserID,
            email=email,
            password=password,
            is_admin=True
        )
        user.admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    UserID = models.CharField(max_length = 255,unique = True,)
    admin = models.BooleanField(default=False) # a superuser
    email = models.EmailField(max_length=255,unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'UserID'
    REQUIRED_FIELDS = []


    

    def get_full_id(self):
        return self.UserID

    def __str__(self):
        return self.UserID

    @property
    def is_admin(self):
        return self.admin
    objects = UserManager()






# Create your models here.
