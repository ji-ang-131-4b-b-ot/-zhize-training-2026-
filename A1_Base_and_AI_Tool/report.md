# A.1 学习记录

## 使用环境与配置过程

本次使用 Windows 宿主机和 WSL Ubuntu 22.04，在 AI 辅助下完成了 Python 虚拟环境、Git 提交身份和 GitHub 推送认证等配置。

主要环境如下：

- Python：3.10.12
- uv：0.13.9
- GitHub CLI：2.4.0
- 项目目录：/home/bonjour/-zhize-training-2026-

首先将个人培训仓库克隆到 Ubuntu，然后使用 `uv venv --python 3.10` 创建 `.venv` 虚拟环境，通过 `source .venv/bin/activate` 激活。

执行 `python -c "import sys; print(sys.executable)"` 后，输出指向项目中的 `.venv/bin/python`，确认使用的是虚拟环境内的解释器。

随后配置 Git 提交姓名和邮箱，并通过 `git check-ignore -v .venv/bin/python` 确认 `.venv` 已被忽略。使用 GitHub CLI 完成网页登录授权，再配置 Git 使用该授权，最终成功提交并推送代码。

## 文件统计脚本的用途和运行方法

脚本位于 `A1_Base_and_AI_Tool/src/count_files.py`，用于递归统计仓库中的文件数量，仅使用 Python 标准库。

主要逻辑如下：

- `root`：根据脚本所在位置，定位仓库根目录。
- `skip`：保存需要跳过的目录名，包括 `.git`、`.venv` 和 `__pycache__`。
- `os.walk(root)`：遍历仓库中的目录和文件。
- `dirs[:]`：原地修改待遍历的子目录列表，使程序不再进入需要排除的目录。
- `total += len(files)`：累计各目录中的文件数量。

在仓库根目录中，先执行 `source .venv/bin/activate`，再执行 `python A1_Base_and_AI_Tool/src/count_files.py`。

首次运行输出的文件总数为 3。这是当时仓库内容对应的统计结果；后续增加报告和截图后，数量会随实际文件变化。

## 遇到的问题与解决方法

### 1. 将代码框的语言标签当成命令

开始时输入了 `Bash`，终端提示找不到命令。后来确认，Bash 是代码框的语言标签，实际操作时只需要执行框内的命令。

### 2. 关闭终端后不知道如何继续

关闭终端窗口后，项目文件仍保存在 Ubuntu 中。重新打开 Ubuntu，再进入原仓库目录即可继续操作；如果需要运行项目中的 Python，还要重新激活虚拟环境。

### 3. GitHub CLI 参数不兼容

执行登录命令时出现 `unknown flag: --git-protocol`。当前安装的 gh 2.4 不支持该参数，因此改用 `gh auth login --hostname github.com --web` 完成登录。

### 4. 无法自动打开浏览器

网页登录过程中，终端提示缺少 `xdg-open` 等浏览器启动工具。随后手动在 Windows 浏览器中打开 GitHub 设备授权页面，输入本次验证码并完成授权，终端显示登录成功。

### 5. 登录成功后仍无法推送

gh 登录完成后，执行 `git push` 仍然出现认证失败。执行 `gh auth setup-git --hostname github.com`，让 Git 使用 gh 保存的认证信息，再次推送后成功出现 `main -> main`。

这说明 Git 的提交姓名、邮箱用于记录作者信息，GitHub 认证则用于验证向远程仓库上传代码的权限，两者作用不同。

## 本地 AI 工具与网页 AI 的使用区别

本次使用宿主机上的 AI 工具辅助生成脚本、解释命令和排查错误，练习中的 uv、Python 和 Git 命令由本人在 Ubuntu 终端执行。

未接入本地工程的网页对话，通常需要使用者提供代码、报错和运行结果，再手动执行建议。接入工程环境的 AI 工具，可以在授权范围内读取项目文件、修改代码、调用终端，并根据实际执行结果继续处理。

本次 gh 参数不兼容的问题也说明，AI 给出的命令需要结合本机软件版本和实际输出进行核对，不能仅凭文字说明判断操作是否成功。

Linux 侧 AI 工具及模型 API 的接入情况，仍需补充实际运行记录和截图。

## 已完成事项、待完成事项与运行截图

### 已完成

- [x] 在 WSL Ubuntu 中使用 Git 和 Python。
- [x] 使用 uv 创建并激活 Python 虚拟环境。
- [x] 验证虚拟环境解释器路径及 Git 忽略规则。
- [x] 在 AI 辅助下编写并运行文件统计脚本。
- [x] 配置 Git 提交身份和 GitHub 推送认证。
- [x] 完成脚本源码的提交与推送。
- [x] 补充 README 中的功能和运行说明。
- [x] 创建报告文件，并通过 `git pull --ff-only` 同步到本地。

### 待完成或补充证据

- [ ] Linux 侧 AI 工具读取项目并正常工作的运行记录。
- [ ] 大模型 API 成功调用的验证记录。
- [ ] 网络配置与连通性的完整验收记录。
- [ ] 将脚本运行截图和 AI 工具运行截图整理到 images 目录并提交。
- [ ] 核对本报告，补充个人实际使用体会。
