'''
学生视图层
'''
from lib import common

student_info = {
    "user": None
}


# 学生注册
def register():
    pass


# 学生登录
def login():
    pass


# 学生选择校区
@common.auth('student')
def choice_school():
    pass


# 学生选择课程
@common.auth('student')
def choice_course():
    pass


# 学生查看分数
@common.auth('student')
def check_score():
    pass


func_dict = {
    '1': register,
    '2': login,
    '3': choice_school,
    '4': choice_course,
    '5': check_score,
}


def student_view():
    while True:
        print('''
===*=*===$= 学生功能 =$==*=*====

            1.注册
            2.登录
            3.选择校区
            4.选择课程
            5.查看分数

===*=*===$= 学生功能 =$==*=*====            
        ''')
        choice = input("请输入你选择的功能序号(输入q退出)：").strip()
        if choice == 'q':
            break

        if choice not in func_dict:
            print("你的输入有误，请重新输入！！")
            continue
        func_dict.get(choice)()
