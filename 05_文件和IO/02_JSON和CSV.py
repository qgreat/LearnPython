"""
Python 文件和 IO - JSON 和 CSV
json 模块读写 JSON；csv 模块读写 CSV 表格
"""

import json
import csv
import os

# ==================== JSON ====================
print("=== JSON ===")

# Python 与 JSON 类型对应：
# dict ↔ object, list ↔ array, str ↔ string, int/float ↔ number, True/False ↔ true/false, None ↔ null

# 内存中的数据结构 → JSON 字符串
data = {"name": "张三", "age": 28, "skills": ["Python", "Swift"], "active": True}
json_str = json.dumps(data, ensure_ascii=False, indent=2)  # ensure_ascii=False 让中文不转 \uXXXX
print("dumps 结果:")
print(json_str)

# JSON 字符串 → Python 对象
parsed = json.loads(json_str)
print(f"\nloads 结果: {parsed}, type: {type(parsed)}")

# 读写文件
json_path = os.path.join(os.path.dirname(__file__), "demo_data.json")
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

with open(json_path, "r", encoding="utf-8") as f:
    loaded = json.load(f)
    print(f"\n从文件 load: {loaded}")

# 清理
if os.path.exists(json_path):
    os.remove(json_path)

# ==================== CSV ====================
print("\n=== CSV ===")

# 写 CSV
csv_path = os.path.join(os.path.dirname(__file__), "demo_table.csv")
rows = [
    ["姓名", "年龄", "城市"],
    ["张三", 28, "北京"],
    ["李四", 25, "上海"],
]
with open(csv_path, "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(rows)

# 读 CSV
with open(csv_path, "r", encoding="utf-8", newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# 用 DictReader 按表头读成字典（每行一个 dict）
with open(csv_path, "r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"  DictRow: {dict(row)}")

# 清理
if os.path.exists(csv_path):
    os.remove(csv_path)

# ==================== 小结与练习 ====================
print("\n=== 小结 ===")
print("• JSON: json.dumps/loads 处理字符串，json.dump/load 处理文件")
print("• CSV: csv.writer/csv.reader，或 csv.DictWriter/DictReader")
print("• 写 CSV 时用 newline='' 避免 Windows 下多换行")

print("\n=== 练习题 ===")
print("1. 把一个包含嵌套 list 的 dict 转成 JSON 字符串并写进文件")
print("2. 用 DictWriter 写一个带表头的 CSV，再读出来用 DictReader 打印")
print("3. 从 JSON 文件读出一个 list，遍历并打印每项的指定字段")
