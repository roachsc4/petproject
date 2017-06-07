from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone
from django.core.validators import RegexValidator


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('E-mail', unique=True)
    created_date = models.DateTimeField('Creation date')
    is_admin = models.BooleanField()

    objects = UserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'

    def get_full_name(self):
        return self.email

    def get_full_name(self):
        return self.email


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            created_date=timezone.now(),
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


class TraineeInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    f = models.CharField(max_length=30)
    i = models.CharField(max_length=30)
    o = models.CharField(max_length=30)
    birth_date = models.DateField()
    address = models.CharField(max_length=150)
    education = models.CharField(max_length=150)

    phone_regex = RegexValidator(regex='^(\+7)|8\d{10}$',
                                 message="Phone number must be entered in the format: '+79001234567' or '89001234567'")
    phone = models.CharField(validators=[phone_regex])
    dsc = models.TextField(max_length=2000)

    def __str__(self):
        return self.f + ' ' + self.i + ' ' + self.o







