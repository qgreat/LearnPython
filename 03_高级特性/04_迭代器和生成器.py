"""
Python 高级特性 - 迭代器和生成器
迭代器协议（__iter__ / __next__）、与可迭代对象的关系、生成器是迭代器的语法糖
"""

# ==================== 可迭代对象 vs 迭代器 ====================
print("=== 可迭代与迭代器 ===")

# 可迭代对象（Iterable）：能用 for 遍历的，如 list、dict、str、range
# 要求：有 __iter__ 方法，返回一个“迭代器”
# 迭代器（Iterator）：有 __next__ 方法，每次返回下一个元素，没有时抛出 StopIteration
# 迭代器通常也有 __iter__，返回 self，这样“迭代器也是可迭代的”

from collections.abc import Iterator, Iterable

# 列表是可迭代的，但不是迭代器（没有 __next__）
lst = [1, 2, 3]
print(f"list 是可迭代: {isinstance(lst, Iterable)}")  # True
print(f"list 是迭代器: {isinstance(lst, Iterator)}")  # False

# iter(list) 得到列表的迭代器
it = iter(lst)
print(f"iter(list) 是迭代器: {isinstance(it, Iterator)}")  # True

# 用 next() 逐个取
print(f"next: {next(it)}, {next(it)}, {next(it)}")  # 1, 2, 3
# next(it)  # 再取会 StopIteration

# ==================== 自定义迭代器类 ====================
print("\n=== 自定义迭代器 ===")


class CountDown:
    """从 n 倒数到 0 的迭代器"""

    def __init__(self, n):
        self.n = n
        self.current = n

    def __iter__(self):
        """返回迭代器自身（迭代器也是可迭代的）"""
        return self

    def __next__(self):
        """返回下一个值，没有时抛出 StopIteration"""
        if self.current < 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value


for i in CountDown(3):
    print(f"  {i}", end=" ")
print()

# ==================== 迭代器协议小结 ====================
# 可迭代对象：有 __iter__()，返回迭代器
# 迭代器：有 __next__()，有 __iter__() 通常返回 self
# for x in obj 等价于：it = iter(obj)，然后重复 x = next(it) 直到 StopIteration

# ==================== 生成器是迭代器 ====================
print("\n=== 生成器即迭代器 ===")

# 生成器函数（含 yield）被调用时返回生成器对象
# 生成器对象满足迭代器协议：有 __iter__ 和 __next__，因此可以直接 for 或 next()


def my_range(n):
    """生成 0 到 n-1"""
    i = 0
    while i < n:
        yield i
        i += 1


gen = my_range(3)
print(f"生成器是迭代器: {isinstance(gen, Iterator)}")  # True
print(f"next: {next(gen)}, {next(gen)}, {next(gen)}")  # 0, 1, 2

# for 循环本质就是不断 next(迭代器)
print("for my_range(4):", list(my_range(4)))

# ==================== iter() 的两种用法 ====================
print("\n=== iter() 用法 ===")

# 1. iter(可迭代对象) → 获取其迭代器
# 2. iter(可调用, 哨兵值) → 重复调用可调用对象直到返回哨兵值
#    例如：iter(f.read, '') 会反复 f.read() 直到读到空字符串（常用于按块读文件）

def read_until_sentinel():
    """模拟：每次返回一行，遇到 'END' 停止"""
    lines = ["line1", "line2", "END", "after"]
    for line in lines:
        yield line

# 用 iter 带哨兵的典型写法是 iter(callable, sentinel)，这里用生成器演示“迭代到结束”
it = iter(read_until_sentinel())
for line in it:
    if line == "END":
        break
    print(f"  {line}")

# ==================== 生成器与迭代器对比 ====================
print("\n=== 生成器 vs 手写迭代器 ===")

# 手写迭代器：需要维护状态（如 self.current），手写 __next__ 和 __iter__
# 生成器：用 yield 自动挂起/恢复状态，代码更短，逻辑更清晰

# 同一逻辑：倒数
def count_down_gen(n):
    """用生成器实现倒数"""
    while n >= 0:
        yield n
        n -= 1


print("生成器倒数:", list(count_down_gen(3)))

# ==================== 迭代器只能遍历一次 ====================
print("\n=== 一次性 ===")

gen_once = (x for x in range(3))
print(f"第一次: {list(gen_once)}")  # [0, 1, 2]
print(f"第二次: {list(gen_once)}")  # []，已耗尽

# 需要多次遍历时，用列表或每次重新创建生成器/迭代器
lst_data = list(range(3))
print(f"列表可多次: {list(lst_data)},  again: {list(lst_data)}")

# ==================== 迭代器节省内存 ====================
# 列表会一次性占用 N 个元素的内存；迭代器/生成器每次只产生一个，适合流式处理大数据

# ==================== 小结与练习 ====================
print("\n=== 小结 ===")
print("• 可迭代：有 __iter__；迭代器：有 __iter__ 和 __next__")
print("• for 循环：iter(obj) → 再反复 next() 直到 StopIteration")
print("• 生成器对象是迭代器，用 yield 写更简洁")
print("• 迭代器/生成器只能遍历一次，多次用需重建或转成列表")

print("\n=== 练习题 ===")
print("1. 写一个类 RangeIterator(start, end, step)，用 __next__ 按步长产生整数")
print("2. 用生成器函数实现上面的 RangeIterator 逻辑")
print("3. 用 iter(可调用, 哨兵) 从列表 [1,2,-1,3,-1] 中迭代直到遇到 -1，收集前面的数")
