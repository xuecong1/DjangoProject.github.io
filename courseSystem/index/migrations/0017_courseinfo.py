# Generated by Django 4.2.2 on 2023-06-21 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("index", "0016_user_email"),
    ]

    operations = [
        migrations.CreateModel(
            name="CourseInfo",
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
                ("Course_Type", models.CharField(max_length=50, unique=True)),
            ],
        ),
    ]
