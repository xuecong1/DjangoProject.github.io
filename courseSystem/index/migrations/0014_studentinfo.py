# Generated by Django 4.2.2 on 2023-06-19 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("index", "0013_delete_user"),
    ]

    operations = [
        migrations.CreateModel(
            name="StudentInfo",
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
                ("title", models.CharField(max_length=32)),
            ],
        ),
    ]
