"""
Python 模块和包 - 虚拟环境
venv 的创建、激活、作用：隔离项目依赖，避免与系统 Python 冲突
"""

# ==================== 为什么需要虚拟环境 ====================
print("=== 虚拟环境的作用 ===")

# 不同项目可能依赖同一库的不同版本，若都装到系统 Python，会冲突
# 虚拟环境为每个项目提供独立的 Python 解释器和 pip 安装目录：
#   - 项目 A：venv_a，可装 django==3.2
#   - 项目 B：venv_b，可装 django==4.0
# 互不影响

# ==================== 创建与激活（在终端执行）====================
print("\n=== 创建与激活 ===")

# 在项目根目录下创建名为 venv 的虚拟环境（目录名可自定义）：
#   python3 -m venv venv
# 会生成 venv/ 目录，内含 bin、lib 等

# 激活（激活后，命令行前会多出 (venv) 等提示）：
#   macOS/Linux:   source venv/bin/activate
#   Windows:       venv\\Scripts\\activate

# 激活后：
#   which python   → 指向 venv/bin/python
#   pip install 包  → 安装到 venv 内

# 退出虚拟环境：
#   deactivate

# ==================== 本文件中检查是否在虚拟环境 ====================
print("\n=== 当前环境 ===")

import sys

# 若在虚拟环境中，sys.prefix 和 sys.base_prefix 可能不同（部分系统上相同）
# 另一种方式：看 sys.executable 是否在 venv 目录下
exe = sys.executable
if "venv" in exe or "env" in exe:
    print(f"  可能处于虚拟环境中: {exe}")
else:
    print(f"  当前 Python: {exe}")
    print("  （若未激活 venv，上面是系统或其它 Python）")

# ==================== 常用流程小结 ====================
print("\n=== 推荐流程 ===")

print("""
  1. 进入项目目录:  cd 你的项目
  2. 创建虚拟环境:  python3 -m venv venv
  3. 激活:          source venv/bin/activate   # macOS/Linux
  4. 安装依赖:       pip install -r requirements.txt
  5. 开发、运行
  6. 退出:          deactivate
""")

# ==================== 小结与练习 ====================
print("=== 小结 ===")
print("• python3 -m venv venv 创建虚拟环境")
print("• source venv/bin/activate 激活，deactivate 退出")
print("• 激活后 pip 和 python 都指向该环境，便于隔离依赖")

print("\n=== 练习题 ===")
print("1. 在 LearnPython 项目下执行 python3 -m venv venv，再 source venv/bin/activate")
print("2. 激活后执行 which python3 和 pip3 list，观察路径和包列表")
print("3. 在 venv 中安装 requests，再 deactivate，比较 pip3 list 与系统环境差异")
