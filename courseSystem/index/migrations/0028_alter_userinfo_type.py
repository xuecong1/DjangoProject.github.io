# Generated by Django 4.2.2 on 2023-06-22 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("index", "0027_alter_userinfo_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userinfo",
            name="Type",
            field=models.CharField(
                default=1, editable=False, max_length=50, unique=True
            ),
        ),
    ]