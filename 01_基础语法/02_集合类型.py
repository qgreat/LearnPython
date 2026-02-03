"""
Python 基础 - 集合类型（列表、元组、字典、集合）
这是 Python 最强大的内置数据结构
"""

# ==================== 列表 (List) - 可变、有序 ====================
# 类似于 JavaScript 的数组或 Swift 的 Array

# 创建列表
fruits = ["苹果", "香蕉", "橙子"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", True, 3.14]  # 可以包含不同类型

print("=== 列表操作 ===")
# 访问元素（支持负索引，-1 表示最后一个）
print(f"第一个水果: {fruits[0]}")
print(f"最后一个水果: {fruits[-1]}")

# 切片操作（非常强大！）
print(f"前两个数字: {numbers[0:2]}")  # [1, 2]
print(f"从索引2开始: {numbers[2:]}")  # [3, 4, 5]
print(f"到索引3为止: {numbers[:3]}")  # [1, 2, 3]
print(f"倒序: {numbers[::-1]}")  # [5, 4, 3, 2, 1]

# 修改列表
fruits.append("葡萄")  # 添加元素
fruits.insert(1, "芒果")  # 在指定位置插入
fruits.remove("香蕉")  # 删除指定元素
popped = fruits.pop()  # 删除并返回最后一个元素
print(f"修改后的水果: {fruits}")

# 列表常用方法
numbers_copy = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"长度: {len(numbers_copy)}")  # 长度
print(f"最大值: {max(numbers_copy)}")  # 最大值
print(f"最小值: {min(numbers_copy)}")  # 最小值
print(f"求和: {sum(numbers_copy)}")  # 求和
print(f"排序前: {numbers_copy}")
numbers_copy.sort()  # 原地排序
print(f"排序后: {numbers_copy}")

# 列表推导式（List Comprehension）- Python 特色！
squares = [x**2 for x in range(1, 6)]  # [1, 4, 9, 16, 25]
evens = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]
print(f"平方数: {squares}")
print(f"偶数: {evens}")

# ==================== 元组 (Tuple) - 不可变、有序 ====================
# 类似于不可变的列表，使用圆括号

# 创建元组
coordinates = (10, 20)
rgb = (255, 128, 0)
single_item = (42,)  # 注意：单元素元组需要逗号

print("\n=== 元组操作 ===")
print(f"坐标: {coordinates}")
x, y = coordinates  # 元组解包
print(f"x = {x}, y = {y}")

# 元组不能修改，但可以合并
new_coordinates = coordinates + (30,)
print(f"新坐标: {new_coordinates}")

# 为什么使用元组？
# 1. 不可变性保证数据安全
# 2. 作为字典的键
# 3. 函数返回多个值
def get_user_info():
    return ("张三", 28, "开发者")  # 返回元组

name, age, job = get_user_info()  # 元组解包
print(f"用户: {name}, {age}岁, {job}")

# ==================== 字典 (Dict) - 键值对 ====================
# 类似于 JSON 对象、JavaScript 的 Object、Swift 的 Dictionary

# 创建字典
user = {
    "name": "李四",
    "age": 30,
    "job": "iOS 开发者",
    "skills": ["Swift", "Objective-C", "UIKit"]
}

print("\n=== 字典操作 ===")
# 访问元素
print(f"姓名: {user['name']}")
print(f"年龄: {user.get('age')}")  # 推荐使用 get()，键不存在时不会报错
print(f"城市: {user.get('city', '未知')}")  # 提供默认值

# 修改字典
user["age"] = 31  # 修改值
user["city"] = "北京"  # 添加新键值对
del user["job"]  # 删除键值对
print(f"修改后: {user}")

# 字典常用方法
print(f"所有键: {user.keys()}")
print(f"所有值: {user.values()}")
print(f"所有键值对: {user.items()}")

# 遍历字典
print("\n遍历字典:")
for key, value in user.items():
    print(f"  {key}: {value}")

# 字典推导式
numbers_dict = {x: x**2 for x in range(1, 6)}  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(f"数字字典: {numbers_dict}")

# ==================== 集合 (Set) - 无序、唯一 ====================
# 自动去重，用于成员测试和集合运算

# 创建集合
colors = {"红", "绿", "蓝"}
numbers_set = {1, 2, 3, 3, 4, 5, 5}  # 自动去重 -> {1, 2, 3, 4, 5}
empty_set = set()  # 注意：{} 创建的是空字典，不是空集合

print("\n=== 集合操作 ===")
print(f"去重后: {numbers_set}")

# 添加和删除
colors.add("黄")  # 添加元素
colors.remove("绿")  # 删除元素（不存在会报错）
colors.discard("紫")  # 删除元素（不存在不报错）
print(f"颜色: {colors}")

# 集合运算
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(f"并集: {set1 | set2}")  # {1, 2, 3, 4, 5, 6}
print(f"交集: {set1 & set2}")  # {3, 4}
print(f"差集: {set1 - set2}")  # {1, 2}
print(f"对称差: {set1 ^ set2}")  # {1, 2, 5, 6}

# 成员测试（速度快）
if "红" in colors:
    print("红色在集合中")

# ==================== 集合类型对比 ====================
print("\n=== 数据结构对比 ===")
print("列表 List:   可变、有序、可重复、用 []")
print("元组 Tuple:  不可变、有序、可重复、用 ()")
print("字典 Dict:   可变、无序、键唯一、用 {key: value}")
print("集合 Set:    可变、无序、元素唯一、用 {item}")

print("\n=== 练习题 ===")
print("1. 创建一个学生列表，每个学生是一个字典（包含姓名、年龄、成绩）")
print("2. 使用列表推导式筛选出成绩大于80的学生")
print("3. 创建两个技能集合，找出共同技能和独有技能")
