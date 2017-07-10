from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core.validators import RegexValidator
#from .utils import UserManager
from django.utils import timezone
#from .utils import AdminInfo


class AdminInfo(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE)


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
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        AdminInfo.objects.create(user=user)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('E-mail', unique=True)
    created = models.DateTimeField('Creation date', auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email


class TraineeInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    f = models.CharField(max_length=30, verbose_name=u'Фамилия')
    i = models.CharField(max_length=30, verbose_name=u'Имя')
    o = models.CharField(max_length=30, verbose_name=u'Отчество')
    birth_date = models.DateField(verbose_name=u'Дата рождения')
    address = models.CharField(max_length=150, verbose_name=u'Адрес')
    education = models.CharField(max_length=150, verbose_name=u'Образование')

    phone_regex = RegexValidator(regex='^(\+7)|8\d{10}$',
                                 message="Phone number must be entered in the format: '+79001234567' or '89001234567'")
    phone = models.CharField(validators=[phone_regex], max_length=12, verbose_name=u'Телефон')
    dsc = models.TextField(max_length=2000, verbose_name=u'О себе')

    def __str__(self):
        return self.f + ' ' + self.i + ' ' + self.o







