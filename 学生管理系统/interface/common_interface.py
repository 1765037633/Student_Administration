'''
公共接口
'''
import os, sys
from conf import sttings


# 查看学校名字接口
def get_all_school_interface():
    # 获取文件夹路径
    school_dir = os.path.join(
        sttings.DB_PATH, 'School'
    )

    # 判断文件夹是否存在，
    if not os.path.exists(school_dir):
        return False, "该学校不存在，请联系管理员询问原因。"

    # 若文件夹存在，获取文件夹中所以学校的名字
    school_list = os.listdir(school_dir)
    return True, school_list
