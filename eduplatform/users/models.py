from courses.mixins import DateTimeMixin
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager

__all__ = {"CustomUser", "Student", "Teacher"}


class CustomUser(DateTimeMixin, AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    first_name = models.CharField(_("first name"), max_length=50, blank=True)
    last_name = models.CharField(_("last name"), max_length=50, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return f"{self.pk} - {self.email}"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Student(DateTimeMixin, models.Model):
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        verbose_name="Рейтинг",
        default=0,
    )
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, verbose_name="Пользователь"
    )

    def __str__(self):
        return f"{self.pk} - {self.user.email}"

    class Meta:
        verbose_name = "Студенты"
        verbose_name_plural = "Студенты"


class Teacher(DateTimeMixin, models.Model):
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, verbose_name="Пользователь"
    )
    specializations = models.ManyToManyField(
        "courses.Specialization", verbose_name="Специализации"
    )

    def __str__(self):
        return f"Teacher - {self.user}"

    class Meta:
        verbose_name = "Преподаватели"
        verbose_name_plural = "Преподаватели"
