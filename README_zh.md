# Ultimate Vocal Remover GUI v5.6 — 中文版

![UVR Banner](https://raw.githubusercontent.com/Anjok07/ultimatevocalremovergui/master/gui_data/img/UVR_v5.6.png)

[![Release](https://img.shields.io/github/release/anjok07/ultimatevocalremovergui.svg)](https://github.com/anjok07/ultimatevocalremovergui/releases/latest)
[![Downloads](https://img.shields.io/github/downloads/anjok07/ultimatevocalremovergui/total.svg)](https://github.com/anjok07/ultimatevocalremovergui/releases)
[![Tests](https://img.shields.io/badge/tests-63%2F63-%E9%80%9A%E8%BF%87-brightgreen)](https://github.com/kasc0206/uvrgui)
[![Ruff](https://img.shields.io/badge/ruff-%E9%9B%B6%E9%94%99%E8%AF%AF-brightgreen)](https://github.com/kasc0206/uvrgui)

> 🎵 **终极人声移除图形界面** — 利用最先进的音源分离模型，从音频文件中提取或移除人声。

---

## 📖 关于本项目

**Ultimate Vocal Remover GUI (UVR)** 是一款基于深度学习的音频源分离工具，支持将音乐中的**人声**、**伴奏**、**鼓点**、**贝斯**等多种音源分离为独立音轨。

除 Demucs v3/v4 的 4-stem 模型外，本软件包提供的所有模型均由 UVR 核心开发团队自行训练。

### 👥 核心开发团队

| 角色 | 开发者 |
| --- | --- |
| 原作者 | [Anjok07](https://github.com/anjok07) |
| 原作者 | [aufr33](https://github.com/aufr33) |
| Fork 维护者 | [kasc0206](https://github.com/kasc0206) |

### ☕ 支持项目

* [Buy Me a Coffee](https://www.buymeacoffee.com/uvr5)

---

## ✨ 特性概览

* ✅ **三种主流 AI 架构**：VR Architecture、MDX-Net、Demucs（v1~v4）
* ✅ **支持多种新型模型**：BS-Roformer、Mel-Roformer、SCNet、Bandit 等
* ✅ **人声 / 伴奏 / 多音源分离**
* ✅ **卡拉 OK 伴奏制作**
* ✅ **去噪 / 去混响 / 去回声**
* ✅ **GPU 加速**（NVIDIA CUDA / Apple MPS）
* ✅ **批量处理**（Batch Mode）
* ✅ **二级模型混合**（Secondary Model Mode）
* ✅ **集成模式**（Ensemble Mode）
* ✅ **变调变速**（需 Rubber Band 库）
* ✅ **拖拽导入**、**采样预览**、**设置保存与加载**

---

## 🚀 安装指南

> ⚠️ **注意**：本 Fork 不提供预编译安装包。请按照以下步骤从源码构建。

### 📦 源码安装（所有平台通用）

```bash
# 1. 克隆仓库
git clone https://github.com/kasc0206/uvrgui.git
cd uvrgui

# 2. 创建虚拟环境
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
# 或 venv\Scripts\activate  # Windows

# 3. 安装依赖
pip install -r requirements.txt

# 4. （可选）NVIDIA GPU 用户安装 CUDA 版 PyTorch
pip install --upgrade torch --extra-index-url https://download.pytorch.org/whl/cu118

# 5. 启动
python UVR.py
```

### 🪟 Windows EXE 构建

本 Fork 支持通过 GitHub Actions 自动构建 Windows EXE。推送 tag 即可触发：

```bash
git tag v1.0.0
git push origin v1.0.0
```

也可手动触发 [Actions 页面](https://github.com/kasc0206/uvrgui/actions/workflows/build-windows.yml)

#### 构建变体

每次推送 tag 后，CI 会自动构建两个版本：

| 变体 | 文件 | 体积 | GPU | Release 附件 | Artifact |
|------|------|------|-----|:---:|:---:|
| **CPU 版** | `UVR_*_CPU.zip` | ~400 MB | ❌ | ✅ 直接下载 | ✅ |
| **CUDA 版** | `UVR_*_CUDA.zip` | ~2.5 GB | ✅ NVIDIA | ❌ 超 2GB 限制 | ✅ |

CI 流程：
1. 先安装 CPU PyTorch → 编译 CPU 版 → 打包 ZIP → 上传 Artifact
2. 再安装 CUDA PyTorch → 重新编译 CUDA 版 → 打包 ZIP → 上传 Artifact
3. Release 页面：CPU 版作为附件直接下载，CUDA 版提供 Artifact 链接

#### 本机构建

```bash
pip install -r requirements.txt
pip install pyinstaller

# CPU 版（默认）
pyinstaller UVR.spec --clean --noconfirm

# CUDA 版（需先安装 CUDA PyTorch）
pip install --upgrade torch --extra-index-url https://download.pytorch.org/whl/cu121
pyinstaller UVR.spec --clean --noconfirm
```

---

### 🍎 macOS 从源码编译

#### 前置条件

- macOS Big Sur (11) 或更高版本
- 约 10 GB 磁盘空间
- Xcode Command Line Tools

#### 编译步骤

```bash
# 1. 安装 Xcode Command Line Tools
xcode-select --install

# 2. 安装 Homebrew（如尚未安装）
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# 3. 安装系统依赖
brew install ffmpeg python@3.10

# 4. 可选：安装 Rubber Band（变调变速功能）
brew install rubberband

# 5. 克隆仓库
git clone https://github.com/kasc0206/uvrgui.git
cd uvrgui

# 6. 创建虚拟环境
python3.10 -m venv venv
source venv/bin/activate

# 7. 安装 Python 依赖
pip install --upgrade pip wheel setuptools
pip install -r requirements.txt

# 8. 启动图形界面
python UVR.py
```

> **首次启动可能需要 5-10 分钟**（模型与 PyTorch 初始化）。
>
> **Apple Silicon (M1/M2/M3)**：PyTorch MPS 加速自动启用，无需额外配置。
>
> **如果遇到「无法验证开发者」提示**：
> ```bash
> sudo spctl --master-disable
> sudo xattr -rd com.apple.quarantine /Applications/Ultimate\ Vocal\ Remover.app
> ```

---

### 🐧 Linux 从源码编译

#### 前置条件

- 64 位 Linux 发行版
- 约 10 GB 磁盘空间
- NVIDIA GPU 用户：CUDA Toolkit 11.8+（可选）

#### Debian / Ubuntu 系

```bash
# 1. 更新系统
sudo apt update && sudo apt upgrade -y

# 2. 安装系统依赖
sudo apt install -y ffmpeg python3-pip python3-tk python3-venv

# 3. 可选：安装 Rubber Band（变调变速功能）
sudo apt install -y rubberband-cli

# 4. 克隆仓库
git clone https://github.com/kasc0206/uvrgui.git
cd uvrgui

# 5. 创建虚拟环境
python3 -m venv venv
source venv/bin/activate

# 6. 安装 Python 依赖
pip install --upgrade pip wheel setuptools
pip install -r requirements.txt

# 7. NVIDIA GPU 用户安装 CUDA PyTorch（可选）
pip install --upgrade torch --extra-index-url https://download.pytorch.org/whl/cu118

# 8. 启动
python UVR.py
```

#### Arch Linux 系

```bash
# 1. 更新系统
sudo pacman -Syu

# 2. 安装系统依赖
sudo pacman -S ffmpeg python-pip tk python-virtualenv

# 3. 可选：安装 Rubber Band（变调变速功能）
sudo pacman -S rubberband

# 4. 克隆仓库
git clone https://github.com/kasc0206/uvrgui.git
cd uvrgui

# 5. 创建虚拟环境
python -m venv venv
source venv/bin/activate

# 6. 安装依赖
pip install --upgrade pip wheel setuptools
pip install -r requirements.txt

# 7. 启动
python UVR.py
```

#### Fedora / RHEL 系

```bash
# 1. 安装系统依赖
sudo dnf install -y ffmpeg python3-pip python3-tkinter python3-virtualenv

# 2. 可选：安装 Rubber Band
sudo dnf install -y rubberband

# 3. 克隆仓库
git clone https://github.com/kasc0206/uvrgui.git
cd uvrgui

# 4. 创建虚拟环境
python3 -m venv venv
source venv/bin/activate

# 5. 安装依赖
pip install --upgrade pip wheel setuptools
pip install -r requirements.txt

# 6. 启动
python UVR.py
```

---

### 🔧 额外依赖

| 依赖 | 用途 | 安装方式 |
| --- | --- | --- |
| **FFmpeg** | 处理非 WAV 格式音频 | 各平台包管理器安装 |
| **Rubber Band** | 变调/变速功能 | 可选，非必需 |

---

## 🧠 模型架构详解

UVR 支持三类核心 AI 架构，每类下有多种预训练模型：

### 1️⃣ VR Architecture（VR 架构）

UVR 团队自研的模型，按频带数划分：

| 频带 | 采样率 | 适用场景 |
| --- | --- | --- |
| 1-band | 16k~44.1k | 轻量快速，适合简单分离 |
| 2-band | 32k | 中等质量人声提取 |
| 3-band | 44.1k | 平衡速度与质量 |
| **4-band** | **44.1k** | **⭐ 主流选择，质量最佳** |

**特殊 VR 模型：**

* `HP-UVR` (1~9号) — 高通滤波优化，提取人声
* `SP-UVR` (10~16号) — 频谱处理优化
* `Karaoke` 系列 — 制作卡拉 OK 伴奏
* `DeNoise / De-Echo / DeReverb` — 降噪、去回声、去混响
* `BVE` — 提取背景和声
* 专项模型：`No Piano`、`No Woodwinds`、`No Echo` 等

### 2️⃣ MDX-Net 架构

基于混合频谱/时域网络的分离模型：

| 模型名称 | 输出 | 说明 |
| --- | --- | --- |
| **UVR-MDX-NET Main** | 人声 | ⭐ 综合效果最佳的主模型 |
| UVR-MDX-NET 1/2/3 | 人声 | 通用人声提取 |
| UVR-MDX-NET Inst Main/HQ | 伴奏 | 高质量伴奏提取 |
| UVR-MDX-NET Karaoke | 伴奏 | 卡拉 OK 伴奏 |
| Kim Vocal/Inst | 人声/伴奏 | 社区贡献模型 |
| MDX23C-InstVoc HQ | 人声+伴奏 | 新版 MDX23C 架构 |

**新型衍生模型（社区贡献）：**

| 模型系列 | 说明 |
| --- | --- |
| **BS-Roformer** | 反卷积频谱重建，SDR > 12.9，分离质量极高 |
| **Mel-Roformer** | Mel 频谱 Roformer |
| **MB-Roformer** | Mel-Band Roformer，有 Inst/Duality 等多种变体 |
| **SCNet (4S-SCNet)** | 4 音源分离（鼓/贝斯/其他/人声） |
| **Cinematic Bandit** | 影院级分离效果 |
| **DrumSep** | 专门提取鼓点音轨 |
| **Reverb HQ** | 专业去混响 |

### 3️⃣ Demucs 架构（Facebook/Meta）

Meta 开源的音源分离模型，UVR 集成了全部版本：

| 版本 | 模型 | 说明 |
| --- | --- | --- |
| v1 | Demucs / Tasnet / Light | 初代模型，轻量 |
| v2 | Demucs / Tasnet / Demucs48_hq | 改进版 |
| **v3** | **mdx / mdx_extra** | ⭐ 混合模型，推荐日常使用 |
| v3 UVR | UVR_Model_1 / 2 / Bag | UVR 特调版 |
| **v4** | **htdemucs** | ⭐⭐ **4-stem 分离（鼓/贝斯/其他/人声）** |
| v4 | htdemucs_ft | Fine-tuned 微调版 |
| **v4** | **htdemucs_6s** | ⭐ **6-stem 版（+吉他、钢琴）** |

---

## 💡 使用建议

| 你的需求 | 推荐模型 |
| --- | --- |
| 🎤 提取人声 | `UVR-MDX-NET Main` 或 `BS-Roformer-Viperx-1297` |
| 🎵 提取伴奏 | `UVR-MDX-NET Inst Main` 或 `MB-Roformer-Inst-v2` |
| 🎧 分离多乐器 | `htdemucs`（4轨）或 `htdemucs_6s`（6轨） |
| 🎤🎤 提取背景和声 | `UVR-BVE-4B_SN-44100-1` |
| 🎶 制作卡拉 OK | `UVR-MDX-NET Karaoke` |
| 🧹 去噪 | `UVR-DeNoise` |
| 🧹 去混响 | `Reverb HQ` 或 `BS-Ro-Dereverb-Anvuew` |

---

## 🖥️ 界面功能速览

### 图形界面（GUI）

* **Select Input** — 选择输入音频文件或文件夹
* **Select Output** — 选择输出目录
* **Download More Models** — 下载更多预训练模型
* **Start Processing** — 开始处理
* **Batch Mode** — 批量处理模式（更高效）
* **Secondary Model** — 二级模型混合（调整分离倾向）
* **Ensemble Mode** — 集成模式（多模型组合）
* **Sample Mode** — 仅处理音频片段预览效果

### 命令行工具（CLI）

本 Fork 新增了 `uvr_cli.py` 命令行工具，支持 10 个命令：

```bash
# 列出所有可用模型及下载状态
python uvr_cli.py list

# JSON 格式输出（适合程序化调用）
python uvr_cli.py list --json

# 查看特定模型详情
python uvr_cli.py info BS-Roformer

# 启动图形界面
python uvr_cli.py gui

# 查看或修改配置
python uvr_cli.py config
python uvr_cli.py config --key default_device --value mps

# 使用 Demucs 分离音频（自动下载模型）
python uvr_cli.py process 歌曲.mp3
python uvr_cli.py demucs 歌曲.flac --two-stem vocals
python uvr_cli.py process 输入文件夹/ --out 输出文件夹/

# 预下载 Demucs 模型（使用 curl，快 500 倍）
python uvr_cli.py download-models

# 查看版本
python uvr_cli.py version

# 显示帮助
python uvr_cli.py help
```

---

## ⚙️ 硬件要求

| 项目 | 最低配置 | 推荐配置 |
| --- | --- | --- |
| **CPU** | 4 核 x86_64 / ARM | 8 核及以上 |
| **内存** | 8 GB | 16 GB+ |
| **NVIDIA GPU** | GTX 1060 6GB | RTX 8GB+ V-RAM |
| **macOS** | Big Sur+ | M1/M2/M3 |
| **系统** | 64 位 | 64 位 |

---

## 🐛 常见问题

### FFmpeg 未安装

处理非 WAV 格式文件时会报错。请通过包管理器安装 FFmpeg：

```bash
# macOS
brew install ffmpeg

# Linux
sudo apt install ffmpeg  # Debian/Ubuntu
sudo pacman -S ffmpeg    # Arch

# Windows
# 下载 https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip
```

### 内存不足

降低 **"Segment"** 或 **"Window"** 大小即可。

### macOS Sonoma 鼠标点击问题

已修复。如仍有问题请下载最新版本。

---

## 🔄 本 Fork 修订记录

相较于原仓库 [Anjok07/ultimatevocalremovergui](https://github.com/Anjok07/ultimatevocalremovergui)，本 Fork 做了以下修订：

### 模型数据更新

| 文件 | 变更说明 |
| --- | --- |
| `models/MDX_Net_Models/model_data/model_data.json` | **大幅扩充**，新增大量新型 MDX 模型配置（+830/-351） |
| `models/MDX_Net_Models/model_data/model_name_mapper.json` | **新增 26 个模型名称映射**（+68/-66） |
| `models/VR_Models/model_data/model_data.json` | 重构并更新 VR 模型参数配置（+272/-137） |
| `models/Demucs_Models/model_data/model_name_mapper.json` | 格式修正，添加文件末尾换行（+66/-66） |

#### 新增 MDX 模型清单

| 类别 | 模型 |
| --- | --- |
| **BS-Roformer** | `Viperx-1297`、`Viperx-1296`、`Viperx-1053` |
| **Mel-Roformer** | `Viperx-1143` |
| **MB-Roformer** | `Inst-v1`、`Inst-v2`、`Inst-v1-E`、`Duality-v1`、`Duality-v2`、`Kim`、`Karaoke` |
| **SCNet** | `Starrytong`、`Large-Starrytong`、`Large`、`XL-ZFTurbo` |
| **Bandit** | `Cinematic-Bandit-Plus`、`Cinematic-Bandit-Multi` |
| **MDX23C** | `InstVoc HQ 2`、`InstVoc D1581` |
| **其他** | `DrumSep`、`Phantom-Mid`、`Reverb HQ`、`BS-Ro-Dereverb`、`BS-Ro-Inst-EXP` |

### 代码质量改进

| 改进项 | 说明 |
| --- | --- |
| **ruff 零错误** | 所有自定义文件通过 F、E、W、I 规则集检查 |
| **Pylance 类型修复** | `UVR.py` 错误从 244 减少到 137（修复真实 bug，剩余为 tkinter/PyTorch 动态类型限制） |
| **星号导入替换** | `from gui_data.constants import *` → 862 个精确符号导入 |
| **Bug 修复** | `highlightthicknes` tkinter 参数拼写错误 → `highlightthickness`（5 处） |
| **字体类型修复** | ~120 处 `font=(name, f"{size}")` → `font=(name, size)` |
| **模型下载提速** | `torch.hub.load_state_dict_from_url` → `curl`（快 500 倍） |

### 测试覆盖

| 测试范围 | 数量 | 状态 |
| --- | --- | --- |
| CLI 命令测试 | 9 | ✅ 通过 |
| 模块导入测试 | 14 | ✅ 通过 |
| `secondary_stem` 映射 | 3 | ✅ 通过 |
| 版本与常量 | 6 | ✅ 通过 |
| **合计** | **32** | **✅ 全部通过** |

### 新增文件

| 文件 | 说明 |
| --- | --- |
| `playsound.py` | `playsound3` 兼容垫片，适配新版库接口 |
| `gui_data/cr_text.txt` | 自定义文本资源文件 |
| `data.pkl` | 数据处理文件 |
| `.gitignore` | 排除 `venv/`、`__pycache__/`、`.vscode/` 等构建产物 |
| `README_zh.md` | **本中文文档** |
| `uvr_cli.py` | **命令行工具** — 查看模型列表、搜索模型信息、快速启动 GUI |
| `requirements.txt` | **重建依赖清单** — 基于当前已验证的虚拟环境生成 |

### 清理

* **重建** `requirements.txt` — 基于当前虚拟环境生成的完整依赖清单，方便新用户快速搭建环境
* **删除** `models/Demucs_Models/v3_v4_repo/demucs_models.txt` — 废弃的模型引用文件

---

## 🤝 贡献指南

* 欢迎提交 Pull Request
* 本项目完全开源（MIT 协议），可自由使用和修改
* 如需使用我们的模型，请保留 UVR 及开发者的署名

## 📋 项目信息

| 项目 | 信息 |
| --- | --- |
| 版本 | `v1.0.0`（基于上游 `v5.6.0`） |
| Fork 仓库 | [kasc0206/uvrgui](https://github.com/kasc0206/uvrgui) |
| 原始仓库 | [Anjok07/ultimatevocalremovergui](https://github.com/Anjok07/ultimatevocalremovergui) |
| 测试 | ✅ 32/32 全部通过（pytest + coverage） |
| 代码质量 | ✅ ruff 零错误 |
| CLI 命令 | 10 个（list/info/process/demucs/download-models/config/version/gui/help + --json） |
| 最新合并 | `dev-upstream → master` 2026-05-31 |

## �📜 许可证

本项目代码采用 [MIT 许可证](LICENSE)。

## 🙏 鸣谢

* [ZFTurbo](https://github.com/ZFTurbo) — MDX23C 新模型的训练与权重
* [DilanBoskan](https://github.com/DilanBoskan) — 项目早期的关键贡献
* [Bas Curtiz](https://www.youtube.com/user/bascurtiz) — 设计官方 Logo、图标、横幅和启动画面
* [tsurumeso](https://github.com/tsurumeso) — VR 架构的原始代码
* [Kuielab & Woosung Choi](https://github.com/kuielab) — MDX-Net AI 的原始代码
* [Adefossez & Demucs](https://github.com/facebookresearch/demucs) — Demucs AI 的原始代码
* [KimberleyJSN](https://github.com/KimberleyJensen) — MDX-Net 和 Demucs 训练脚本的指导
* [Hv](https://github.com/NaJeongMo/Colab-for-MDX_B) — MDX-Net 的分块处理实现

## 📚 参考文献

* [1] Takahashi et al., "Multi-scale Multi-band DenseNets for Audio Source Separation", <https://arxiv.org/pdf/1706.09588.pdf>
