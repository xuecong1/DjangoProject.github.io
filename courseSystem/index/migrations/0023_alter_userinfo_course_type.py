# Generated by Django 4.2.2 on 2023-06-22 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("index", "0022_alter_userinfo_course_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userinfo",
            name="Course_Type",
            field=models.CharField(default=2, max_length=50, unique=True),
        ),
    ]