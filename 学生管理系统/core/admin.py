'''
管理员视图层
'''
from interface import admin_interface, common_interface
from lib import common

# user_info = {"user": None}
admin_info = {
    "user": None
}


# 管理员注册
def register():
    print("管理员注册中······")
    while True:
        username = input("请输入注册的用户名：").strip()
        password = input("请输入设置的密码：").strip()
        re_password = input("再次输入设置的密码：").strip()

        if re_password == password:

            # 管理员注册接口
            flag, msg = admin_interface.admin_register_interface(
                username, password
            )
            if flag:
                print(msg)
                break

            else:
                print(msg)

        else:
            print("你输入的两次密码不一致，请重新输入！！")


# 管理员登录
def login():
    print("管理员登录中·······")
    while True:
        username = input("请输入你的用户名：").strip()
        password = input("请输入你的密码: ").strip()

        # 调用管理员登录接口
        flag, msg = admin_interface.admin_login_interface(
            username, password
        )
        if flag:
            print(msg)

            # 记录当前登录状态
            admin_info['user'] = username
            break
        else:
            print(msg)


# 管理员创建学校
@common.auth('admin')
def create_school():
    print("管理员创建学校中·····")
    while True:
        school_name = input("请输入你想设置的学校名字：").strip()
        school_addr = input("请输入你设置的学校的地址：").strip()

        # 调用接口，保存数据
        flag, msg = admin_interface.create_school_interface(

            # 学校名      学校地址      创建学校的管理员
            school_name, school_addr, admin_info.get('user')
        )

        if flag:
            print(msg)
            break
        else:
            print(msg)


# 管理员创建课程
@common.auth('admin')
def create_course():
    print("管理员创建课程中·····")
    while True:

        # 1.让管理员先选择学校

        # 1.1调用接口，获取所有学校的名称并打印
        flag, school_list_or_msg = common_interface.get_all_school_interface()
        if not flag:
            print(school_list_or_msg)
            break

        for index, school_name in enumerate(school_list_or_msg):
            print(f"编号：{index}   学校名：{school_name} ")

        choice = input("请输入你想要选择的学校名称所对应的编号：").strip()

        if not choice.isdigit():
            print("请输入正确的数字！！！")
            continue

        choice = int(choice)

        if choice not in range(len(school_list_or_msg)):
            print("请输入正确的编号！")
            continue

        # 获取选择后的学校名字
        school_name = school_list_or_msg[choice]

        # 2.选择学校后再输入课程名称
        course_name = input("请输入所要创建的课程名称：").strip()

        # 3.调用创建课程接口，让管理员去创建课程
        flag, msg = admin_interface.create_course_interface(
            school_name, course_name, admin_info['user']
        )
        if flag:
            print(msg)
            break
        else:
            print(msg)


# 管理员创建讲师
@common.auth('admin')
def create_teacher():
    print("创建讲师中····")
    while True:
        teacher_name = input("请输入创建老师的名字：").strip()

        # 调用接口创建老师
        flag, msg = admin_interface.create_teacher_interface(
            teacher_name, admin_info['user']
        )

        if flag:
            print(msg)
            break
        else:
            print(msg)


func_dict = {
    '1': register,
    '2': login,
    '3': create_school,
    '4': create_course,
    '5': create_teacher,
}


def admin_view():
    while True:
        print('''
======== 管理员功能 ========
        
         1.注册
         2.登录
         3.创建学校
         4.创建课程
         5.创建讲师
        
======== 管理员功能 ========            
        ''')
        choice = input("请输入你选择的功能序号(输入q退出)：").strip()
        if choice == 'q':
            break

        if choice not in func_dict:
            print("你的输入有误，请重新输入！！")
            continue
        func_dict.get(choice)()
