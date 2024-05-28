from django.db import models
from users.models import Student, Teacher


class Specialization(models.Model):
    title = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Специализации"
        verbose_name_plural = "Специализации"
        ordering = ['id']

    def __str__(self):
        return f'Specialization #{self.pk} - {self.title}'


class Course(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    duration = models.DurationField(verbose_name="Продолжительность")
    specialization = models.ManyToManyField(Specialization)

    def str(self):
        return f"{self.pk} - {self.title}"

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
        ordering = ['id']


class Group(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    quantity = models.IntegerField(verbose_name="Количество человек")
    date_formation = models.DateField(verbose_name="Дата образования")
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ManyToManyField(Student)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def str(self):
        return f"{self.pk} - {self.title} - {self.date_formation}"

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"
        ordering = ['id']
