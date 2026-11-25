
import os
from pathlib import Path

# 获取项目根目录
root = Path(__file__).resolve().parents[2]

# 跳过不需要统计的目录
skip = {".git", ".venv", "__pycache__"}

# 图片文件的扩展名
image_exts = {".png", ".jpg", ".jpeg", ".gif", ".bmp", ".webp",".svg"}

# 初始化计数器
total = 0
image_total = 0

# 遍历项目目录
for current, dirs, files in os.walk(root):
    dirs[:] = [d for d in dirs if d not in skip]

    # 统计所有文件
    total += len(files)

    # 统计图片文件
    image_total += sum(
        1 for name in files
        if Path(name).suffix.lower() in image_exts
    )

# 输出统计结果
print(f"统计目录：{root}")
print(f"文件总数：{total}")
print(f"图片数量：{image_total}")
