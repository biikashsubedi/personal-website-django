# Generated by Django 4.2.6 on 2023-10-09 05:21

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Home",
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
                (
                    "model",
                    models.CharField(
                        editable=False, max_length=200, verbose_name="Model Name"
                    ),
                ),
                (
                    "value",
                    models.CharField(
                        editable=False, max_length=200, verbose_name="Today's Data"
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="created"),
                ),
            ],
            options={
                "verbose_name_plural": "Home",
                "db_table": "homes",
            },
        ),
    ]
