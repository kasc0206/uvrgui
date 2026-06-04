# Changelog / 更新日志

All notable changes to this project will be documented in this file.

格式基于 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.1.0/)。

---

## [Unreleased]

### 新增
- i18n 国际化框架：`gui_data/l10n.py` + `en.json` / `zh.json` 语言包
- 设置菜单添加语言切换下拉框（English/中文）
- CLI 增强：`--no-progress` 隐藏进度条、`--output-format` 别名、argcomplete shell 补全
- 配置系统升级：`config --init`、`config --list`、版本自动迁移
- CUDA Dockerfile (`Dockerfile.cuda`)：NVIDIA GPU 容器构建

### 变更
- README 改为中英文混合文档
- GUI 界面全面汉化（~350 处字符串）
- 容器构建优先推荐 OrbStack（兼容 Docker CLI）

### 修复
- Pylance 类型警告：`menu_move_tab` 缺失 `self`、`secondary_stem` 未绑定变量
- README markdownlint 错误（MD033/031/032/004/024/034 等）

---

## [v1.0.0] — 2026-05-31

### 新增
- CLI 工具 `uvr_cli.py`：12 个命令（list/info/process/download-models/config/gui/version/help + --json）
- 测试套件：63 个 pytest 测试 + coverage 覆盖率报告
- `playsound.py`：playsound3 兼容垫片
- `__version__.py`：FORK_VERSION / FORK_REPO 版本信息
- `pyproject.toml`：项目元数据 + ruff lint 配置
- `.editorconfig` / `.pre-commit-config.yaml` / `.gitattributes`：代码规范
- Dockerfile：多阶段容器构建
- `Makefile`：install/run/lint/fix/clean 快捷命令
- GitHub Actions：Windows EXE 自动构建（CPU + CUDA）

### 变更
- 模型数据大幅扩充：MDX 模型配置 +830/-351，26 个新模型名称映射
- 新增 BS-Roformer / Mel-Roformer / MB-Roformer / SCNet / Bandit / MDX23C 模型支持
- `requirements.txt` 重建，基于当前已验证虚拟环境
- 模型下载方式：`torch.hub.load_state_dict_from_url` → `curl`（快 500 倍）

### 修复
- `highlightthicknes` tkinter 拼写错误 → `highlightthickness`（5 处）
- `from gui_data.constants import *` → 862 个精确符号导入
- Pylance 类型错误减少 107 个（244 → 137）
- ~120 处 `font=(name, f"{size}")` → `font=(name, size)`

---

## [v5.6] — 上游版本

同步至上游 [Anjok07/ultimatevocalremovergui](https://github.com/Anjok07/ultimatevocalremovergui) v5.6。

### 新增
- BS-Roformer / Mel-Roformer / MB-Roformer / SCNet / Bandit 模型支持
- MPS (Apple Silicon) GPU 加速
- Phase Swapper Tool：参考音频相位应用到目标音频
- Apollo Restore Tool：修复低码率音频失真
- Model Installer：VR Arch / MDX-Net / Apollo 模型安装器
- 模型别名功能：不修改文件名即可重命名模型
- YAML 配置编辑：GUI 内直接编辑模型 YAML

### 变更
- 增强模型配置菜单：支持批量配置、自动填充现有设置
- 集成模式模型框增加横向滚动条
- ffmpeg / Rubber Band 不再弹出 CMD 窗口
- 旧 GPU 默认使用 Torch "No Grad" 模式

---

## [v5.5.0] — 上游版本

### 新增
- MDX23C 模型支持（ZFTurbo 训练）
- Karaoke 模式增强
- 去混响（DeReverb）功能

### 变更
- VR Architecture 模型更新
- 界面性能优化

---

## [v5.4.0] — 上游版本

### 新增
- Demucs v4 (htdemucs) 4-stem 支持
- 6-stem 模型 (htdemucs_6s) 支持
- Ensemble Mode 集成模式

### 变更
- 模型架构重构
- 批量处理性能优化

---

## [v5.3.0] — 上游版本

### 新增
- MDX-Net 架构支持
- 二级模型混合（Secondary Model Mode）
- 模型自动下载

### 变更
- GUI 界面重构
- 性能优化

---

## [v5.2.0] — 上游版本

### 新增
- Demucs v3 模型支持
- 音频格式选择（WAV/FLAC/MP3）
- GPU 加速选项

---

## [v5.1.0] — 上游版本

### 新增
- VR Architecture 1.0
- 批量处理模式
- 基础 CLI 支持

---

## [v5.0.2] — 初始版本

### 新增
- 首个公开发布版本
- VR Architecture 基础功能
- 人声/伴奏分离
- Tkinter GUI

---

<!-- 链接引用 -->
[Unreleased]: https://github.com/kasc0206/uvrgui/compare/v1.0.0...HEAD
[v1.0.0]: https://github.com/kasc0206/uvrgui/releases/tag/v1.0.0
