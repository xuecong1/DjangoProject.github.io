from django.db import models


# Create your models here.
# 在MySQL中创建对应的一个表
class UserInfo(models.Model):
    # 创建字段
    name = models.CharField(max_length=32)
    num = models.CharField(max_length=64)
    time = models.IntegerField(null=True, default=None)

    enroll_status = models.CharField(max_length=10,
                                     choices=[('开放', '开放选课'), ('关闭', '已关闭选课'), ('待定', '待定')],
                                     default='pending')
    gpa_condition = models.FloatField(null=True, blank=True)
    level_condition = models.CharField(max_length=10,
                                       choices=[('大一', '大一'), ('大二', '大二'), ('大三', '大三'),
                                                ('大四', '大四')], default='pending')
    Course_Type = models.CharField(max_length=50, null=True, blank=True)

    # sex = models.CharField(max_length=2)


# class StudentInfo(models.Model):
#     title = models.CharField(max_length=32)

class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)


class CourseInfo(models.Model):
    Course_Type = models.CharField(max_length=50, unique=True)
    # enroll_status = models.CharField(max_length=10,
    #                                  choices=[('open', '开放选课'), ('closed', '已关闭选课'), ('pending', '待定')],default='pending')
    # gpa_condition = models.FloatField(null=True, blank=True)
    # level_condition = models.CharField(max_length=10,
    #                                    choices=[('freshman', '大一'), ('sophomore', '大二'), ('junior', '大三'),
    #                                             ('senior', '大四')],default='pending')
# class TeacherInfo(models.Model):
#     name = models.CharField(max_length=32)
