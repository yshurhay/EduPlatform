from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=50, blank=True)
    last_name = models.CharField(_('last name'), max_length=50, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Student(models.Model):
    rating = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ],
        verbose_name='Рейтинг'
    )
    user = models.OneToOneField(to=CustomUser, on_delete=models.CASCADE, verbose_name='Пользователь')

    class Meta:
        verbose_name = "Студенты"
        verbose_name_plural = "Студенты"
        ordering = ['id']

    def __str__(self):
        return f'Student - {self.user}'


class Teacher(models.Model):
    user = models.OneToOneField(to=CustomUser, on_delete=models.CASCADE, verbose_name='Пользователь')
    specializations = models.ManyToManyField(to='courses.Specialization', verbose_name='Специализации')

    class Meta:
        verbose_name = "Преподаватели"
        verbose_name_plural = "Преподаватели"
        ordering = ['id']

    def __str__(self):
        return f'Teacher - {self.user}'
