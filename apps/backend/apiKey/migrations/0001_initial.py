# Generated by Django 4.2.1 on 2023-09-01 07:43

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ApiKey",
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
                ("title", models.CharField(max_length=200, verbose_name="Title")),
                (
                    "key",
                    models.CharField(
                        blank=True, max_length=200, null=True, verbose_name="Key"
                    ),
                ),
                ("hits", models.IntegerField(default=0, verbose_name="Hits")),
                ("status", models.BooleanField(default=True, verbose_name="Status")),
            ],
            options={
                "verbose_name_plural": "Api Key",
                "db_table": "api_keys",
            },
        ),
    ]
