from django.contrib.auth.models import BaseUserManager
from django.utils import timezone
from django.db import models
from .models import User

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )
        user.is_admin = False
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email=email,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        AdminInfo.objects.create(user=user)
        return user


class AdminInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)



