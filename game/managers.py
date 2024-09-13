# game/managers.py
from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, fullname, mobile, city, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        if not mobile:
            raise ValueError('The Mobile Number must be set')

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            username=username,
            fullname=fullname,
            mobile=mobile,
            city=city,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, fullname, mobile, city, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, username, fullname, mobile, city, password, **extra_fields)
