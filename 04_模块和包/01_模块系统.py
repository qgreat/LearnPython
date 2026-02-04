"""
Python 模块和包 - 模块系统
如何用 import 导入模块、__name__ 与“主程序”判断、搜索路径
"""

# ==================== 什么是模块 ====================
print("=== 模块 ===")

# 一个 .py 文件就是一个模块。模块名就是文件名去掉 .py
# 使用 import 模块名 或 from 模块名 import 名字 来使用其他模块的代码

# 例如标准库：
import math

print(f"math.pi = {math.pi}")
print(f"math.sqrt(16) = {math.sqrt(16)}")

# 只导入需要的名字
from math import pi, sqrt

print(f"直接使用 sqrt(9) = {sqrt(9)}")

# 用 as 起别名（避免重名或长名）
import datetime as dt

print(f"今天: {dt.date.today()}")

# ==================== __name__ 与主程序 ====================
print("\n=== __name__ ===")

# 每个模块都有一个 __name__ 属性：
# - 当该文件被“直接运行”（python 某文件.py）时，__name__ 为 "__main__"
# - 当该文件被其他文件 import 时，__name__ 为模块名（即文件名去掉 .py）

# 因此常见写法：只在“作为主程序运行”时执行测试或启动逻辑
if __name__ == "__main__":
    print("  当前文件被直接运行，__name__ =", __name__)
else:
    print("  当前文件被导入，__name__ =", __name__)

# 这样既可以把该文件当脚本运行，也可以被其他模块 import 而不执行这些代码

# ==================== 导入方式对比 ====================
print("\n=== 导入方式 ===")

# import mod        → 使用 mod.xxx
# from mod import a, b  → 直接使用 a, b
# from mod import *    → 导入 mod 里 __all__ 列出的名字（不推荐，容易命名冲突）
# from mod import a as my_a  → 别名

# 重复 import 同一模块不会重复执行模块代码，只会复用已加载的模块对象

# ==================== 模块搜索路径 ====================
print("\n=== 搜索路径 ===")

import sys

# Python 查找模块的顺序：当前目录、环境变量 PYTHONPATH、标准库、site-packages 等
print("sys.path 前几项:")
for p in sys.path[:4]:
    print(f"  {p}")

# 若要临时加入目录（例如项目根目录）：
# sys.path.insert(0, "/path/to/project")

# ==================== 包（Package）====================
print("\n=== 包 ===")

# 包是“包含 __init__.py 的目录”，用于组织多个模块
# 例如：mypackage/
#         __init__.py
#         a.py
#         b.py
# 使用：import mypackage.a  或  from mypackage import a

# 本学习项目里 01_基础语法、02_面向对象 等是目录，但通常不作为包被 import
# 若某目录下有 __init__.py，则可以用 import 包名.模块名

# __init__.py 可以为空，也可以写包初始化代码或定义 __all__
# from mypackage import * 时，会导入 __init__.py 里 __all__ 列出的子模块或名字

# ==================== 相对导入（在包内部）====================
print("\n=== 相对导入 ===")

# 在包内部的模块里，可以用相对导入引用兄弟模块或父包
# from . import sibling_module   # 当前包下的 sibling_module
# from .sibling_module import something
# from .. import parent_module   # 上一级包
# 注意：相对导入只能在“包内的模块”里使用，不能在主脚本（直接运行的文件）里用

# ==================== 常用标准库模块示例 ====================
print("\n=== 标准库示例 ===")

import random

print(f"随机整数 1~10: {random.randint(1, 10)}")
print(f"随机选一个: {random.choice(['a', 'b', 'c'])}")

import os

print(f"当前工作目录: {os.getcwd()}")
print(f"环境变量 HOME: {os.environ.get('HOME', '未设置')}")

# ==================== 小结与练习 ====================
print("\n=== 小结 ===")
print("• 一个 .py 文件是一个模块；带 __init__.py 的目录是包")
print("• import 模块 / from 模块 import 名字 / as 别名")
print("• __name__ == '__main__' 表示当前文件被直接运行")
print("• 模块搜索顺序：当前目录、PYTHONPATH、标准库、site-packages")

print("\n=== 练习题 ===")
print("1. 新建 utils.py，写一个 add(a,b) 函数，在本文件中 import 并调用")
print("2. 在 utils.py 里用 if __name__ == '__main__' 写一段测试 add 的代码")
print("3. 查文档：os.path.join 的用法，并打印 join('a','b','c') 的结果")
