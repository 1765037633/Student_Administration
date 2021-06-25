import os

# 获取目录
BASE_PATH = os.path.dirname(os.path.dirname(__file__))

# 获取文件路径
DB_PATH = os.path.abspath(os.path.join(
    BASE_PATH, 'db'
))

# print(DB_PATH)
