"""
Python 模块和包 - 包管理
pip 安装第三方库、requirements.txt、PyPI、常用命令
"""

# ==================== pip 是什么 ====================
print("=== pip ===")

# pip 是 Python 的包管理工具，用于从 PyPI（Python Package Index）安装、卸载、列出第三方库
# 通常随 Python 安装，对应关系：python3 对应 pip3

# 常用命令（在终端执行，不在本 .py 里执行）：
#   pip3 install 包名          # 安装最新版
#   pip3 install 包名==1.0.0    # 安装指定版本
#   pip3 uninstall 包名        # 卸载
#   pip3 list                  # 列出已安装的包
#   pip3 show 包名             # 查看包信息
#   pip3 freeze                # 输出已安装包及版本（常用于生成 requirements.txt）

# ==================== requirements.txt ====================
print("\n=== requirements.txt ===")

# 项目依赖通常写在 requirements.txt 中，每行一个包，可带版本约束
# 示例内容：
#   requests>=2.28.0
#   flask==2.3.0
#   numpy

# 安装文件中所有依赖：
#   pip3 install -r requirements.txt

# 生成当前环境的依赖列表（用于分享或部署）：
#   pip3 freeze > requirements.txt

# 本学习项目若暂时不用第三方库，可以没有 requirements.txt；做项目时建议养成习惯

# ==================== 虚拟环境与 pip ====================
print("\n=== 虚拟环境中的 pip ===")

# 使用虚拟环境时，应先激活再执行 pip：
#   source venv/bin/activate   # macOS/Linux
#   pip install requests       # 此时安装到 venv 内，不影响系统 Python
# 这样不同项目可以用不同版本的同一库，互不干扰

# ==================== 国内镜像（可选）====================
print("\n=== 使用国内镜像 ===")

# 若从 PyPI 下载慢，可使用国内镜像，例如清华：
#   pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple 包名
# 或临时使用：
#   pip3 install --index-url https://pypi.tuna.tsinghua.edu.cn/simple 包名

# ==================== 本文件仅做说明 ====================
# 下面用代码检查是否安装了 requests（仅演示，不强制安装）
try:
    import requests

    print(f"已安装 requests，版本: {requests.__version__}")
except ImportError:
    print("未安装 requests。在终端执行: pip3 install requests")

# ==================== 小结与练习 ====================
print("\n=== 小结 ===")
print("• pip3 install / uninstall / list / show / freeze")
print("• requirements.txt 记录依赖，pip install -r requirements.txt 安装")
print("• 建议在虚拟环境中安装项目依赖")

print("\n=== 练习题 ===")
print("1. 在终端执行 pip3 list，观察已安装的包")
print("2. 创建 requirements.txt，写一行 requests>=2.28，然后 pip3 install -r requirements.txt")
print("3. 在虚拟环境中安装 flask，再用 pip freeze 查看并保存到 requirements.txt")
