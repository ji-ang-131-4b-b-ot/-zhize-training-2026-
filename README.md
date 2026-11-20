# -zhize-training-2026-
## A.1 文件统计脚本

源码位置：`A1_Base_and_AI_Tool/src/count_files.py`

功能：递归统计仓库内的文件数量，跳过 `.git`、`.venv` 和 `__pycache__` 目录。

环境：Ubuntu 22.04、Python 3.10、uv。脚本仅使用 Python 标准库。

### 运行方法

首次使用时，在仓库根目录执行 `uv venv --python 3.10` 创建虚拟环境。

每次重新打开终端后，进入仓库根目录，依次执行：

1. `source .venv/bin/activate`
2. `python A1_Base_and_AI_Tool/src/count_files.py`

程序会输出统计目录和文件总数。
