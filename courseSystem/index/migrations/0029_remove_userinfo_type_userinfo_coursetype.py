# Generated by Django 4.2.2 on 2023-06-22 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("index", "0028_alter_userinfo_type"),
    ]

    operations = [
        migrations.RemoveField(model_name="userinfo", name="Type",),
        migrations.AddField(
            model_name="userinfo",
            name="CourseType",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]