# Generated by Django 5.0.6 on 2024-06-20 11:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0008_remove_customuser_email_is_verified_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="email_is_verified",
            field=models.BooleanField(default=False),
        ),
    ]
