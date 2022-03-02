"""
Provides model for Account
"""
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from group.models import Group

__author__ = "Jakupov Dias, Edward Calonghi (edited slightly)"

def validate_email(email):
    """Validates that email is in valid format (University email)"""
    host = "@exeter.ac.uk"
    if host not in email:
        raise ValidationError(
            _('Use your student email -- %(host)s'),
            params={'host': host},
        )

class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have username")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    email                   = models.EmailField(verbose_name="email", max_length=60, unique=True, validators=[validate_email])
    username                = models.CharField(max_length=30, unique=True)
    is_gameKeeper           = models.BooleanField(default=False)
    date_joined             = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login              = models.DateTimeField(verbose_name='last login', auto_now_add=True)
    is_admin                = models.BooleanField(default=False)
    is_active               = models.BooleanField(default=True)
    is_staff                = models.BooleanField(default=False)
    is_superuser            = models.BooleanField(default=False)
    is_inTeam               = models.BooleanField(default=False)
    latitude 				= models.DecimalField(max_digits=20, decimal_places=15, default = 0, null=True, blank=True)
    longitude 				= models.DecimalField(max_digits=20, decimal_places=15, default = 0, null=True, blank=True)
    score                   = models.DecimalField(max_digits=7,decimal_places=0, default=0)
    belongs_to_group        = models.ForeignKey(Group, null=True, on_delete=models.SET_NULL)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True

    