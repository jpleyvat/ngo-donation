from django.db import models

# Create your models here.

from django.db import models
import UUID

# Create your models here.
class User(models.Model):
      ADMIN = 'Admin'
      USER = 'Users'

      USER_CHOICES = (
          (ADMIN, 'Admin'),
          (USER, 'Users'),
      )
      UserID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable = False)
      First_Name = models.CharField(max_length = 66, default = '')
      Last_Name = models.CharField(max_length = 66, default = '')
      Email = models.EmailField(max_length= 60)
      Password = models.CharField(max_length = 60, default = '')

# These fields are optional only require them to be filled out when user is donating for the first time.

      CMA_Num = models.IntegerField(max_length = 80, blank = True, null = True,  default = '')
      Phone = models.CharField(max_length = 12, blank = True, default = '')
      AddressLineOne = models.CharField(max_length = 60, Blank = True, null = True, default = '')
      AddressLineTwo = models.CharField(max_length = 60, Blank = True, null = True, Default = '')
      City = models.CharField(max_length = 60, Blank = True, null = True, Default = '')
      State = models.CharField(max_length = 60, Blank = True, null = True, Default = '')
      Zip = models.CharField(max_length = 60, blank = True, null = True, Default = '')
      Country = models.CharField(max_length = 60, blank = True,  null = True, Default = '')
      Urbanization = models.CharField(max_length = 60, blank = True, null = True, Default = '')
