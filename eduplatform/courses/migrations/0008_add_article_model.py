# Generated by Django 5.0.6 on 2024-05-29 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0007_add_answer_model"),
    ]

    operations = [
        migrations.CreateModel(
            name="Article",
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
                (
                    "image",
                    models.ImageField(blank=True, upload_to="", verbose_name="Фото"),
                ),
                (
                    "specializations",
                    models.ManyToManyField(to="courses.specialization"),
                ),
            ],
            options={
                "verbose_name": "Статья",
                "verbose_name_plural": "Статьи",
            },
        ),
    ]
