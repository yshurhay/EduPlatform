# Generated by Django 5.0.6 on 2024-05-28 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_student_teacher"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="student",
            name="name",
        ),
        migrations.RemoveField(
            model_name="teacher",
            name="name",
        ),
        migrations.AlterField(
            model_name="student",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="teacher",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
