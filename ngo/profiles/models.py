from time import time

# Django.
from django.db import models


from django.apps import apps

# Create your models here.


def get_id():
    """Returns unique ID."""
    return int(time())


class Profile(models.Model):
    profile_id = models.IntegerField(primary_key=True, editable=False)
    first_name = models.CharField(max_length=66, null=True, blank=True)
    last_name = models.CharField(max_length=66, null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    cma_num = models.IntegerField(null=True, blank=True)
    phone = models.CharField(max_length=12, null=True, blank=True)
    addressLineOne = models.CharField(max_length=60, null=True, blank=True)
    addressLineTwo = models.CharField(max_length=60, null=True, blank=True)
    city = models.CharField(max_length=60, null=True, blank=True)
    state = models.CharField(max_length=60, null=True, blank=True)
    zip_code = models.CharField(max_length=60, null=True, blank=True)
    country = models.CharField(max_length=60, null=True, blank=True)
    urbanization = models.CharField(max_length=60, null=True, blank=True)

    def save(self, *args, **kwargs):
        """Unique ID"""
        if not self.profile_id:
            self.profile_id = get_id()

        users = apps.get_model("users", "CustomUser")
        if users.objects.filter(profile=self.profile_id).count() > 0:
            user = users.objects.get(profile=self.profile_id)
            if self.first_name and self.first_name != "":
                user.first_name = self.first_name
            if self.last_name and self.last_name != "":
                user.last_name = self.last_name
            user.save()

        super().save(*args, **kwargs)

    def __str__(self):
        return (
            " ".join((self.first_name, self.last_name))
            if self.first_name and self.last_name
            else str(self.profile_id)
        )
