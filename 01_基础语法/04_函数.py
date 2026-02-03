"""
Python 基础 - 函数
Python 函数非常灵活，支持多种参数类型
"""

# ==================== 基本函数定义 ====================
print("=== 基本函数 ===")

# 使用 def 关键字定义函数
def greet(name):
    """
    这是文档字符串（docstring）
    用于说明函数的作用
    """
    return f"你好, {name}!"

# 调用函数
message = greet("张三")
print(message)

# 无返回值的函数（实际返回 None）
def print_info(name, age):
    """打印用户信息"""
    print(f"姓名: {name}, 年龄: {age}")

print_info("李四", 30)

# ==================== 默认参数 ====================
print("\n=== 默认参数 ===")

def create_profile(name, age=18, city="北京"):
    """
    创建用户档案
    age 和 city 有默认值
    """
    return {
        "name": name,
        "age": age,
        "city": city
    }

# 使用默认值
profile1 = create_profile("王五")
print(profile1)

# 覆盖部分默认值
profile2 = create_profile("赵六", city="上海")
print(profile2)

# 覆盖所有默认值
profile3 = create_profile("孙七", 25, "深圳")
print(profile3)

# ==================== 关键字参数 ====================
print("\n=== 关键字参数 ===")

def describe_pet(animal_type, pet_name, age):
    """描述宠物"""
    print(f"{pet_name} 是一只 {age} 岁的 {animal_type}")

# 位置参数调用
describe_pet("狗", "旺财", 3)

# 关键字参数调用（推荐，更清晰）
describe_pet(pet_name="咪咪", animal_type="猫", age=2)

# 混合使用（位置参数必须在前）
describe_pet("鸟", pet_name="小黄", age=1)

# ==================== 可变参数 ====================
print("\n=== 可变参数 ===")

# *args - 接收任意数量的位置参数（元组）
def sum_all(*numbers):
    """计算所有数字的和"""
    print(f"接收到的参数: {numbers}")  # 这是一个元组
    return sum(numbers)

print(f"总和: {sum_all(1, 2, 3)}")
print(f"总和: {sum_all(1, 2, 3, 4, 5)}")

# **kwargs - 接收任意数量的关键字参数（字典）
def build_profile(first_name, last_name, **user_info):
    """创建用户档案"""
    profile = {
        "first_name": first_name,
        "last_name": last_name
    }
    profile.update(user_info)  # 添加其他信息
    return profile

user = build_profile(
    "张", "三",
    age=28,
    city="北京",
    job="开发者",
    skill="Python"
)
print(f"用户档案: {user}")

# 综合使用
def flexible_function(required, *args, **kwargs):
    """演示三种参数类型"""
    print(f"必需参数: {required}")
    print(f"位置参数: {args}")
    print(f"关键字参数: {kwargs}")

flexible_function("必需", 1, 2, 3, name="张三", age=28)

# ==================== 返回值 ====================
print("\n=== 返回值 ===")

# 返回单个值
def square(x):
    """计算平方"""
    return x ** 2

print(f"5的平方: {square(5)}")

# 返回多个值（实际是元组）
def get_dimensions():
    """返回长、宽、高"""
    return 10, 20, 30

length, width, height = get_dimensions()  # 元组解包
print(f"尺寸: {length} x {width} x {height}")

# 返回字典
def get_user():
    """返回用户信息"""
    return {
        "name": "张三",
        "age": 28,
        "skills": ["Python", "Swift"]
    }

user = get_user()
print(f"用户: {user['name']}")

# ==================== Lambda 函数（匿名函数）====================
print("\n=== Lambda 函数 ===")

# 语法：lambda 参数: 表达式
# 适合简单的一行函数

# 普通函数
def add(x, y):
    return x + y

# Lambda 等价写法
add_lambda = lambda x, y: x + y

print(f"普通函数: {add(3, 5)}")
print(f"Lambda: {add_lambda(3, 5)}")

# Lambda 常用场景：作为参数传递
numbers = [1, 2, 3, 4, 5]

# 使用 map（映射）
squares = list(map(lambda x: x**2, numbers))
print(f"平方: {squares}")

# 使用 filter（过滤）
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"偶数: {evens}")

# 排序时使用
students = [
    {"name": "张三", "score": 85},
    {"name": "李四", "score": 92},
    {"name": "王五", "score": 78}
]
# 按分数排序
sorted_students = sorted(students, key=lambda s: s["score"], reverse=True)
print("按分数排序:")
for student in sorted_students:
    print(f"  {student['name']}: {student['score']}")

# ==================== 作用域 ====================
print("\n=== 变量作用域 ===")

# 全局变量
global_var = "全局变量"

def scope_demo():
    # 局部变量
    local_var = "局部变量"
    print(f"函数内访问全局变量: {global_var}")
    print(f"函数内访问局部变量: {local_var}")
    
    # 修改全局变量需要使用 global 关键字
    global global_var
    global_var = "修改后的全局变量"

scope_demo()
print(f"函数外访问全局变量: {global_var}")
# print(local_var)  # 错误！局部变量在函数外不可访问

# ==================== 函数作为对象 ====================
print("\n=== 函数作为对象 ===")

# Python 中函数是一等公民，可以像变量一样传递

def apply_operation(x, y, operation):
    """应用指定的操作"""
    return operation(x, y)

# 定义一些操作函数
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

# 传递函数作为参数
result1 = apply_operation(5, 3, add)
result2 = apply_operation(5, 3, multiply)
print(f"5 + 3 = {result1}")
print(f"5 * 3 = {result2}")

# 将函数存储在列表中
operations = [add, multiply, lambda x, y: x - y]
for op in operations:
    print(f"操作结果: {op(10, 5)}")

# ==================== 装饰器简介（高级特性）====================
print("\n=== 装饰器（预览）===")

# 装饰器用于在不修改函数代码的情况下增加功能
def timer_decorator(func):
    """计时装饰器"""
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} 执行时间: {end - start:.4f}秒")
        return result
    return wrapper

# 使用装饰器（使用 @ 语法糖）
@timer_decorator
def slow_function():
    """模拟一个耗时的函数"""
    import time
    time.sleep(0.1)
    return "完成"

result = slow_function()

# ==================== 类型提示（Python 3.5+）====================
print("\n=== 类型提示（Type Hints）===")

# Python 是动态类型，但可以添加类型提示（不强制）
def greet_with_type(name: str, age: int) -> str:
    """
    带类型提示的函数
    name: str - 字符串类型
    age: int - 整数类型
    -> str - 返回字符串类型
    """
    return f"{name} 今年 {age} 岁"

print(greet_with_type("张三", 28))

# 复杂类型提示
from typing import List, Dict, Optional

def process_users(users: List[Dict[str, any]]) -> Optional[Dict]:
    """
    处理用户列表
    users: 用户字典的列表
    返回: 可选的字典（可能是 None）
    """
    if not users:
        return None
    return users[0]

print("\n=== 练习题 ===")
print("1. 编写一个函数，接收任意数量的数字，返回最大值和最小值")
print("2. 编写一个函数，接收一个列表和一个函数，对列表中每个元素应用该函数")
print("3. 编写一个函数，使用默认参数创建学生信息")
print("4. 使用 lambda 和 filter 筛选出列表中的所有负数")
