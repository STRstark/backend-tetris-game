from enum import unique

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=225, unique=True)
    phone_number = models.CharField(max_length=11, unique=True)
    full_name = models.CharField(max_length=100)
    study_field = models.CharField(max_length=50)
    student_id = models.CharField(max_length=11, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['email', 'full_name', 'study_field', 'student_id']

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        return self.is_admin


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    point = models.PositiveIntegerField(default=0)


    class Meta:
        ordering = ['-point', ]

    def __str__(self):
        return f"{self.user} >> {self.point}"