# Generated by Django 4.2.1 on 2023-09-06 16:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0009_user_token"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="token_time",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="token time"
            ),
        ),
    ]
