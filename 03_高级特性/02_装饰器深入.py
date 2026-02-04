"""
Python 高级特性 - 装饰器深入
在 01_基础语法/04_函数 中已有装饰器预览，这里深入：functools.wraps、带参数装饰器、类装饰器、多层装饰
"""

import functools
import time

# ==================== 装饰器本质回顾 ====================
print("=== 装饰器本质 ===")

# @decorator 等价于：func = decorator(func)
# 装饰器是一个“接收函数、返回新函数”的函数


def simple_decorator(func):
    """最简单的装饰器：包装原函数，在前后加打印"""

    def wrapper(*args, **kwargs):
        print(f"调用前: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"调用后: {func.__name__}")
        return result

    return wrapper


@simple_decorator
def say_hello(name):
    return f"Hello, {name}!"


print(say_hello("张三"))
# 问题：此时 say_hello 实际是 wrapper，__name__ 会变成 "wrapper"，文档字符串也会丢失

# ==================== functools.wraps ====================
print("\n=== functools.wraps ===")

# 使用 wraps 把原函数的 __name__、__doc__ 等元信息复制到 wrapper上，便于调试和文档


def logged(func):
    """带日志的装饰器，并保留原函数元信息"""

    @functools.wraps(func)  # 将 func 的名字、文档等复制到 wrapper
    def wrapper(*args, **kwargs):
        print(f"[LOG] 进入 {func.__name__}")
        result = func(*args, **kwargs)
        print(f"[LOG] 离开 {func.__name__}")
        return result

    return wrapper


@logged
def add(a, b):
    """两数相加"""
    return a + b


print(f"add(2, 3) = {add(2, 3)}")
print(f"函数名: {add.__name__}, 文档: {add.__doc__}")  # 正确显示 add 和其 docstring

# ==================== 带参数的装饰器 ====================
print("\n=== 带参数的装饰器 ===")

# 若需要 @decorator(参数)，则 decorator(参数) 必须返回一个“真正的装饰器”（接收 func 的函数）
# 即：三层结构 —— 外层传参，中层是装饰器，内层是 wrapper


def repeat(times):
    """重复执行函数 times 次（装饰器带参数）"""

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(times):
                results.append(func(*args, **kwargs))
            return results  # 返回所有结果的列表

        return wrapper

    return decorator


@repeat(3)
def greet(name):
    return f"Hi, {name}!"


print(greet("李四"))  # ['Hi, 李四!', 'Hi, 李四!', 'Hi, 李四!']


# 另一种常见用法：重试装饰器
def retry(max_attempts=3):
    """失败时重试最多 max_attempts 次"""

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_error = None
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_error = e
                    print(f"第 {attempt} 次失败: {e}")
            raise last_error

        return wrapper

    return decorator


# ==================== 类装饰器 ====================
print("\n=== 类装饰器 ===")

# 用类实现装饰器：类需要可调用，即实现 __call__
# 这样 @ClassName 等价于 func = ClassName(func)，之后调用 func() 会走 __call__


class CountCalls:
    """统计函数被调用次数的类装饰器"""

    def __init__(self, func):
        self.func = func
        self.call_count = 0
        functools.update_wrapper(self, func)  # 类似 wraps，把元信息拷到 self

    def __call__(self, *args, **kwargs):
        self.call_count += 1
        print(f"第 {self.call_count} 次调用")
        return self.func(*args, **kwargs)


@CountCalls
def say_hi():
    return "Hi!"


print(say_hi())
print(say_hi())
print(f"总调用次数: {say_hi.call_count}")

# ==================== 多个装饰器叠加 ====================
print("\n=== 多个装饰器 ===")

# @A
# @B
# def f(): ...
# 等价于 f = A(B(f))，执行时先经过 B 的 wrapper，再经过 A 的 wrapper（从上到下包装，从外到内执行）


def bold(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return "<b>" + func(*args, **kwargs) + "</b>"

    return wrapper


def italic(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return "<i>" + func(*args, **kwargs) + "</i>"

    return wrapper


@bold
@italic
def text():
    return "Hello"


print(text())  # <b><i>Hello</i></b>，先执行 italic 再 bold

# ==================== 常见内置/标准装饰器回顾 ====================
print("\n=== 常用装饰器 ===")

# @staticmethod、@classmethod、@property 在 02_面向对象/01_类和对象 中已学
# 标准库还有：functools.lru_cache（缓存）、functools.singledispatch（重载）等


@functools.lru_cache(maxsize=128)
def fib(n):
    """带缓存的斐波那契，相同 n 只算一次"""
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


print(f"fib(35) = {fib(35)}")  # 有缓存后很快
print(f"缓存信息: {fib.cache_info()}")

# ==================== 小结与练习 ====================
print("\n=== 小结 ===")
print("• 装饰器本质: func = decorator(func)，用 wrapper 包装原函数")
print("• 用 functools.wraps 保留 __name__、__doc__")
print("• 带参装饰器: 三层函数，外层接收参数返回 decorator")
print("• 类装饰器: 实现 __call__，用 update_wrapper 保留元信息")
print("• 多装饰器: @A @B def f → f = A(B(f))，从上到下包装")

print("\n=== 练习题 ===")
print("1. 写一个 @deprecated(msg) 装饰器，调用时打印弃用警告 msg")
print("2. 写一个 @timer 装饰器，统计函数执行时间并打印")
print("3. 用类实现一个 @Memoize 装饰器，缓存无参函数的返回值")
