from django.shortcuts import render, HttpResponse, redirect
from .models import User


# Create your views here.
def index(request):
    return HttpResponse("hellow world!")


def course_add(request):
    if request.method == "GET":
        return render(request, "course_add.html", {"msg": ""})
    elif request.method == "POST":
        get_post = request.POST
        coursename = get_post.get("coursename")
        num = get_post.get("coursenum")
        time = get_post.get("coursetime")
        from index.models import UserInfo
        UserInfo.objects.create(name=coursename, num=num, time=int(time))
        if UserInfo.objects.filter(name=coursename):
            return redirect("/course/list/")
        else:
            msg = "提交失败"
            return render(request, "course_add.html", {"msg": msg})


def course_register(request):
    from index.models import UserInfo, CourseInfo

    if request.method == 'POST':
        # 从 POST 请求中获取表单数据
        course_num = request.POST.get('num')
        course_type_id = request.POST.get('type')
        enroll_status = request.POST.get('enroll-status')
        gpa_condition = request.POST.get('gpa-condition')
        level_condition = request.POST.get('level-condition')

        # 获取当前用户并更新 UserInfo 表记录
        userinfo, created = UserInfo.objects.get_or_create(num=course_num)
        userinfo.Course_Type = course_type_id
        userinfo.enroll_status = enroll_status
        userinfo.gpa_condition = gpa_condition
        userinfo.level_condition = level_condition
        userinfo.save()

        # 重定向到成功页面或其他处理页面
        return redirect('/course/detail/')
    else:
        course_type_list = CourseInfo.objects.all()
        return render(request, "course_register.html", {"course_type_list": course_type_list})

    # if request.method == "POST":
    #     # 获取提交的表单数据
    #     get_post = request.POST
    #     num1 = get_post.get("num")
    #     type_id1 = get_post.get('type')
    #     status1 = get_post.get('enroll_status')
    #     gpa1 = get_post.get('gpa_condition')
    #     level1 = get_post.get('level_condition')
    #     print(num1, type_id1, status1, gpa1, level1)
    #     try:
    #         # 根据课程名筛选要修改的对象，并更新对应字段的值
    #         course = CourseInfo.objects.get(num=num1)
    #         course.Course_type = UserInfo.objects.get(id=type_id1)
    #         course.Enroll_status = UserInfo.objects.get(name=status1)
    #         course.GPA_condition = gpa1
    #         course.Level_condition = level1
    #         course.save()
    #         # 更新成功后重定向到课程列表页面
    #         return redirect("http://127.0.0.1:8000/course/list/")
    #     except UserInfo.DoesNotExist:
    #         # 数据库中不存在该课程，则返回错误信息
    #         return render(request, "course_update.html", {"msg": "课程不存在"})
    # else:
    #     # 查询课程类型列表，传递到前端页面进行展示
    #     course_type_list = CourseInfo.objects.all()
    #     return render(request, "course_register.html", {"course_type_list": course_type_list})


def course_del(request):
    if request.method == "GET":
        return render(request, "course_delete.html", {"msg": ""})
    elif request.method == "POST":
        get_post = request.POST
        coursename = get_post.get("coursename")
        try:
            from index.models import UserInfo
            UserInfo.objects.filter(name=coursename).delete()
        except UserInfo.DoesNotExist:
            return render(request, "course_delete.html", {"msg": "删除失败"})
        return redirect("/course/list/")


def course_detail(request):
    from index.models import UserInfo
    all_data = UserInfo.objects.all()
    if request.method == "GET":
        return render(request, "course_detail.html", {"course_detail": all_data})


def course_cleck(request):
    if request.method == "POST":
        from index.models import UserInfo
        coursename = request.POST.get("coursename")
        data = UserInfo.objects.filter(name=coursename).first()
        if data is not None:
            return render(request, "course_cleck.html", {"course_cleck": data})
        else:
            msg = "未找到该课程名"
            return render(request, "course_cleck.html", {"msg": msg})
    else:
        return render(request, "course_cleck.html", {})


# def course_update(request):
#     if request.method == "GET":
#         return render(request, "course_update.html", {"msg": ""})
#     elif request.method == "POST":
#         get_post = request.POST
#         name1 = get_post.get("coursename")
#         num1 = get_post.get("coursenum")
#         time1 = get_post.get("coursetime")
#         try:
#             from index.models import UserInfo
#             UserInfo.objects.filter(name=name1).update(num=num1, time=int(time1))
#         except UserInfo.DoesNotExist:
#             return render(request, "course_update.html", {"msg": "修改失败"})
#         return redirect("http://127.0.0.1:8000/course/list/")


def course_update(request):
    if request.method == "POST":
        # 获取提交的表单数据
        coursename = request.POST.get("coursename")
        coursenum = request.POST.get("coursenum")
        coursetime = request.POST.get("coursetime")

        try:
            from index.models import UserInfo
            # 根据课程名筛选要修改的对象，并更新对应字段的值
            UserInfo.objects.filter(name=coursename).update(num=coursenum, time=int(coursetime))
            # 更新成功后重定向到课程列表页面
            return redirect("/course/list/")
        except UserInfo.DoesNotExist:
            # 数据库中不存在该课程，则返回错误信息
            return render(request, "course_update.html", {"msg": "修改失败"})

    # GET请求则渲染课程更新页面
    return render(request, "course_update.html")


def course_list(request):
    from index.models import UserInfo
    all_data = UserInfo.objects.all()
    if request.method == "GET":
        return render(request, "course_list.html", {"course_list": all_data})
    elif request.method == "POST":
        # action = request.form['action']
        # user_id = request.form['user_id']
        form_value = request.POST.get('form')

        if form_value == 'form1':
            return redirect('/course/add/')
        elif form_value == 'form2':
            return redirect('/course/manage/')
        elif form_value == 'form3':
            return redirect('/course/cleck/')
        elif form_value == 'form4':
            return redirect('/course/detail/')
        elif form_value == 'form5':
            return redirect('/course/register/')
    return render(request, "course_list.html")


def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    elif request.method == "POST":
        post_data = request.POST
        username = post_data.get("username")
        pwd = post_data.get("password")
        print(post_data)
        user = User.objects.filter(username=username, password=pwd).first()
        if user:
            return redirect("/course/list/")
        else:
            return render(request, "login.html", {"tip": "用户或密码错误"})


def register(request):
    if request.method == "GET":
        return render(request, "register.html")
    elif request.method == "POST":
        post_data = request.POST
        username = post_data.get("username")
        email = post_data.get("email")
        pwd1 = post_data.get("password1")
        pwd2 = post_data.get("password2")
        print(post_data)
        # 校验两次密码是否一致
        if pwd1 != pwd2:
            return render(request, "register.html", {"tip": "两次密码不一致"})
        # 根据用户名判断用户是否已经存在
        user = User.objects.filter(username=username).first()
        if user:
            return render(request, "register.html", {"tip": "用户名已存在"})
        # 创建新用户并保存到数据库
        new_user = User(username=username, email=email, password=pwd1)
        new_user.save()
        return redirect("http://127.0.0.1:8000")


def course_manage(request):
    from index.models import UserInfo
    all_data = UserInfo.objects.all()
    if request.method == "GET":
        return render(request, "course_manage.html", {"course_manage": all_data})
    elif request.method == "POST":
        # action = request.form['action']
        # user_id = request.form['user_id']
        button_value = request.POST.get('button')

        if button_value == 'button1':
            return redirect('/course/update/')
        elif button_value == 'button2':
            return redirect('/course/delete/')
    return render(request, "course_list.html")


def dep_list(request):
    return render(request, "dep_list.html")


def __str__(self):
    return self.username
