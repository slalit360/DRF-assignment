from django.contrib.auth.base_user import BaseUserManager


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
            email=self.normalize_email(email),
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
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.is_admin = False
        user.is_staff = True
        user.save(using=self._db)
        return user

