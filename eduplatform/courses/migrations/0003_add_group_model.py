# Generated by Django 5.0.6 on 2024-05-29 12:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("courses", "0002_add_course_model"),
        ("users", "0003_add_teacher_model"),
    ]

    operations = [
        migrations.CreateModel(
            name="Group",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100, verbose_name="Название")),
                ("date_formation", models.DateField(verbose_name="Дата образования")),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="courses.course"
                    ),
                ),
                ("students", models.ManyToManyField(to="users.student")),
                (
                    "teacher",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="users.teacher"
                    ),
                ),
            ],
            options={
                "verbose_name": "Группа",
                "verbose_name_plural": "Группы",
            },
        ),
    ]
