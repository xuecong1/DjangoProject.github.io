# Generated by Django 4.2.2 on 2023-06-19 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("index", "0008_delete_studentinfo"),
    ]

    operations = [
        migrations.DeleteModel(name="courseInfo",),
    ]
