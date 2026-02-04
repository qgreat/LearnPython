"""
Python 基础 - 变量和数据类型
适合有编程经验的开发者快速上手
"""

# ==================== 变量声明 ====================
# Python 是动态类型语言，不需要声明变量类型
name = "张三"  # 字符串
age = 28  # 整数
height = 1.75  # 浮点数
is_developer = True  # 布尔值

print(f"姓名: {name}, 年龄: {age}, 身高: {height}m, 是否开发者: {is_developer}")

# ==================== 基本数据类型 ====================
# 1. 数字类型
integer_num = 42  # 整数
float_num = 3.14  # 浮点数
complex_num = 3 + 4j  # 复数（Python 特有）

# 2. 字符串（不可变类型）
single_quote = '单引号字符串'
double_quote = "双引号字符串"
multi_line = """
多行字符串
可以跨越多行
"""

# 字符串常用操作
text = "Hello Python"
print(f"长度: {len(text)}")  # 长度
print(f"大写: {text.upper()}")  # 转大写
print(f"小写: {text.lower()}")  # 转小写
print(f"分割: {text.split()}")  # 分割成列表
print(f"替换: {text.replace('Python', 'World')}")  # 替换

# 字符串格式化（推荐使用 f-string，Python 3.6+）
language = "Python"
version = 3.11
print(f"{language} 版本是 {version}")  # f-string（最推荐）
print("{} 版本是 {}".format(language, version))  # format 方法
print("%s 版本是 %.1f" % (language, version))  # 旧式格式化

# 3. 布尔类型
is_true = True
is_false = False
# 注意：Python 中的布尔值首字母大写

# 4. None 类型（类似其他语言的 null）
nothing = None
if nothing is None:
    print("nothing 是 None")

# ==================== 类型转换 ====================
# 显式类型转换
str_num = "123"
int_num = int(str_num)  # 字符串转整数
float_num = float(str_num)  # 字符串转浮点数
str_from_int = str(int_num)  # 整数转字符串

print(f"原始: {str_num} (类型: {type(str_num).__name__})")
print(f"转换后: {int_num} (类型: {type(int_num).__name__})")

# ==================== 类型检查 ====================
# 使用 type() 函数检查类型
print(f"\ntype(42) = {type(42)}")  # <class 'int'>
print(f"type('hello') = {type('hello')}")  # <class 'str'>
print(f"type(True) = {type(True)}")  # <class 'bool'>

# 使用 isinstance() 检查类型（更推荐）
if isinstance(age, int):
    print(f"{age} 是整数类型")

# ==================== 变量命名规范 ====================
# Python 使用 snake_case 命名（不同于移动端的 camelCase）
user_name = "正确"  # ✓ 推荐
userName = "不推荐"  # ✗ 不符合 Python 规范
USER_NAME = "常量"  # ✓ 常量使用全大写

# 私有变量使用下划线前缀（见下方「私有 vs 强私有」说明）
_private_var = "私有变量"
__very_private = "强私有变量"

# ==================== 私有变量 vs 强私有变量 ====================
# 单下划线 _xxx：约定上的「私有」，Python 不强制，外部仍可访问
# 双下划线 __xxx：名称改编（Name Mangling），避免子类同名冲突，并非真正不可访问
#
# 区别总结：
# 1. _private   → 只是约定，提示「内部使用」，obj._private 可直接访问
# 2. __private  → 解释器会改名为 _类名__private，子类不会意外覆盖，仍可用 obj._类名__private 访问
#
# 注意：Python 没有像 Java/C++ 那样的「真正私有」，都是约定或名称改编

print("\n=== 练习题 ===")
print("1. 创建一个变量存储你的姓名、年龄和职业")
print("2. 使用 f-string 格式化输出这些信息")
print("3. 将一个数字字符串转换为整数并进行数学运算")

student = {
    "name": "张三",
    "age": 20,
    "gender": "男",
    "score": 90,
    "class": "1班",
    "id": "1234567890",
    "phone": "1234567890",
    "email": "zhangsan@example.com",
}

studentList = [student, student, student]
for student in studentList:
    print(student)

studentList.append(student)
print(studentList)

studentList.remove(student)
print(studentList)

studentList.pop()
print(studentList)