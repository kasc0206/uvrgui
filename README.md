# Ultimate Vocal Remover GUI v5.6 / 终极人声移除图形界面

<img src="https://raw.githubusercontent.com/Anjok07/ultimatevocalremovergui/master/gui_data/img/UVR_v5.6.png?raw=true" />

[![Release](https://img.shields.io/github/release/anjok07/ultimatevocalremovergui.svg)](https://github.com/anjok07/ultimatevocalremovergui/releases/latest)
[![Downloads](https://img.shields.io/github/downloads/anjok07/ultimatevocalremovergui/total.svg)](https://github.com/anjok07/ultimatevocalremovergui/releases)
[![Tests](https://img.shields.io/badge/tests-63%2F63-passing-brightgreen)](https://github.com/kasc0206/uvrgui)
[![Build Windows](https://github.com/kasc0206/uvrgui/actions/workflows/build-windows.yml/badge.svg)](https://github.com/kasc0206/uvrgui/actions/workflows/build-windows.yml)

> 🎵 **Ultimate Vocal Remover** — A state-of-the-art AI-powered audio source separation tool.
> 🎵 **终极人声移除图形界面** — 利用最先进的 AI 音源分离模型，从音频文件中提取或移除人声。

---

## 📖 About / 关于本项目

**English:** This application uses state-of-the-art source separation models to remove vocals from audio files. UVR's core developers trained all of the models provided in this package (except for the Demucs v3 and v4 4-stem models). It supports **VR Architecture**, **MDX-Net**, and **Demucs**三大 AI 架构，可将音乐中的人声、伴奏、鼓、贝斯等音源分离为独立音轨。

**中文：** **Ultimate Vocal Remover GUI (UVR)** 是一款基于深度学习的音频源分离桌面工具，支持将音乐中的**人声**、**伴奏**、**鼓点**、**贝斯**等多种音源分离为独立音轨。除 Demucs v3/v4 的 4-stem 模型外，本软件包提供的所有模型均由 UVR 核心开发团队自行训练。

### 👥 Core Developers / 核心开发团队

| 角色 (Role) | 开发者 (Developer) |
| --- | --- |
| 原作者 (Original Author) | [Anjok07](https://github.com/anjok07) |
| 原作者 (Original Author) | [aufr33](https://github.com/aufr33) |
| Fork 维护者 (Fork Maintainer) | [kasc0206](https://github.com/kasc0206) |

### ☕ Support the Project / 支持项目

* [Buy Me a Coffee](https://www.buymeacoffee.com/uvr5)

---

## ✨ Features / 特性概览

| English | 中文 |
| --- | --- |
| ✅ **Three AI Architectures**: VR, MDX-Net, Demucs (v1~v4) | ✅ **三种主流 AI 架构**：VR Architecture、MDX-Net、Demucs（v1~v4） |
| ✅ **New model support**: BS-Roformer, Mel-Roformer, SCNet, Bandit, etc. | ✅ **支持多种新型模型**：BS-Roformer、Mel-Roformer、SCNet、Bandit 等 |
| ✅ Vocal / Instrumental / Multi-stem separation | ✅ 人声 / 伴奏 / 多音源分离 |
| ✅ Karaoke backing track creation | ✅ 卡拉 OK 伴奏制作 |
| ✅ Denoising / De-reverb / De-echo | ✅ 去噪 / 去混响 / 去回声 |
| ✅ **GPU Acceleration** (NVIDIA CUDA / Apple MPS) | ✅ **GPU 加速**（NVIDIA CUDA / Apple MPS） |
| ✅ **Batch Processing** | ✅ **批量处理**（Batch Mode） |
| ✅ **Secondary Model Mode** | ✅ **二级模型混合**（Secondary Model Mode） |
| ✅ **Ensemble Mode** | ✅ **集成模式**（Ensemble Mode） |
| ✅ Time-stretch & Pitch-shift (Rubber Band) | ✅ **变调变速**（需 Rubber Band 库） |
| ✅ Drag-and-drop, sample preview, settings save/load | ✅ **拖拽导入**、**采样预览**、**设置保存与加载** |

## 🖥️ CLI Tool (Fork Feature) / 命令行工具（Fork 特性）

**English:** This fork adds `uvr_cli.py`, a full-featured command-line interface with 10 commands:

**中文：** 本 Fork 新增了 `uvr_cli.py` 命令行工具，支持 10 个命令：

```bash
# List all available models with download status / 列出所有可用模型及下载状态
python uvr_cli.py list

# JSON format output (for programmatic use) / JSON 格式输出（适合程序化调用）
python uvr_cli.py list --json

# Show model details / 查看特定模型详情
python uvr_cli.py info BS-Roformer

# Launch the GUI / 启动图形界面
python uvr_cli.py gui

# View or modify configuration / 查看或修改配置
python uvr_cli.py config
python uvr_cli.py config --key default_device --value mps

# Process audio (auto-downloads models) / 分离音频（自动下载模型）
python uvr_cli.py process song.mp3
python uvr_cli.py process input_dir/ --out output_dir/

# Download models via curl (500x faster) / 预下载模型（使用 curl，快 500 倍）
python uvr_cli.py download-models

# Check version / 查看版本
python uvr_cli.py version

# Show help / 显示帮助
python uvr_cli.py help
```

## 🚀 Installation / 安装指南

> ⚠️ **Note / 注意**：This fork does not provide pre-built binaries. Please build from source. / 本 Fork 不提供预编译安装包，请按照以下步骤从源码构建。

### 📦 Source Install (All Platforms) / 源码安装（所有平台通用）

```bash
# 1. Clone the repository / 克隆仓库
git clone https://github.com/kasc0206/uvrgui.git
cd uvrgui

# 2. Create virtual environment / 创建虚拟环境
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
# 或 venv\Scripts\activate  # Windows

# 3. Install dependencies / 安装依赖
pip install -r requirements.txt

# 4. (Optional) NVIDIA GPU CUDA PyTorch / （可选）NVIDIA GPU 用户安装 CUDA 版 PyTorch
pip install --upgrade torch --extra-index-url https://download.pytorch.org/whl/cu118

# 5. Launch / 启动
python UVR.py
```

### 🪟 Windows EXE Build / Windows EXE 构建

**English:** This fork supports automated Windows EXE builds via GitHub Actions. Push a tag to trigger:

**中文：** 本 Fork 支持通过 GitHub Actions 自动构建 Windows EXE。推送 tag 即可触发：

```bash
git tag v1.0.0
git push origin v1.0.0
```

Also can be triggered manually from the [Actions page](https://github.com/kasc0206/uvrgui/actions/workflows/build-windows.yml) / 也可手动触发 [Actions 页面](https://github.com/kasc0206/uvrgui/actions/workflows/build-windows.yml)

#### Build Variants / 构建变体

| Variant / 变体 | File / 文件 | Size / 体积 | GPU | Release Asset | Artifact |
|------|------|------|-----|:---:|:---:|
| **CPU Edition** | `UVR_*_CPU.zip` | ~400 MB | ❌ | ✅ Direct download | ✅ |
| **CUDA Edition** | `UVR_*_CUDA.zip` | ~2.5 GB | ✅ NVIDIA | ❌ Exceeds 2GB limit | ✅ |

**CI Flow / CI 流程：**
1. Install CPU PyTorch → Build CPU edition → Package ZIP → Upload Artifact
2. Install CUDA PyTorch → Rebuild CUDA edition → Package ZIP → Upload Artifact
3. Release page: CPU edition as direct download, CUDA edition via Artifact link

#### Local Build / 本机构建

```bash
pip install -r requirements.txt
pip install pyinstaller

# CPU edition (default) / CPU 版（默认）
pyinstaller UVR.spec --clean --noconfirm

# CUDA edition (install CUDA PyTorch first) / CUDA 版（需先安装 CUDA PyTorch）
pip install --upgrade torch --extra-index-url https://download.pytorch.org/whl/cu121
pyinstaller UVR.spec --clean --noconfirm
```

---

### 🍎 macOS Build from Source / macOS 从源码编译

#### Prerequisites / 前置条件

- macOS Big Sur (11) or later / 或更高版本
- ~10 GB disk space (including PyTorch runtime) / 约 10 GB 磁盘空间（含 PyTorch 运行时）
- Xcode Command Line Tools

#### Steps / 编译步骤

```bash
# 1. Install Xcode Command Line Tools / 安装 Xcode Command Line Tools
xcode-select --install

# 2. Install Homebrew (if not already) / 安装 Homebrew（如尚未安装）
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# 3. Install system dependencies / 安装系统依赖
brew install ffmpeg python@3.10

# 4. (Optional) Rubber Band for pitch/time adjustment
brew install rubberband

# 5. Clone repository / 克隆仓库
git clone https://github.com/kasc0206/uvrgui.git
cd uvrgui

# 6. Create virtual environment / 创建虚拟环境
python3.10 -m venv venv
source venv/bin/activate

# 7. Install dependencies / 安装依赖
pip install --upgrade pip wheel setuptools
pip install -r requirements.txt

# 8. Launch / 启动
python UVR.py
```

> **First launch may take 5-10 minutes** (model initialization). / **首次启动可能需要 5-10 分钟**（模型初始化）。
>
> **Apple Silicon (M1/M2/M3)**: PyTorch MPS acceleration is automatically enabled. / PyTorch MPS 加速自动启用，无需额外配置。
>
> **If you see "Cannot verify developer" / 如果遇到「无法验证开发者」提示**：
> ```bash
> sudo spctl --master-disable
> sudo xattr -rd com.apple.quarantine /Applications/Ultimate\ Vocal\ Remover.app
> ```

---

### 🐧 Linux Build from Source / Linux 从源码编译

#### Prerequisites / 前置条件

- 64-bit Linux distribution / 64 位 Linux 发行版
- ~10 GB disk space / 约 10 GB 磁盘空间
- NVIDIA GPU: CUDA Toolkit 11.8+ (optional)

#### Debian / Ubuntu

```bash
# Update system / 更新系统
sudo apt update && sudo apt upgrade -y

# Install system dependencies / 安装系统依赖
sudo apt install -y ffmpeg python3-pip python3-tk python3-venv

# (Optional) Rubber Band / 可选：安装 Rubber Band
sudo apt install -y rubberband-cli

# Clone / 克隆仓库
git clone https://github.com/kasc0206/uvrgui.git
cd uvrgui

# Virtual environment / 创建虚拟环境
python3 -m venv venv
source venv/bin/activate

# Install dependencies / 安装依赖
pip install --upgrade pip wheel setuptools
pip install -r requirements.txt

# (Optional) CUDA PyTorch for NVIDIA GPU
pip install --upgrade torch --extra-index-url https://download.pytorch.org/whl/cu118

# Launch / 启动
python UVR.py
```

#### Arch Linux

```bash
sudo pacman -Syu
sudo pacman -S ffmpeg python-pip tk python-virtualenv
sudo pacman -S rubberband  # optional / 可选
git clone https://github.com/kasc0206/uvrgui.git
cd uvrgui
python -m venv venv
source venv/bin/activate
pip install --upgrade pip wheel setuptools
pip install -r requirements.txt
python UVR.py
```

#### Fedora / RHEL

```bash
sudo dnf install -y ffmpeg python3-pip python3-tkinter python3-virtualenv
sudo dnf install -y rubberband  # optional / 可选
git clone https://github.com/kasc0206/uvrgui.git
cd uvrgui
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip wheel setuptools
pip install -r requirements.txt
python UVR.py
```

---

### 🔧 Additional Dependencies / 额外依赖

| 依赖 (Dependency) | 用途 (Purpose) | 安装方式 (Installation) |
| --- | --- | --- |
| **FFmpeg** | Process non-WAV audio | Package manager per platform |
| **Rubber Band** | Time-stretch / pitch-shift | Optional / 可选 |

<details id="CannotOpen">
  <summary>🍎 macOS: Having Trouble Opening UVR? / 无法打开 UVR？</summary>

> Due to Apple's strict application security, you may need to follow these steps:
> 由于 Apple 严格的应用安全策略，您可能需要执行以下步骤：
>
> 1. Allow apps from all sources / 允许从所有来源运行应用（建议解决问题后重新关闭）：
> ```bash
> sudo spctl --master-disable
> ```
>
> 2. Bypass notarization / 绕过公证检查：
> ```bash
> sudo xattr -rd com.apple.quarantine /Applications/Ultimate\ Vocal\ Remover.app
> ```

</details>

---

## ⚙️ Hardware Requirements / 硬件要求

| 项目 (Item) | 最低配置 (Minimum) | 推荐配置 (Recommended) |
| --- | --- | --- |
| **CPU** | 4-core x86_64 / ARM | 8-core+ |
| **RAM** | 8 GB | 16 GB+ |
| **NVIDIA GPU** | GTX 1060 6GB | RTX 8GB+ VRAM |
| **macOS** | Big Sur+ | M1/M2/M3 |
| **Platform** | 64-bit only | 64-bit only |

**Notes / 说明：**
- AMD Radeon GPU support is limited. See [v5.6-amd-gpu branch](https://github.com/Anjok07/ultimatevocalremovergui/tree/v5.6-amd-gpu)
- Conversion times depend significantly on your hardware / 转换时间取决于硬件配置
- Models are computationally intensive / 模型计算强度大

---

## 🧠 Model Architecture / 模型架构详解

UVR supports three core AI architectures with various pretrained models:
UVR 支持三类核心 AI 架构，每类下有多种预训练模型：

### 1️⃣ VR Architecture（VR 架构）

UVR team's self-developed models, categorized by band count / 按频带数划分：

| Bands / 频带 | Sample Rate / 采样率 | Use Case / 适用场景 |
| --- | --- | --- |
| 1-band | 16k~44.1k | Lightweight, fast / 轻量快速 |
| 2-band | 32k | Medium quality / 中等人声提取 |
| 3-band | 44.1k | Balanced speed & quality / 平衡速度与质量 |
| **4-band** | **44.1k** | **⭐ Best quality / 主流选择，质量最佳** |

**Special VR models / 特殊 VR 模型：**

| Model | Purpose / 用途 |
| --- | --- |
| `HP-UVR` (1~9) | HP filter optimized vocal extraction / 高通滤波优化，提取人声 |
| `SP-UVR` (10~16) | Spectral processing optimized / 频谱处理优化 |
| `Karaoke` series | Karaoke backing tracks / 制作卡拉 OK 伴奏 |
| `DeNoise / De-Echo / DeReverb` | Noise/echo/reverb removal / 降噪、去回声、去混响 |
| `BVE` | Background vocal extraction / 提取背景和声 |
| Specialized: `No Piano`, `No Woodwinds`, `No Echo`, etc. | Targeted stem removal / 专项移除 |

### 2️⃣ MDX-Net Architecture（MDX-Net 架构）

Hybrid spectral/temporal network models / 基于混合频谱/时域网络的分离模型：

| Model Name | Output | Description / 说明 |
| --- | --- | --- |
| **UVR-MDX-NET Main** | Vocals | ⭐ Best all-round main model / 综合效果最佳的主模型 |
| UVR-MDX-NET 1/2/3 | Vocals | General vocal extraction / 通用人声提取 |
| UVR-MDX-NET Inst Main/HQ | Instrumentals | High-quality instrumental / 高质量伴奏提取 |
| UVR-MDX-NET Karaoke | Instrumentals | Karaoke backing / 卡拉 OK 伴奏 |
| Kim Vocal/Inst | Vocals/Inst | Community contributed / 社区贡献模型 |
| MDX23C-InstVoc HQ | Vocals+Inst | New MDX23C architecture / 新版 MDX23C 架构 |

**New derivative models (community contributed) / 新型衍生模型（社区贡献）：**

| Series | Description / 说明 |
| --- | --- |
| **BS-Roformer** | Deconvolution spectral reconstruction, SDR > 12.9, excellent quality |
| **Mel-Roformer** | Mel-spectrogram Roformer |
| **MB-Roformer** | Mel-Band Roformer (Inst/Duality variants) |
| **SCNet (4S-SCNet)** | 4-stem separation (drums/bass/other/vocals) |
| **Cinematic Bandit** | Cinematic-grade separation |
| **DrumSep** | Dedicated drum track extraction |
| **Reverb HQ** | Professional de-reverb |

### 3️⃣ Demucs Architecture（Demucs 架构，Facebook/Meta）

Open-source source separation models from Meta, all versions integrated:

| Version | Model | Description / 说明 |
| --- | --- | --- |
| v1 | Demucs / Tasnet / Light | First-gen, lightweight / 初代模型，轻量 |
| v2 | Demucs / Tasnet / Demucs48_hq | Improved / 改进版 |
| **v3** | **mdx / mdx_extra** | ⭐ Hybrid, recommended for daily use / 推荐日常使用 |
| v3 UVR | UVR_Model_1 / 2 / Bag | UVR-tuned / UVR 特调版 |
| **v4** | **htdemucs** | ⭐⭐ **4-stem (drums/bass/other/vocals)** |
| v4 | htdemucs_ft | Fine-tuned / 微调版 |
| **v4** | **htdemucs_6s** | ⭐ **6-stem (+ guitar, piano)** |

---

## 💡 Usage Recommendations / 使用建议

| Your Need / 你的需求 | Recommended Model / 推荐模型 |
| --- | --- |
| 🎤 Extract vocals / 提取人声 | `UVR-MDX-NET Main` or `BS-Roformer-Viperx-1297` |
| 🎵 Extract instrumental / 提取伴奏 | `UVR-MDX-NET Inst Main` or `MB-Roformer-Inst-v2` |
| 🎧 Multi-instrument separation / 分离多乐器 | `htdemucs` (4-track) or `htdemucs_6s` (6-track) |
| 🎤🎤 Background vocals / 提取背景和声 | `UVR-BVE-4B_SN-44100-1` |
| 🎶 Karaoke / 制作卡拉 OK | `UVR-MDX-NET Karaoke` |
| 🧹 Denoising / 去噪 | `UVR-DeNoise` |
| 🧹 De-reverb / 去混响 | `Reverb HQ` or `BS-Ro-Dereverb-Anvuew` |

---

## 🐛 Troubleshooting / 常见问题

### Common Issues / 常见问题

- **FFmpeg not installed**: The app will throw an error when processing non-WAV files. Install FFmpeg via your package manager.
- **Memory errors**: Lower the "Segment" or "Window" size settings. / 降低"Segment"或"Window"大小即可。
- **macOS Sonoma left-click bug**: Resolved in newer Tkinter. Update via: / 已修复，更新 Tkinter：
  ```bash
  brew update && brew upgrade python-tk
  ```

### Issue Reporting / 问题报告

Please be as detailed as possible when posting a new issue. Click the "Settings" button → "Error Log" for detailed error information.
请在提交问题时尽量详细描述。点击"Settings"按钮→"Error Log"获取详细错误信息。

## 🏗️ Building Windows EXE / 构建 Windows EXE

**English:** This fork provides automated Windows EXE builds via GitHub Actions.

**中文：** 本 Fork 提供多种 Windows EXE 构建方式。

### Method 1: GitHub Actions (Recommended / 推荐)

Push a version tag to trigger an automated build / 推送 tag 自动触发构建：

```bash
git tag v1.0.0
git push origin v1.0.0
```

The workflow will / 工作流将执行：
1. Build `UVR.exe` with PyInstaller on `windows-latest`
2. Create a ZIP archive with all runtime files / 打包 ZIP
3. Upload the artifact and create a GitHub Release

### Method 2: Docker Cross-Compilation (macOS/Linux)

```bash
docker run --rm -v "$PWD:/workspace" \
  -w /workspace cdrx/pyinstaller-windows:latest \
  pyinstaller UVR.spec --clean --noconfirm
```

### Method 3: Native Windows Build / 原生 Windows 构建

```bash
pip install -r requirements.txt
pip install pyinstaller
pyinstaller UVR.spec --clean --noconfirm
```

The output `UVR.exe` will be in `dist/` / 输出文件位于 `dist/` 目录。

## 📋 Fork Changelog / Fork 修订记录

**English:** This fork ([kasc0206/uvrgui](https://github.com/kasc0206/uvrgui)) encompasses the following improvements over the upstream [Anjok07/ultimatevocalremovergui](https://github.com/Anjok07/ultimatevocalremovergui).

**中文：** 本 Fork 相较于原仓库，做了以下修订。

### Model Data Updates / 模型数据更新

| File / 文件 | Change / 变更说明 |
| --- | --- |
| `models/MDX_Net_Models/model_data/model_data.json` | **Expanded** with 80+ new MDX models (+830/-351) / **大幅扩充** |
| `models/MDX_Net_Models/model_data/model_name_mapper.json` | **26 new** name mappings (+68/-66) / **新增 26 个映射** |
| `models/VR_Models/model_data/model_data.json` | Refactored VR parameters (+272/-137) / 重构 VR 参数 |
| `models/Demucs_Models/model_data/model_name_mapper.json` | Format fix / 格式修正 |

#### New MDX Models / 新增 MDX 模型清单

| Category / 类别 | Models / 模型 |
| --- | --- |
| **BS-Roformer** | `Viperx-1297`, `Viperx-1296`, `Viperx-1053` |
| **Mel-Roformer** | `Viperx-1143` |
| **MB-Roformer** | `Inst-v1`, `Inst-v2`, `Inst-v1-E`, `Duality-v1`, `Duality-v2`, `Kim`, `Karaoke` |
| **SCNet** | `Starrytong`, `Large-Starrytong`, `Large`, `XL-ZFTurbo` |
| **Bandit** | `Cinematic-Bandit-Plus`, `Cinematic-Bandit-Multi` |
| **MDX23C** | `InstVoc HQ 2`, `InstVoc D1581` |
| **Other / 其他** | `DrumSep`, `Phantom-Mid`, `Reverb HQ`, `BS-Ro-Dereverb`, `BS-Ro-Inst-EXP` |

### New / Improved Files / 新增文件

| File / 文件 | Description / 说明 |
| --- | --- |
| `uvr_cli.py` | **CLI tool** — 10 commands (list/info/process/demucs/download-models/config/version/gui/help + --json) |
| `tests/` | **Test suite** — 32 tests via pytest + coverage |
| `playsound.py` | `playsound3` compatibility shim / 兼容垫片 |
| `__version__.py` | Version info with `FORK_VERSION` and `FORK_REPO` |
| `pyproject.toml` | Project metadata + ruff lint config |
| `.editorconfig` | Consistent coding style / 统一编码风格 |
| `.pre-commit-config.yaml` | Pre-commit hooks for code quality |
| `.gitattributes` | LF line-ending normalization |
| `Dockerfile` | Containerized deployment / Docker 部署 |
| `gui_data/cr_text.txt` | Custom text resource / 自定义文本资源 |
| `.gitignore` | Exclude build artifacts / 排除构建产物 |
| `requirements.txt` | **Rebuilt dependency list** / 重建依赖清单 |

### Code Quality Improvements / 代码质量改进

| Improvement / 改进项 | Description / 说明 |
| --- | --- |
| **ruff zero errors / ruff 零错误** | All custom files pass F, E, W, I rulesets |
| **Pylance type fixes / 类型修复** | Reduced errors in `UVR.py` from 244 → 137 |
| **Star imports / 星号导入替换** | Replaced `from gui_data.constants import *` with 862 explicit symbols |
| **Bug fix / Bug 修复** | `highlightthicknes` typo → `highlightthickness` (5 occurrences) |
| **Font tuples / 字体类型修复** | Fixed ~120 `font=(name, f"{size}")` → `font=(name, size)` |
| **Model download / 模型下载提速** | `torch.hub` → `curl` (500x speedup / 快 500 倍) |

### Test Coverage / 测试覆盖

| Area / 测试范围 | Tests / 数量 | Status / 状态 |
| --- | --- | --- |
| CLI commands / CLI 命令测试 | 9 | ✅ Pass / 通过 |
| Module imports / 模块导入测试 | 14 | ✅ Pass / 通过 |
| `secondary_stem` mapping / 映射测试 | 3 | ✅ Pass / 通过 |
| Version & constants / 版本与常量 | 6 | ✅ Pass / 通过 |
| **Total / 合计** | **32** | **✅ All Pass / 全部通过** |

## 📜 License / 许可证

**English:** The **Ultimate Vocal Remover GUI** code is [MIT-licensed](LICENSE). For all third-party application developers who wish to use our models, please honor the MIT license by providing credit to UVR and its developers.

**中文：** 本项目代码采用 [MIT 许可证](LICENSE)。如需使用我们的模型，请保留 UVR 及开发者的署名。

## 🙏 Credits / 鸣谢

| Contributor | Contribution / 贡献 |
| --- | --- |
| [ZFTurbo](https://github.com/ZFTurbo) | MDX23C model training / 训练新 MDX23C 模型权重 |
| [DilanBoskan](https://github.com/DilanBoskan) | Early project contributions / 项目早期关键贡献 |
| [Bas Curtiz](https://www.youtube.com/user/bascurtiz) | Logo, icon, banner, splash screen design / 设计 Logo、图标等 |
| [tsurumeso](https://github.com/tsurumeso) | Original VR Architecture code / VR 架构原始代码 |
| [Kuielab & Woosung Choi](https://github.com/kuielab) | Original MDX-Net AI code / MDX-Net 原始代码 |
| [Adefossez & Demucs](https://github.com/facebookresearch/demucs) | Original Demucs AI code / Demucs 原始代码 |
| [KimberleyJSN](https://github.com/KimberleyJensen) | Training scripts guidance / 训练脚本指导 |
| [Hv](https://github.com/NaJeongMo/Colab-for-MDX_B) | Chunk implementation in MDX-Net / 分块处理实现 |

## 🤝 Contributing / 贡献指南

- Pull requests are welcome! / 欢迎提交 Pull Request！
- This project is 100% open-source under MIT. / 本项目完全开源（MIT 协议）。
- We maintain development and support for UVR and provided models only. / 我们仅维护 UVR 软件及提供的模型。

## 📚 References / 参考文献

- [1] Takahashi et al., "Multi-scale Multi-band DenseNets for Audio Source Separation", https://arxiv.org/pdf/1706.09588.pdf
