from django.db import models
from django.contrib.auth.models import AbstractBaseUser, Group, AbstractUser
from django.core.validators import RegexValidator, EmailValidator

from account.manager import UserManager


class User(AbstractBaseUser):
    name = models.CharField(max_length=50, validators=[RegexValidator(
        regex='^[a-zA-Z ]*$',
        message='name must be alphabetic only',
        code='invalid_name'
    )])
    email = models.EmailField(max_length=100, unique=True, validators=[EmailValidator(
        message='invalid email entered',
        code='invalid_email'
    )])
    password = models.CharField(max_length=50, validators=[RegexValidator(
        regex='^(?=.*[a-zA-Z]){8,}(?=.*\d.*\d)(?=.*[$@#!*?&].*[$@#!*?&])[A-Za-z\d$@#!*?&]{12,}$',
        message='Password should contain minimum 8 letters, 2 numbers and 2 special chars',
        code='invalid_password'
    )])
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    groups = models.ManyToManyField(Group)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'password']

    def __str__(self):
        return str(self.name)

    def is_mentor(self):
        if self.groups.filter(name='Mentors').exists():
            return True
        return False

    def is_user(self):
        if self.groups.filter(name='Users').exists():
            return True
        return False

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
