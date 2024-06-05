# Generated by Django 5.0.6 on 2024-06-01 12:02

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0004_add_image_model"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                verbose_name="Дата создания",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="customuser",
            name="updated_at",
            field=models.DateTimeField(
                auto_now=True, verbose_name="Дата последнего обновления"
            ),
        ),
        migrations.AddField(
            model_name="student",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                verbose_name="Дата создания",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="student",
            name="updated_at",
            field=models.DateTimeField(
                auto_now=True, verbose_name="Дата последнего обновления"
            ),
        ),
        migrations.AddField(
            model_name="teacher",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                verbose_name="Дата создания",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="teacher",
            name="updated_at",
            field=models.DateTimeField(
                auto_now=True, verbose_name="Дата последнего обновления"
            ),
        ),
    ]
