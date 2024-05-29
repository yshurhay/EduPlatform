# Generated by Django 5.0.6 on 2024-05-29 11:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0008_add_article_model"),
        ("users", "0003_add_teacher_model"),
    ]

    operations = [
        migrations.CreateModel(
            name="CompletedTest",
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
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="users.student"
                    ),
                ),
                (
                    "test",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="courses.test"
                    ),
                ),
            ],
            options={
                "verbose_name": "Выполненный тест",
                "verbose_name_plural": "Выполненные тесты",
                "ordering": ["id"],
            },
        ),
    ]
