# Generated by Django 4.2.1 on 2023-10-07 09:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0010_user_token_time"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="last_activity",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="Last Activity"
            ),
        ),
    ]
