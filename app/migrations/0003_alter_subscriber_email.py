# Generated by Django 5.0 on 2023-12-06 21:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0002_rename_usersubscriber_subscriber"),
    ]

    operations = [
        migrations.AlterField(
            model_name="subscriber",
            name="email",
            field=models.EmailField(max_length=255, unique=True),
        ),
    ]
