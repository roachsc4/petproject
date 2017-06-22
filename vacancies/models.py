from django.db import models
from django.utils import timezone
from users.models import User
from specs.models import Spec


class Vacancy(models.Model):
    FULL_TIME = 1
    PART_TIME = 2
    PROJECT = 3
    TYPE_CHOICES = ((FULL_TIME, 'Full time'),
                    (PART_TIME, 'Part time'),
                    (PROJECT, 'Single project'))

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trainee = models.ManyToManyField(User, through='TraineeVacancy', related_name='trainees')
    spec = models.ManyToManyField(Spec)

    name = models.CharField(max_length=50)
    dsc = models.TextField(max_length=2000)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    address = models.CharField(max_length=200)
    type = models.SmallIntegerField(choices=TYPE_CHOICES)
    is_remote = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class TraineeVacancy(models.Model):
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
    trainee = models.ForeignKey(User, on_delete=models.CASCADE)
    reg_date = models.DateTimeField(auto_now_add=True)



