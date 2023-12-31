# Generated by Django 4.2.2 on 2023-06-19 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("index", "0014_studentinfo"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("username", models.CharField(max_length=50, unique=True)),
                ("password", models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(name="StudentInfo",),
    ]
