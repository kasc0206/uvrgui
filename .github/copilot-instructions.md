# Ultimate Vocal Remover GUI — Copilot Instructions

## 项目简介

UVR (Ultimate Vocal Remover) 是一款基于深度学习的音频源分离桌面工具，支持 VR Architecture / MDX-Net / Demucs 三大 AI 架构，可将音乐中的人声、伴奏、鼓、贝斯等音源分离为独立音轨。

## 项目结构

```
UVR.py                # Tkinter GUI 主窗口（~8000 行）
uvr_cli.py            # CLI 入口（12 个命令）
separate.py           # 分离引擎核心逻辑
playsound.py          # playsound 兼容 shim
__version__.py        # 版本信息（FORK_VERSION, VERSION, FORK_REPO）
uvr_config.json       # 配置文件（设备、模型、输出格式等）
pyproject.toml        # 项目元数据与依赖声明
requirements.txt      # pip 依赖锁定
UVR.spec              # PyInstaller 构建配置
Dockerfile            # Docker 构建

├── demucs/           # Facebook Demucs 模型实现
│   ├── apply.py      # 模型应用接口
│   ├── demucs.py     # Demucs v4 架构
│   ├── hdemucs.py    # 混合 Demucs
│   ├── htdemucs.py   # 混合时间 Demucs
│   ├── model.py      # 模型定义
│   ├── model_v2.py   # 模型 v2
│   ├── tasnet.py     | TASNet 架构
│   ├── tasnet_v2.py  | TASNet v2
│   ├── transformer.py| Transformer 模块
│   ├── states.py     | 状态管理
│   ├── pretrained.py | 预训练模型加载
│   ├── spec.py       | 频谱工具
│   ├── filtering.py  | 滤波工具
│   ├── utils.py      | 工具函数
│   └── repo.py       | 仓库管理
├── lib_v5/           # VR/MDX 架构模型实现
├── gui_data/         # GUI 资源
│   ├── constants.py  # 常量定义
│   ├── app_size_values.py  # 窗口尺寸
│   ├── error_handling.py   # 错误处理
│   ├── sv_ttk/       # Sun Valley ttk 主题
│   ├── tkinterdnd2/  # 拖拽支持
│   ├── img/          # 图片资源
│   └── fonts/        # 字体文件
├── models/           # 模型文件目录（运行时下载）
├── scripts/          # 辅助脚本
└── tests/            # 测试套件
    ├── test_imports.py     # 导入与版本测试
    ├── test_cli.py         # CLI 命令测试
    ├── test_demucs.py      # Demucs 模型测试
    ├── test_separate.py    # 分离引擎测试
    ├── test_uvr_utils.py   # 工具函数测试
    └── conftest.py         # pytest 共享配置
```

## 技术栈

- **GUI**: Tkinter + sv_ttk 主题
- **AI 推理**: PyTorch 2.x, ONNX Runtime
- **音频处理**: librosa, soundfile, audioread, FFmpeg
- **GPU 加速**: CUDA (NVIDIA), MPS (Apple Silicon)
- **测试**: pytest, coverage
- **代码质量**: Ruff（lint + import 排序）
- **CI/CD**: GitHub Actions（build-windows.yml，Windows EXE 自动构建）

## 代码规范

- Python >= 3.9
- 行长度 100 字符
- 引号使用双引号（`"`）
- import 排序遵循 Ruff I001
- 类型标注推荐但不强制

## 常用命令

### 运行测试

```bash
# 运行所有测试
pytest -v

# 带覆盖率
pytest --cov=. --cov-report=term

# 运行特定测试文件
pytest tests/test_cli.py -v
pytest tests/test_imports.py -v

# 跳过慢测试
pytest -v -m "not slow"
```

### 代码检查

```bash
# Lint 检查
ruff check .

# 自动修复
ruff check --fix .

# 格式化
ruff format .
```

### 运行应用

```bash
# GUI 模式
python UVR.py

# CLI 模式
python uvr_cli.py list                    # 列出模型
python uvr_cli.py list --downloaded       # 仅已下载
python uvr_cli.py list --missing          # 仅未下载
python uvr_cli.py process 歌曲.mp3 --two-stem vocals   # 分离人声
python uvr_cli.py process 歌曲.mp3 --shifts 5          # 高质量
python uvr_cli.py process 文件夹/ --resume              # 续传
python uvr_cli.py process 歌曲.mp3 --dry-run            # 预览
python uvr_cli.py config --key default_device --value mps  # 设默认设备
python uvr_cli.py config --delete default_device        # 删配置项
python uvr_cli.py config --reset                       # 重置配置
python uvr_cli.py config --export backup.json           # 导出配置
python uvr_cli.py config --import backup.json           # 导入配置
python uvr_cli.py gui
```

## 关键模块说明

### `UVR.py` — 主 GUI 窗口

Tkinter 主窗口类 `MainWindow`，继承自 `DownloadCenterMixin` 和 `_MainWindowBase`，负责：
- 模型选择与管理（VR/MDX/Demucs 三大架构）
- 音频文件导入与处理
- 分离任务执行与进度显示
- 二级模型混合（Secondary Model Mode）
- 集成模式（Ensemble Mode）
- 批量处理（Batch Mode）

### `uvr_cli.py` — 命令行

CLI 入口，14 个命令：`list`, `info`, `process`, `demucs`（已弃用）, `download-models`, `config`, `gui`, `version`, `help`

输出支持 `--json` 参数（AI 友好模式）。

新增 v1.1.0 特性：
- `list --downloaded` / `--missing` 过滤已下载/未下载模型
- `process --shifts N` / `--overlap N` 调节推理质量
- `process --resume` 跳过已完成的文件
- `process --dry-run` 预览不执行
- `process --arch demucs|vr|mdx` 选择分离架构
- `config --delete key` / `--reset` / `--export` / `--import` 增强配置管理

### `separate.py` — 分离引擎

核心音频分离逻辑，包含 `secondary_stem` 映射函数和 `save_format` 格式化函数。

### `gui_data/constants.py` — 全局常量

包含架构类型常量（`VR_ARCH_TYPE`, `MDX_ARCH_TYPE`, `DEMUCS_ARCH_TYPE`）、音轨常量（`VOCAL_STEM`, `INST_STEM`）、`secondary_stem()` 映射函数等。

## CI/CD

- 推送 tag `v*` 自动触发 Windows EXE 构建
- 构建 CPU + CUDA 双版本
- 通过 `workflow_dispatch` 可手动触发
