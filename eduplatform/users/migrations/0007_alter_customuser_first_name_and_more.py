# Generated by Django 5.0.6 on 2024-06-20 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0006_customuser_email_is_verified"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="first_name",
            field=models.CharField(
                blank=True, max_length=50, null=True, verbose_name="first name"
            ),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="last_name",
            field=models.CharField(
                blank=True, max_length=50, null=True, verbose_name="last name"
            ),
        ),
    ]
