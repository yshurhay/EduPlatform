# Generated by Django 5.0.6 on 2024-05-30 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0001_add_specialization_model"),
    ]

    operations = [
        migrations.CreateModel(
            name="Course",
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
                ("description", models.TextField(verbose_name="Описание")),
                ("duration", models.DurationField(verbose_name="Продолжительность")),
                (
                    "specialization",
                    models.ManyToManyField(
                        to="courses.specialization", verbose_name="Специализации"
                    ),
                ),
            ],
            options={
                "verbose_name": "Курс",
                "verbose_name_plural": "Курсы",
            },
        ),
    ]
