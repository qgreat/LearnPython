"""
Python 高级特性 - 列表推导式和生成器
在 02_集合类型 中你已见过简单的列表推导式，这里深入讲解并引入生成器
"""

# ==================== 列表推导式回顾与深化 ====================
print("=== 列表推导式 ===")

# 基本形式：[表达式 for 变量 in 可迭代对象]
# 等价于：先创建一个空列表，再在 for 循环里 append

# 传统写法
squares_old = []
for x in range(1, 6):
    squares_old.append(x ** 2)

# 列表推导式写法（更简洁、更 Pythonic）
squares = [x ** 2 for x in range(1, 6)]
print(f"平方数: {squares}")  # [1, 4, 9, 16, 25]

# 带条件的推导式：[表达式 for 变量 in 可迭代对象 if 条件]
evens = [x for x in range(10) if x % 2 == 0]
print(f"偶数: {evens}")  # [0, 2, 4, 6, 8]

# 条件也可以放在前面（需要 else 时用三元表达式）
# [结果 if 条件 else 另一结果 for x in ...]
labels = ["偶数" if x % 2 == 0 else "奇数" for x in range(5)]
print(f"奇偶标签: {labels}")  # ['偶数', '奇数', '偶数', '奇数', '偶数']

# 多重 for（嵌套循环）
# 顺序：先写外循环，再写内循环
pairs = [(a, b) for a in [1, 2] for b in ["x", "y"]]
print(f"组合: {pairs}")  # [(1,'x'), (1,'y'), (2,'x'), (2,'y')]

# 实际例子：展平二维列表
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [num for row in matrix for num in row]
print(f"展平矩阵: {flat}")  # [1, 2, 3, 4, 5, 6]

# ==================== 字典推导式 ====================
print("\n=== 字典推导式 ===")

# 形式：{键表达式: 值表达式 for 变量 in 可迭代对象}
# 从列表构建字典
fruits = ["苹果", "香蕉", "橙子"]
length_dict = {f: len(f) for f in fruits}
print(f"水果名长度: {length_dict}")  # {'苹果': 2, '香蕉': 2, '橙子': 2}

# 从两个列表构建字典
keys = ["name", "age", "job"]
values = ["张三", 28, "开发者"]
user_dict = {k: v for k, v in zip(keys, values)}
print(f"用户字典: {user_dict}")

# 带条件的字典推导式
numbers = [1, 2, 3, 4, 5]
square_dict = {n: n ** 2 for n in numbers if n % 2 == 1}
print(f"奇数的平方: {square_dict}")  # {1: 1, 3: 9, 5: 25}

# ==================== 集合推导式 ====================
print("\n=== 集合推导式 ===")

# 形式：{表达式 for 变量 in 可迭代对象}
# 用花括号但无冒号，得到的是集合（去重、无序）
words = ["hello", "world", "hello", "python"]
lengths_set = {len(w) for w in words}
print(f"单词长度的集合（去重）: {lengths_set}")  # {5, 6} 等

# 去重的同时做变换
first_chars = {s[0].upper() for s in words}
print(f"首字母集合: {first_chars}")

# ==================== 元组没有“元组推导式” ====================
# 圆括号 + for 得到的是生成器表达式，不是元组！
# 若要元组，需显式转换：
tuple_from_gen = tuple(x ** 2 for x in range(5))
print(f"从生成器表达式得到的元组: {tuple_from_gen}")

# ==================== 生成器表达式 ====================
print("\n=== 生成器表达式 ===")

# 语法：把列表推导式的方括号 [] 改成圆括号 ()
# 生成器不会一次性生成所有元素，而是“按需”产生（惰性求值）
# 优点：省内存，适合处理大量数据或无限序列

# 列表推导式：一次性在内存中生成整个列表
list_comp = [x ** 2 for x in range(1000000)]  # 占用较多内存

# 生成器表达式：只生成一个生成器对象，每次 next() 才计算下一个值
gen_exp = (x ** 2 for x in range(1000000))  # 几乎不占额外内存
print(f"生成器对象: {gen_exp}")  # <generator object ...>

# 使用方式一：for 循环（自动迭代）
print("前 5 个平方数（用生成器）:")
for i, val in enumerate(gen_exp):
    if i >= 5:
        break
    print(f"  {val}", end=" ")
print()

# 注意：生成器只能遍历一次！上面已经消费了一部分，再遍历会从 6 开始
# 重新创建一个生成器
gen_exp2 = (x ** 2 for x in range(10))
print(f"转成列表: {list(gen_exp2)}")  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 使用方式二：next() 逐个取
gen_exp3 = (x * 10 for x in range(3))
print(f"next: {next(gen_exp3)}, {next(gen_exp3)}, {next(gen_exp3)}")  # 0, 10, 20
# 再 next 会抛出 StopIteration

# ==================== 生成器函数（yield）====================
print("\n=== 生成器函数（yield）===")

# 在函数里使用 yield，函数就变成“生成器函数”
# 调用时不会执行函数体，而是返回一个生成器对象
# 每次 next(生成器) 时，执行到 yield 就暂停并返回值，下次从 yield 后继续


def count_up_to(n):
    """生成从 0 到 n-1 的数字（每次 yield 一个）"""
    i = 0
    while i < n:
        yield i  # 在这里暂停，把 i 传给调用者
        i += 1


# 调用生成器函数得到生成器对象
gen = count_up_to(4)
print(f"count_up_to(4): {list(gen)}")  # [0, 1, 2, 3]


def fibonacci(max_count):
    """生成前 max_count 个斐波那契数"""
    a, b = 0, 1
    count = 0
    while count < max_count:
        yield a
        a, b = b, a + b
        count += 1


print(f"前 8 个斐波那契数: {list(fibonacci(8))}")


# 生成器可以带条件
def even_squares(n):
    """生成 0 到 n-1 中偶数的平方"""
    for x in range(n):
        if x % 2 == 0:
            yield x ** 2


print(f"偶数的平方: {list(even_squares(10))}")  # [0, 4, 16, 36, 64]

# ==================== 何时用列表推导式，何时用生成器 ====================
print("\n=== 使用场景 ===")

# 列表推导式：需要多次遍历、需要索引/长度、数据量不大
# 例如：结果要反复使用、要 len()、要下标访问
result_list = [x * 2 for x in range(100)]
print(f"列表长度: {len(result_list)}, 第一个: {result_list[0]}")

# 生成器：数据量大、只遍历一次、管道式处理
# 例如：读大文件逐行处理、无限序列、链式转换
def read_large_file_lines(path, max_lines=3):
    """模拟逐行读取大文件（这里用 range 模拟）"""
    for i in range(max_lines):
        yield f"Line {i + 1}"

lines_gen = read_large_file_lines("fake.txt", 3)
for line in lines_gen:
    print(f"  {line}")

# ==================== 小结与练习题 ====================
print("\n=== 小结 ===")
print("• 列表推导式: [x for x in ...] 或带 if/多重 for")
print("• 字典推导式: {k: v for ...}")
print("• 集合推导式: {x for ...}")
print("• 生成器表达式: (x for x in ...) — 惰性，省内存")
print("• 生成器函数: 函数内用 yield，每次产生一个值")

print("\n=== 练习题 ===")
print("1. 用列表推导式生成 1~20 中能被 3 整除的数的平方列表")
print("2. 用字典推导式把列表 ['a','b','c'] 变成 {0:'a', 1:'b', 2:'c'}")
print("3. 写一个生成器函数 range_step(start, end, step)，按步长生成整数")
print("4. 用生成器表达式求 1~100 内所有偶数的和（用 sum()）")
