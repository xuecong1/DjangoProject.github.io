# Generated by Django 4.2.2 on 2023-06-19 13:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("index", "0012_user_delete_studentinfo"),
    ]

    operations = [
        migrations.DeleteModel(name="User",),
    ]