"""
Python 文件和 IO - 异常处理
try / except / else / finally、抛出异常、常见异常类型
"""

# ==================== 基本 try except ====================
print("=== try except ===")

try:
    num = int("abc")  # 会抛出 ValueError
except ValueError as e:
    print(f"捕获到 ValueError: {e}")

# 不写 as e 也可以，只判断类型
try:
    result = 1 / 0  # ZeroDivisionError
except ZeroDivisionError:
    print("捕获到 ZeroDivisionError（除零）")

# ==================== 多个 except ====================
print("\n=== 多个 except ===")

def parse_number(s):
    try:
        return int(s)
    except ValueError:
        return None
    except TypeError:
        return None

print(f"parse_number('42'): {parse_number('42')}")
print(f"parse_number('x'): {parse_number('x')}")

# 一次捕获多种异常：except (ValueError, TypeError) as e:
# 捕获所有异常（慎用）：except Exception as e:

# ==================== else 和 finally ====================
print("\n=== else / finally ===")

# else：在 try 块没有发生异常时执行
# finally：无论是否异常都会执行，常用于释放资源（如关闭文件）
try:
    f = open("不存在的文件.txt")
except FileNotFoundError as e:
    print(f"文件不存在: {e}")
else:
    # 只有没异常时才会执行
    print("读取成功")
    f.close()
finally:
    # 无论是否异常都执行（这里没打开文件就不关）
    print("finally 执行完毕")

# ==================== 主动抛出异常 ====================
print("\n=== raise ===")

def set_age(age):
    if not (0 <= age <= 150):
        raise ValueError("年龄必须在 0~150 之间")
    return age

try:
    set_age(200)
except ValueError as e:
    print(f"捕获: {e}")

# 重新抛出当前异常：在 except 里写 raise，不带参数
# 抛出别的异常：raise ValueError("消息")

# ==================== 常见异常类型 ====================
print("\n=== 常见异常 ===")

# ValueError     传入值不合法，如 int("x")
# TypeError      类型错误，如 "2" + 3
# IndexError     索引越界，如 [][0]
# KeyError       字典键不存在，如 {}["x"]
# FileNotFoundError  文件不存在
# ZeroDivisionError  除零
# AttributeError 对象没有该属性
# 继承关系：BaseException ← Exception ← 各种具体异常，一般捕获 Exception 即可涵盖大部分

# ==================== 自定义异常 ====================
print("\n=== 自定义异常 ===")

class MyError(Exception):
    """自定义异常，继承 Exception"""
    pass

class ConfigError(MyError):
    """配置错误"""
    def __init__(self, key, msg=None):
        self.key = key
        self.msg = msg or f"配置项错误: {key}"
        super().__init__(self.msg)

try:
    raise ConfigError("timeout", "超时时间无效")
except ConfigError as e:
    print(f"ConfigError: {e}, key={e.key}")

# ==================== 小结与练习 ====================
print("\n=== 小结 ===")
print("• try / except [异常类型] [as 变量] / else / finally")
print("• raise 异常类型(消息) 主动抛出；except 里 raise 重新抛出")
print("• 自定义异常继承 Exception，可加属性")

print("\n=== 练习题 ===")
print("1. 写一个 safe_divide(a, b)，除零时返回 None 并打印提示，不抛异常")
print("2. 写一个 read_config(path)，文件不存在或 JSON 解析失败时抛出自定义异常")
print("3. 用 try/except 包裹一段“可能出错”的代码，并打印异常类型和消息")
