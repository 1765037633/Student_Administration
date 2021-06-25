import os
import pickle
from conf import sttings


# 保存数据
def save_data(obj):
    # 1.获取对象的保存文件路径
    # 以类名当中文件夹的名字
    class_name = obj.__class__.__name__  # __class__ 获取当前的类，__name__获取当前类的名字
    user_dir_path = os.path.join(
        sttings.DB_PATH, class_name
    )

    # 2.判断文件夹是否存在，不存在则创建文件夹
    if not os.path.exists(user_dir_path):
        os.mkdir(user_dir_path)

    # 3.拼接当前用户的pickle文件路径，以用户名做为文件名
    user_path = os.path.join(
        user_dir_path, obj.user  # obj.user 当前用户名字
    )

    # 打开文件，保存对象（通过pickle）
    with open(user_path, 'wb') as f:
        pickle.dump(obj, f)


def select_data(cls, username):  # 类名 , 名字

    class_name = cls.__name__  # __class__ 获取当前的类，__name__获取当前类的名字
    user_dir_path = os.path.join(
        sttings.DB_PATH, class_name
    )

    # 2.判断文件夹是否存在，不存在则创建文件夹
    if not os.path.exists(user_dir_path):
        os.mkdir(user_dir_path)

    # 3.拼接当前用户的pickle文件路径，以用户名做为文件名
    user_path = os.path.join(
        user_dir_path, username  # obj.user 当前用户名字
    )

    # 4.判断文件是否存在，再打开，不存在就代表用户不存在
    if os.path.exists(user_path):

        # 5.打开文件，获取对象
        with open(user_path, 'rb') as f:
            obj = pickle.load(f)
            return obj
