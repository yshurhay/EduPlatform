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

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
        ordering = ['id']

    def str(self):
        return f"{self.pk} - {self.title}"


class Group(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    quantity = models.IntegerField(verbose_name="Количество человек")
    date_formation = models.DateField(verbose_name="Дата образования")
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ManyToManyField(Student)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"
        ordering = ['id']

    def str(self):
        return f"{self.pk} - {self.title} - {self.date_formation}"


class Topic(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    course = models.ForeignKey(to=Course, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Тема"
        verbose_name_plural = "Темы"
        ordering = ['id']

    def __str__(self):
        return f'Title #{self.pk} - {self.title}'


class Test(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    topic = models.ForeignKey(to=Topic, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Тест"
        verbose_name_plural = "Тесты"
        ordering = ['id']

    def __str__(self):
        return f'Test #{self.pk} - {self.title}'


class Question(models.Model):
    DIFFICULTY_CHOICES = [
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard'),
    ]

    text = models.TextField(verbose_name='Текст вопроса')
    difficulty = models.CharField(max_length=6, choices=DIFFICULTY_CHOICES, verbose_name='Сложность')
    test = models.ForeignKey(to=Test, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"
        ordering = ['id']

    def __str__(self):
        return f'Question #{self.pk} - {self.difficulty}'


class Answer(models.Model):
    title = models.CharField(max_length=100, verbose_name='Ответ')
    is_correct = models.BooleanField(verbose_name='Верный ответ')
    question = models.ForeignKey(to=Question, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"
        ordering = ['id']

    def __str__(self):
        return f'Answer #{self.pk} - {self.title}'


class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    specializations = models.ManyToManyField(to=Specialization)

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ['id']

    def __str__(self):
        return f'Article #{self.pk} - {self.title}'


class CompletedTest(models.Model):
    test = models.ForeignKey(to=Test, on_delete=models.CASCADE)
    student = models.ForeignKey(to=Student, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Выполненный тест"
        verbose_name_plural = "Выполненные тесты"
        ordering = ['id']

    def __str__(self):
        return f'{self.student} - {self.test}'
