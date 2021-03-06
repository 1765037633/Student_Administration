'''
教师视图层
'''
from lib import common
teacher_info = {
    "user": None
}


# 老师登录
def login():
    pass


# 老师查看教授课程
@common.auth('teacher')
def check_course():
    pass


# 老师选择教授课程
@common.auth('teacher')
def choose_course():
    pass


# 老师查看课程下的学员
@common.auth('teacher')
def check_stu_from_course():
    pass


# 老师修改学生的分数
@common.auth('teacher')
def change_score_from_stu():
    pass


func_dict = {
    '1': login,
    '2': check_course,
    '3': choose_course,
    '4': check_stu_from_course,
    '5': change_score_from_stu,
}


def teacher_view():
    while True:
        print('''
======== 老师功能 ========

         1.登录
         2.查看教授课程
         3.选择教授课程
         4.查看课程下的学员
         5.修改学生分数

======== 老师功能 ========            
        ''')
        choice = input("请输入你选择的功能序号(输入q退出)：").strip()
        if choice == 'q':
            break

        if choice not in func_dict:
            print("你的输入有误，请重新输入！！")
            continue
        func_dict.get(choice)()
