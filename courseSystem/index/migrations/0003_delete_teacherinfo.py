# Generated by Django 4.2.2 on 2023-06-08 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("index", "0002_studentinfo_teacherinfo"),
    ]

    operations = [
        migrations.DeleteModel(name="TeacherInfo",),
    ]