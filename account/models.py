from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    Group)
from django.core.validators import RegexValidator


class UserManager(BaseUserManager):

    def create_superuser(self, name, email, password=None):
        if not name:
            raise ValueError('Users must have a username')
        if not password:
            raise ValueError('Users must set the password')
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            name=name,
            email=UserManager.normalize_email(email),
        )
        user.set_password(password)
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        group = Group.objects.get(name='Mentors')
        user.groups.add(group)
        return user

    def create_user(self, name, email, password=None):
        if not name:
            raise ValueError('Users must have a username')
        if not password:
            raise ValueError('Users must set the password')
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            name=name,
            email=UserManager.normalize_email(email),
        )
        user.set_password(password)
        user.is_admin = False
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    name = models.CharField(max_length=50, blank=False, validators=[RegexValidator(
        regex='^[a-zA-Z ]*$',
        message='name must be Alphabetic only',
        code='invalid_first_name'
    )])
    email = models.EmailField(max_length=100, blank=False, unique=True)
    password = models.CharField(max_length=100)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    groups = models.ManyToManyField(Group)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'password']

    def __str__(self):
        return str(self.name) + " --> " + str(self.email)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
