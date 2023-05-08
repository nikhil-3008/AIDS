from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.db import models
# from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
# from django.utils.translation import gettext_lazy as _

# Create your models here.
class AccountManager(BaseUserManager):
    def create_user(self,email,username,password):
        if not email:
            raise ValueError(_("Users must have an email address"))
        if not username:
            raise ValueError(_("Users must have an unique username"))
        email=self.normalize_email(email)
        user=self.model(email=email,username=username)
        user.set_password(password)
        user.save()

    def create_superuser(self,email,username,password,**other_fields):
            other_fields.setdefault('is_staff',True)
            other_fields.setdefault('is_superuser',True)
            other_fields.setdefault('is_active',True)
            if other_fields.get('is_staff') is not True:
                raise ValueError('is_staff is set to False')
            if other_fields.get('is_superuser') is not True:
                raise ValueError('is_superuser is set to False')
            return self.create_user(email,username,password)
    
class account(models.Model):
   email  = models.EmailField(('email address'),max_length=60,unique=True)
   username = models.CharField(max_length=30,unique=True)

   
   def __str__(self):
        return self.username
