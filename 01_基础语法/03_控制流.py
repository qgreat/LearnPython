"""
Python 基础 - 控制流（条件、循环）
注意 Python 的缩进规则！
"""

# ==================== 条件语句 ====================
# Python 使用缩进而不是大括号来表示代码块

print("=== if/elif/else ===")
score = 85

# 基本 if-else
if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 60:
    print("及格")
else:
    print("不及格")

# 比较运算符
# ==  等于
# !=  不等于
# >   大于
# <   小于
# >=  大于等于
# <=  小于等于

# 逻辑运算符
# and  与
# or   或
# not  非（注意不是 ! ）

age = 25
is_student = True

if age >= 18 and not is_student:
    print("成年非学生")
elif age >= 18 or is_student:
    print("成年或学生")

# 成员运算符（Python 特色）
fruits = ["苹果", "香蕉", "橙子"]
if "苹果" in fruits:
    print("列表中有苹果")

if "葡萄" not in fruits:
    print("列表中没有葡萄")

# 三元表达式（类似其他语言的 condition ? true : false）
status = "成年" if age >= 18 else "未成年"
print(f"状态: {status}")

# ==================== for 循环 ====================
print("\n=== for 循环 ===")

# 遍历列表
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(f"数字: {num}")

# 遍历字符串（字符串是可迭代对象）
for char in "Python":
    print(char, end=" ")  # P y t h o n
print()

# 使用 range() 函数（类似其他语言的 for(i=0; i<10; i++)）
print("\nrange 示例:")
for i in range(5):  # 0 到 4
    print(i, end=" ")
print()

for i in range(1, 6):  # 1 到 5
    print(i, end=" ")
print()

for i in range(0, 10, 2):  # 0 到 9，步长为 2
    print(i, end=" ")  # 0 2 4 6 8
print()

# enumerate() - 同时获取索引和值
print("\nenumerate 示例:")
fruits = ["苹果", "香蕉", "橙子"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# enumerate 可以指定起始索引
for index, fruit in enumerate(fruits, start=1):
    print(f"第{index}个水果: {fruit}")

# 遍历字典
print("\n遍历字典:")
user = {"name": "张三", "age": 28, "job": "开发者"}

# 遍历键
for key in user:
    print(f"键: {key}")

# 遍历键值对（推荐）
for key, value in user.items():
    print(f"{key} = {value}")

# 同时遍历多个列表 - zip()
print("\nzip 示例:")
names = ["张三", "李四", "王五"]
ages = [28, 30, 25]
jobs = ["iOS", "Android", "前端"]

for name, age, job in zip(names, ages, jobs):
    print(f"{name}, {age}岁, {job}开发")

# ==================== while 循环 ====================
print("\n=== while 循环 ===")

count = 0
while count < 5:
    print(f"计数: {count}")
    count += 1  # Python 没有 count++ 语法

# 无限循环（配合 break）
print("\n无限循环示例:")
counter = 0
while True:
    print(f"执行第 {counter} 次")
    counter += 1
    if counter >= 3:
        break  # 跳出循环

# ==================== break 和 continue ====================
print("\n=== break 和 continue ===")

# break - 跳出整个循环
print("break 示例:")
for i in range(10):
    if i == 5:
        break
    print(i, end=" ")  # 0 1 2 3 4
print()

# continue - 跳过当前迭代
print("\ncontinue 示例:")
for i in range(10):
    if i % 2 == 0:
        continue  # 跳过偶数
    print(i, end=" ")  # 1 3 5 7 9
print()

# ==================== else 子句（Python 特色！）====================
# for/while 可以有 else 子句，当循环正常结束（没有 break）时执行
print("\n=== for-else 示例 ===")

# 示例1：查找质数
def is_prime(n):
    """判断是否为质数"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            print(f"{n} 不是质数，因为可以被 {i} 整除")
            break
    else:
        # 循环正常结束，没有执行 break
        print(f"{n} 是质数")
        return True
    return False

is_prime(17)
is_prime(15)

# 示例2：在列表中查找元素
print("\n查找示例:")
target = "Python"
languages = ["Java", "Swift", "Kotlin"]

for lang in languages:
    if lang == target:
        print(f"找到了 {target}")
        break
else:
    # 循环结束都没找到
    print(f"没有找到 {target}")

# ==================== 嵌套循环 ====================
print("\n=== 嵌套循环 ===")

# 打印乘法表
print("九九乘法表:")
for i in range(1, 4):  # 简化版，只显示前3行
    for j in range(1, i + 1):
        print(f"{j}x{i}={i*j}", end="  ")
    print()  # 换行

# ==================== 实用模式 ====================
print("\n=== 实用模式 ===")

# 1. 同时迭代多个序列
list1 = [1, 2, 3]
list2 = [4, 5, 6]
for a, b in zip(list1, list2):
    print(f"{a} + {b} = {a + b}")

# 2. 反向迭代
for i in reversed(range(5)):
    print(i, end=" ")  # 4 3 2 1 0
print()

# 3. 迭代副本（修改列表时）
numbers = [1, 2, 3, 4, 5]
for num in numbers[:]:  # 使用切片创建副本
    if num % 2 == 0:
        numbers.remove(num)
print(f"删除偶数后: {numbers}")

print("\n=== 练习题 ===")
print("1. 使用 for 循环计算 1 到 100 的和")
print("2. 打印一个列表中的所有偶数")
print("3. 使用 while 循环实现一个简单的猜数字游戏")
print("4. 遍历一个字典，找出值最大的键")
