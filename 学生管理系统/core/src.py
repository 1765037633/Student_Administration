'''
主视图
'''
# import admin, student, teacher 不可以这样导
from core import admin, student, teacher

func_dict = {
    '1': admin.admin_view,
    '2': student.student_view,
    '3': teacher.teacher_view,
}


def run():
    while True:
        print('''
    ======== 选课系统 =======
    
            1.管理员功能
            2.学生功能
            3.老师功能
        
    ======== 选课系统 =======
        ''')
        count = input("请输入你想选择的功能序号：").strip()
        if count not in func_dict:
            print("你的输入有误，请重新输入")
            continue

        func_dict.get(count)()
