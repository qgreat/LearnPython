"""
Python 文件和 IO - 文件操作
open()、读写文本/二进制、with 自动关闭、路径处理
"""

import os

# ==================== 打开与关闭 ====================
print("=== 打开文件 ===")

# open(路径, 模式, encoding=...) 返回文件对象
# 模式常用：'r' 只读（默认）、'w' 覆盖写、'a' 追加、'x' 独占创建（存在则报错）
# 加 'b' 表示二进制：'rb'、'wb'
# 加 '+' 表示读写：'r+'、'w+'
# 文本模式可指定 encoding，如 encoding='utf-8'

# 推荐：用 with 自动关闭，避免忘记 close
# 先创建并写入一个临时文件供后面示例读
demo_path = os.path.join(os.path.dirname(__file__), "demo_io.txt")

with open(demo_path, "w", encoding="utf-8") as f:
    f.write("第一行\n")
    f.write("第二行\n")
    f.write("第三行\n")

print(f"已写入示例文件: {demo_path}")

# ==================== 读取 ====================
print("\n=== 读取 ===")

with open(demo_path, "r", encoding="utf-8") as f:
    # 读全部
    content = f.read()
    print("read() 全部:")
    print(content)

with open(demo_path, "r", encoding="utf-8") as f:
    # 按行读
    lines = f.readlines()  # 返回列表，每行一个元素（含换行符）
    print("readlines():", lines)

with open(demo_path, "r", encoding="utf-8") as f:
    # 逐行迭代（省内存，适合大文件）
    print("逐行:")
    for line in f:
        print(f"  {line.rstrip()}")

# read(n) 读前 n 个字符（文本模式）或 n 字节（二进制）
with open(demo_path, "r", encoding="utf-8") as f:
    head = f.read(6)
    print(f"\nread(6): '{head}'")

# ==================== 写入与追加 ====================
print("\n=== 写入与追加 ===")

# 'w' 会清空原文件
with open(demo_path, "w", encoding="utf-8") as f:
    f.write("新内容\n")
    f.writelines(["A\n", "B\n"])  # 写入多行，不会自动加换行，需自己写 \n

with open(demo_path, "a", encoding="utf-8") as f:
    f.write("追加的一行\n")

with open(demo_path, "r", encoding="utf-8") as f:
    print("写入+追加后:", f.read())

# ==================== 路径处理 ====================
print("\n=== 路径 ===")

# 使用 os.path 拼接、取目录名、取文件名等（跨平台）
cur_dir = os.path.dirname(os.path.abspath(__file__))
print(f"当前脚本所在目录: {cur_dir}")
print(f"路径拼接: {os.path.join(cur_dir, 'sub', 'file.txt')}")
print(f"文件是否存在: {os.path.exists(demo_path)}")
print(f"是文件: {os.path.isfile(demo_path)}")

# Python 3.4+ 也可用 pathlib.Path，更面向对象（可选学习）
from pathlib import Path

p = Path(demo_path)
print(f"pathlib 父目录: {p.parent}, 文件名: {p.name}")

# ==================== 二进制读写 ====================
print("\n=== 二进制 ===")

bin_path = os.path.join(os.path.dirname(__file__), "demo_bin.bin")
with open(bin_path, "wb") as f:
    f.write(b"hello\x00world")  # 字节串

with open(bin_path, "rb") as f:
    data = f.read()
    print(f"读取字节: {data}")

# 清理示例文件（可选，学习时也可保留）
if os.path.exists(demo_path):
    os.remove(demo_path)
    print(f"已删除 {demo_path}")
if os.path.exists(bin_path):
    os.remove(bin_path)
    print(f"已删除 {bin_path}")

# ==================== 小结与练习 ====================
print("\n=== 小结 ===")
print("• open(路径, 'r'/'w'/'a', encoding='utf-8')，推荐 with open(...) as f")
print("• 读：read() / readline() / readlines() / for line in f")
print("• 写：write() / writelines()")
print("• 路径：os.path.join、dirname、exists、pathlib.Path")

print("\n=== 练习题 ===")
print("1. 写程序创建一个 hello.txt，写入三行问候语，再读出来打印")
print("2. 用追加模式在 hello.txt 末尾加一行 '再见'")
print("3. 用 os.listdir 列出当前目录下的所有 .py 文件")
