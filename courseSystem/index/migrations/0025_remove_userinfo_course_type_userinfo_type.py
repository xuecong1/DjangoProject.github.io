# Generated by Django 4.2.2 on 2023-06-22 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("index", "0024_alter_userinfo_course_type"),
    ]

    operations = [
        migrations.RemoveField(model_name="userinfo", name="Course_Type",),
        migrations.AddField(
            model_name="userinfo",
            name="Type",
            field=models.CharField(default=1, max_length=50, unique=True),
        ),
    ]
