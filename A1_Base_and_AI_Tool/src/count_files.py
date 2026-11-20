import os
from pathlib import Path

root = Path(__file__).resolve().parents[2]
skip = {".git", ".venv", "__pycache__"}
total = 0

for current, dirs, files in os.walk(root):
    dirs[:] = [d for d in dirs if d not in skip]
    total += len(files)

print(f"统计目录：{root}")
print(f"文件总数：{total}")
