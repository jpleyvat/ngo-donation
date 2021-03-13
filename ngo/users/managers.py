from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _

                                                                                                                                                                                                                                
class UserManager(BaseUserManager):  
    # This custom user model uses email an in unique identifier rather than an email for authentication
    def create_user(self,UserID,email, password=None):
        # create and save user
        if not email:
            raise ValueError(_('The Email must be set'))
        if not UserID:
            raise ValueError("Users must have an UserID")
        user = self.model(
            email = self.normalize_email(email)
        )
        user.UserID = UserID
        user.is_admin = False
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, UserID, email, password):
        user = self.create_user(
            UserID,email,password=password 
        )
        user.is_admin = True
        user.save(using=self._db)
        return user 

        
