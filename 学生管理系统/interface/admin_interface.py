'''
管理员接口层
'''
from db import models


# 管理员注册接口
def admin_register_interface(username, password):
    # 1.判断注册用户名是否存在
    # 调用Admin类中的select，用该方法去调用db_handler中的select_data的功能获取对象
    admin_obj = models.Admin.select(username)

    # 1.1 要是存在就不允许注册，返回提示信息给视图层
    if admin_obj:
        return False, '该用户以存在，请重新输入'

    # 1.2 不存在则允许注册，调用类实例化并保存
    admin_obj = models.Admin(username, password)

    # 对象调用save(),会将admin.obj穿给save方法
    admin_obj.save()

    return True, '注册成功'


# 管理员登录接口
def admin_login_interface(username, password):
    # 1.判断用户是否存在，
    admin_obj = models.Admin.select(username)

    # 2.若用户不存在存在，返回信息给视图层
    if not admin_obj:
        return False, '用户不存在,请重新输入！'

    # 3.用户存在就校验用户密码
    if admin_obj.pwd == password:
        return True, '登陆成功'
    else:
        return False, '密码错误！请重新输入！！'


# 管理员创建学校接口
def create_school_interface(school_name, school_addr, admin_name):
    # 1.查看所要创建的学校是否存在
    school_obj = models.School.select(school_name)

    # 2.存在则返回False,提示学校已经存在
    if school_obj:
        return False, "该学校(校区)以存在！！，请重新输入！"

    # 3.若不存则创建（由管理员用户创建）
    admin_obj = models.Admin.select(admin_name)
    admin_obj.create_school(school_name, school_addr)

    # 4.创建学校成功，返回给视图层
    return True, f"{[school_name]} 创建成功！恭喜恭喜！！"


# 管理员创建课程接口
def create_course_interface(school_name, course_name, admin_name):
    # 1.先查看学校是否存在

    # 1.1 获取学校对像的课程列表
    school_obj = models.School.select(school_name)

    # 1.2 再判断当前课程是否在课表列表中
    if course_name in school_obj.course_list:
        return False, "当前课程也存在，请重新输入！！"

    # 1.3 如果课程不存在就创建课程，由管理员来创建
    admin_obj = models.Admin.select(admin_name)
    admin_obj.create_course(
        school_obj, course_name
    )

    return True, f"[{course_name}] 课程创建成功，绑定给[{school_name}] 校区"


# 管理员创建老师接口
def create_teacher_interface(teacher_name, admin_name, teacher_pwd='123'):
    # 1.判断老师是否存在
    teacher_obj = models.Teacher.select(teacher_name)

    # 2.要是存在的话，就返回不能创建
    if teacher_obj:
        return False, "老师已经存在！请重新输入！"

    # 3.不存在，创建老师，让管理员来创建
    admin_obj = models.Admin.select(admin_name)
    admin_obj.create_teacher(teacher_name, teacher_pwd)

    return True, f"[{teacher_name}] 老师创建成功！"
