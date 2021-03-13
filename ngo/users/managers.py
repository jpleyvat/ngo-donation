from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _

                                                                                                                                                                                                                                
class UserManager(BaseUserManager):  
    # This custom user model uses email an in unique identifier rather than an email for authentication
    def create_user(self,username,email,first_name,last_name,password=None):
        # create and save user
        if not email:
            raise ValueError(_('The Email must be set'))
        if not username:
            raise ValueError("Users must have an username")
        user = self.model(
            email = self.normalize_email(email)
        )
        user.username = username
        user.first_name = first_name
        user.last_name = last_name 
        user.is_admin = False
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email,first_name,last_name,password):
        user = self.create_user(
            username,email,first_name,last_name,password=password 
        )
        user.is_admin = True
        user.save(using=self._db)
        return user 

        
