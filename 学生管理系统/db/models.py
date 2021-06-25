'''
存放学员类，教师类，学校类，管理员类，课程类等等需要设置的类
'''
from db import db_handler


# 父类 让所以的子类都继承 select方法 和 save方法
class Base:

    # 查看数据
    @classmethod
    def select(cls, username):  # Admin , 拿到username
        obj = db_handler.select_data(cls, username)
        return obj

    # 保存数据
    def save(self):
        # 让db_handler中的save 功能帮我们保存对象数据
        db_handler.save_data(self)


# 管理员⚪类
class Admin(Base):
    def __init__(self, user, pwd):
        # 给当前对象赋值
        self.user = user
        self.pwd = pwd

    # 管理员创建学校
    def create_school(self, school_name, school_addr):
        # 该方法内部调用了学校类实例化的得到对象，并保存数据
        school_obj = School(school_name, school_addr)
        school_obj.save()

    # 管理员创建课程
    def create_course(self, school_obj, course_name):
        # 1.调用课程类，实例化创建课程
        course_obj = Course(course_name)
        course_obj.save()

        # 2.获取当前学校对象，并将课程添加到课程列表中
        school_obj.course_list.append(course_name)
        school_obj.save()  # 更新学校数据

    # 管理员创建讲师
    def create_teacher(self, teacher_name, teacher_pwd):
        # 调用老师类,实例化到老师的对象，并保存
        teacher_obj = Teacher(teacher_name, teacher_pwd)
        teacher_obj.save()   # 更新老师数据


# 学校类
class School(Base):
    def __init__(self, name, addr):
        # 必须写self.user,因为db_handler里的select_data要统一规范
        self.user = name
        self.addr = addr

        # 课程列表：每一所学校都有相应的课程
        self.course_list = []


# 学生类
class Student(Base):
    pass


# 课程类
class Course(Base):
    def __init__(self, course_name):
        self.user = course_name
        self.student_list = []


# 老师类
class Teacher(Base):
    def __init__(self, teacher_name, teacher_pwd):
        self.user = teacher_name
        self.pwd = teacher_pwd
        self.course_list = []
