# Generated by Django 4.2.2 on 2023-06-22 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("index", "0030_remove_userinfo_coursetype_userinfo_course_type_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userinfo",
            name="Course_Type",
            field=models.CharField(max_length=50),
        ),
    ]
