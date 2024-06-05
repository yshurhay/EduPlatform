# Generated by Django 5.0.6 on 2024-06-01 10:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0003_add_teacher_model"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="customuser",
            options={
                "verbose_name": "Пользователь",
                "verbose_name_plural": "Пользователи",
            },
        ),
        migrations.AlterField(
            model_name="student",
            name="rating",
            field=models.PositiveSmallIntegerField(
                default=0,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(100),
                ],
                verbose_name="Рейтинг",
            ),
        ),
    ]
