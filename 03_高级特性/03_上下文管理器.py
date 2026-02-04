"""
Python 高级特性 - 上下文管理器
with 语句和 with 背后的协议：__enter__ / __exit__，以及 contextlib 的简便写法
"""

# ==================== with 语句是什么 ====================
print("=== with 语句 ===")

# with 用于“进入时做准备、离开时做清理”，例如打开文件后自动关闭
# 常见写法：with open("file.txt") as f: ...

# 等价于（概念上）：
# 1. 调用 上下文管理器.__enter__()，返回值赋给 as 后面的变量
# 2. 执行 with 块
# 3. 无论是否异常，都会调用 __exit__ 做清理

# 手动打开关闭文件（不推荐）
# f = open("test.txt")
# try:
#     data = f.read()
# finally:
#     f.close()

# 推荐：with 自动关闭
# with open("test.txt") as f:
#     data = f.read()
# 离开 with 块后 f 会自动关闭

# 下面用自定义类演示协议，不依赖真实文件

# ==================== 类方式：__enter__ 和 __exit__ ====================
print("\n=== 类实现上下文管理器 ===")


class Timer:
    """计时上下文管理器：进入时记录开始时间，离开时打印耗时"""

    def __enter__(self):
        """进入 with 时调用，返回值会赋给 as 后面的变量"""
        import time

        self.start = time.time()
        return self  # 通常返回 self，这样可以用 as t 访问 t.start 等

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        离开 with 时调用（包括异常时）
        exc_type: 异常类型，无异常时为 None
        exc_val: 异常实例
        exc_tb: 追溯信息
        返回 True 表示“已处理异常”，Python 不会再把异常向外抛；False 或 None 会继续抛出
        """
        import time

        elapsed = time.time() - self.start
        print(f"耗时: {elapsed:.4f} 秒")
        if exc_type:
            print(f"  发生异常: {exc_type.__name__}: {exc_val}")
        return False  # 不吞掉异常，让调用方知道


with Timer() as t:
    print("  with 块内执行")
    print(f"  开始时间: {t.start}")

# 演示异常时 __exit__ 仍会被调用
print("带异常的 with:")
try:
    with Timer():
        raise ValueError("故意出错")
except ValueError as e:
    print(f"外层捕获: {e}")

# ==================== contextlib.contextmanager ====================
print("\n=== contextmanager 装饰器 ===")

# 用生成器 + 装饰器写上下文管理器，只需写“进入时 yield 前的代码”和“yield 后的清理代码”
from contextlib import contextmanager


@contextmanager
def simple_timer(name="操作"):
    """用生成器实现的计时器"""
    import time

    start = time.time()
    print(f"[{name}] 开始")
    try:
        yield  # 这里之前相当于 __enter__，之后相当于 __exit__ 前的逻辑
    finally:
        print(f"[{name}] 结束，耗时 {time.time() - start:.4f} 秒")


with simple_timer("任务A"):
    print("  执行任务 A")

# ==================== 实际例子：临时切换目录 ====================
print("\n=== 实际例子：临时目录 ===")

import os
from contextlib import contextmanager


@contextmanager
def temporary_cd(path):
    """临时进入某目录，退出 with 后回到原目录"""
    old_cwd = os.getcwd()
    try:
        os.chdir(path)
        yield
    finally:
        os.chdir(old_cwd)


print(f"当前目录: {os.getcwd()}")
# 若有子目录 demo，可 with temporary_cd("demo"): ...
# 这里仅演示结构，不真正 chdir 到不存在的路径

# ==================== 同时管理多个资源 ====================
print("\n=== 多个 with 写在一起 ===")

# 从 Python 3.10 起可以：
# with open("a.txt") as f1, open("b.txt") as f2:
# 更早版本可以嵌套 with，或使用 contextlib.ExitStack（略）

# 用类演示“多资源”概念
class Resource:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print(f"  打开资源 {self.name}")
        return self

    def __exit__(self, *args):
        print(f"  关闭资源 {self.name}")
        return False


with Resource("A") as a, Resource("B") as b:
    print(f"  使用 {a.name} 和 {b.name}")

# ==================== contextlib 其他常用工具 ====================
print("\n=== suppress / nullcontext ===")

from contextlib import suppress, nullcontext

# suppress(异常类型)：在 with 块内忽略指定异常
with suppress(ValueError):
    int("not a number")  # 不抛异常，静默忽略
print("  suppress 已忽略 ValueError")

# nullcontext：不做事，只提供一个值，用于“有时有上下文，有时没有”的统一样式
with nullcontext(42) as x:
    print(f"  nullcontext 提供的值: {x}")

# ==================== 小结与练习 ====================
print("\n=== 小结 ===")
print("• with 语句：自动调用 __enter__ / __exit__，保证清理")
print("• 类实现：实现 __enter__ 和 __exit__，__exit__ 可吞掉异常（返回 True）")
print("• @contextmanager：用 yield 分界“进入”和“退出”，更简洁")
print("• 多资源：with A() as a, B() as b: ...")

print("\n=== 练习题 ===")
print("1. 实现一个 LockContext，进入时 print('加锁')，退出时 print('解锁')")
print("2. 用 @contextmanager 实现一个 suppress(ZeroDivisionError) 的等价写法")
print("3. 写一个 with open('x.txt') as f 的等价类 FileContext（只要求 __enter__ 返回 f）")
