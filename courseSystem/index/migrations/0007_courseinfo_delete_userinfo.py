# Generated by Django 4.2.2 on 2023-06-19 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("index", "0006_rename_name_studentinfo_title"),
    ]

    operations = [
        migrations.CreateModel(
            name="courseInfo",
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
                ("name", models.CharField(max_length=32)),
                ("num", models.CharField(max_length=64)),
                ("time", models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(name="UserInfo",),
    ]
