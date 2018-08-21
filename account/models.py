from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager #BaseUsermanager will help us manage the user model we defined
# so we could add custom user model but hold django authentication https://medium.com/agatha-codes/options-objects-customizing-the-django-user-model-6d42b3e971a4
from django.utils.translation import ugettext_lazy as _ #for verbose

class CustomAccountManager(BaseUserManager):

    def _create_user(self, email, password, **extra_fields):
        '''
        Creates and saves a User with the given email and password
        '''
        if not email:
            raise ValueError('Email must be set')

        email = self.normalize_email(email)  #remove duplicacy and redundancy
        user= self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self,email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self,email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin): #AbstractBaseUser has django's authentication with it
    email = models.EmailField(unique=True) #login through email
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True) #differentiate between admin and non admin
    is_staff= models.BooleanField(default=False)
    REQUIRED_FIELDS = [] #mandatory to create a user
    USERNAME_FIELD = 'email' #this field will be used to identify unique accounts

    objects= CustomAccountManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        '''
        human-readable name for the CustomUser. Instead of CustomUser we have user now. https://docs.djangoproject.com/en/2.1/ref/models/options/#verbose-name
        '''

    def get_full_name(self):
        full_name= '%s %s' %(self.first_name, self.last_name)
        return full_name.strip() #str.strip([chars]) removes character chars from the string and returns the rest of the string. here we strip nothing

    def get_short_name (self):
        return self.first_name


    def __str__ (self):
        return self.email

    def natural_key(self):
        return self.email
