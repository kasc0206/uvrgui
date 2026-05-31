# Ultimate Vocal Remover GUI v5.6 — 中文版

<img src="https://raw.githubusercontent.com/Anjok07/ultimatevocalremovergui/master/gui_data/img/UVR_v5.6.png?raw=true" />

[![Release](https://img.shields.io/github/release/anjok07/ultimatevocalremovergui.svg)](https://github.com/anjok07/ultimatevocalremovergui/releases/latest)
[![Downloads](https://img.shields.io/github/downloads/anjok07/ultimatevocalremovergui/total.svg)](https://github.com/anjok07/ultimatevocalremovergui/releases)

> 🎵 **终极人声移除图形界面** — 利用最先进的音源分离模型，从音频文件中提取或移除人声。

---

## 📖 关于本项目

**Ultimate Vocal Remover GUI (UVR)** 是一款基于深度学习的音频源分离工具，支持将音乐中的**人声**、**伴奏**、**鼓点**、**贝斯**等多种音源分离为独立音轨。

除 Demucs v3/v4 的 4-stem 模型外，本软件包提供的所有模型均由 UVR 核心开发团队自行训练。

### 👥 核心开发团队

| 角色 | 开发者 |
|------|--------|
| 核心开发者 | [Anjok07](https://github.com/anjok07) |
| 核心开发者 | [aufr33](https://github.com/aufr33) |

### ☕ 支持项目

- [Buy Me a Coffee](https://www.buymeacoffee.com/uvr5)

---

## ✨ 特性概览

- ✅ **三种主流 AI 架构**：VR Architecture、MDX-Net、Demucs（v1~v4）
- ✅ **支持多种新型模型**：BS-Roformer、Mel-Roformer、SCNet、Bandit 等
- ✅ **人声 / 伴奏 / 多音源分离**
- ✅ **卡拉 OK 伴奏制作**
- ✅ **去噪 / 去混响 / 去回声**
- ✅ **GPU 加速**（NVIDIA CUDA / Apple MPS）
- ✅ **批量处理**（Batch Mode）
- ✅ **二级模型混合**（Secondary Model Mode）
- ✅ **集成模式**（Ensemble Mode）
- ✅ **变调变速**（需 Rubber Band 库）
- ✅ **拖拽导入**、**采样预览**、**设置保存与加载**

---

## 🚀 安装指南

### 📦 快速安装（推荐）

#### Windows

1. 下载安装包：[主下载链接](https://github.com/Anjok07/ultimatevocalremovergui/releases/download/v5.6/UVR_v5.6.0_setup.exe) | [镜像](https://www.mediafire.com/file_premium/jiatpgp0ljou52p/UVR_v5.6.0_setup.exe/file)
2. 运行安装程序，按向导完成安装

> **注意：**
> - 仅支持 Windows 10 及以上系统
> - 必须安装到 C 盘主分区
> - AMD Radeon / Intel Arc 用户请使用 [DirectML 版本](https://github.com/Anjok07/ultimatevocalremovergui/releases/download/v5.6/UVR_1_15_25_22_30_BETA_full.exe)

#### macOS

- **Apple Silicon (M1/M2/M3)**：[arm64 下载](https://github.com/Anjok07/ultimatevocalremovergui/releases/download/v5.6/Ultimate_Vocal_Remover_v5_6_MacOS_arm64.dmg)
- **Intel Mac**：[x86_64 下载](https://github.com/Anjok07/ultimatevocalremovergui/releases/download/v5.6/Ultimate_Vocal_Remover_v5_6_MacOS_x86_64.dmg)

> **首次启动可能需要 5~10 分钟**，取决于你的 Mac 型号。
>
> 如果遇到无法打开的问题，请在终端执行：
> ```bash
> sudo spctl --master-disable
> sudo xattr -rd com.apple.quarantine /Applications/Ultimate\ Vocal\ Remover.app
> ```

#### Linux

```bash
# Debian/Ubuntu 系
sudo apt update && sudo apt upgrade
sudo apt-get install -y ffmpeg python3-pip python3-tk

# Arch 系
sudo pacman -Syu
sudo pacman -S ffmpeg python-pip tk

# 创建虚拟环境（强烈推荐）
python3 -m venv venv
source venv/bin/activate

# 安装依赖（从已激活的 venv 中）
pip install -r requirements.txt

# 启动
python UVR.py
```

---

### 🔧 手动安装（所有平台通用）

```bash
# 1. 克隆仓库
git clone https://github.com/kasc0206/uvrgui.git
cd uvrgui

# 2. 创建并激活虚拟环境
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
# 或 venv\Scripts\activate  # Windows

# 3. 安装依赖
pip install -r requirements.txt

# 4. （可选）NVIDIA GPU 用户安装 CUDA 版 PyTorch
pip install --upgrade torch --extra-index-url https://download.pytorch.org/whl/cu117

# 5. 启动
python UVR.py
```

#### 额外依赖

| 依赖 | 用途 | 安装方式 |
|------|------|----------|
| **FFmpeg** | 处理非 WAV 格式音频 | 各平台包管理器安装 |
| **Rubber Band** | 变调/变速功能 | 可选，非必需 |

---

## 🧠 模型架构详解

UVR 支持三类核心 AI 架构，每类下有多种预训练模型：

### 1️⃣ VR Architecture（VR 架构）

UVR 团队自研的模型，按频带数划分：

| 频带 | 采样率 | 适用场景 |
|------|--------|----------|
| 1-band | 16k~44.1k | 轻量快速，适合简单分离 |
| 2-band | 32k | 中等质量人声提取 |
| 3-band | 44.1k | 平衡速度与质量 |
| **4-band** | **44.1k** | **⭐ 主流选择，质量最佳** |

**特殊 VR 模型：**
- `HP-UVR` (1~9号) — 高通滤波优化，提取人声
- `SP-UVR` (10~16号) — 频谱处理优化
- `Karaoke` 系列 — 制作卡拉 OK 伴奏
- `DeNoise / De-Echo / DeReverb` — 降噪、去回声、去混响
- `BVE` — 提取背景和声
- 专项模型：`No Piano`、`No Woodwinds`、`No Echo` 等

### 2️⃣ MDX-Net 架构

基于混合频谱/时域网络的分离模型：

| 模型名称 | 输出 | 说明 |
|----------|------|------|
| **UVR-MDX-NET Main** | 人声 | ⭐ 综合效果最佳的主模型 |
| UVR-MDX-NET 1/2/3 | 人声 | 通用人声提取 |
| UVR-MDX-NET Inst Main/HQ | 伴奏 | 高质量伴奏提取 |
| UVR-MDX-NET Karaoke | 伴奏 | 卡拉 OK 伴奏 |
| Kim Vocal/Inst | 人声/伴奏 | 社区贡献模型 |
| MDX23C-InstVoc HQ | 人声+伴奏 | 新版 MDX23C 架构 |

**新型衍生模型（社区贡献）：**

| 模型系列 | 说明 |
|----------|------|
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
|------|------|------|
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
|----------|----------|
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


- **Select Input** — 选择输入音频文件或文件夹
- **Select Output** — 选择输出目录
- **Download More Models** — 下载更多预训练模型
- **Start Processing** — 开始处理
- **Batch Mode** — 批量处理模式（更高效）
- **Secondary Model** — 二级模型混合（调整分离倾向）
- **Ensemble Mode** — 集成模式（多模型组合）
- **Sample Mode** — 仅处理音频片段预览效果

### 命令行工具（CLI）

本 Fork 新增了 `uvr_cli.py` 命令行工具，方便快速操作：

```bash
# 列出所有可用模型及下载状态
python uvr_cli.py list

# 查看特定模型详情
python uvr_cli.py info BS-Roformer

# 启动图形界面
python uvr_cli.py gui

# 显示帮助
python uvr_cli.py help
```

---

## ⚙️ 硬件要求

| 项目 | 最低配置 | 推荐配置 |
|------|----------|----------|
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
|------|----------|
| `models/MDX_Net_Models/model_data/model_data.json` | **大幅扩充**，新增大量新型 MDX 模型配置（+830/-351） |
| `models/MDX_Net_Models/model_data/model_name_mapper.json` | **新增 26 个模型名称映射**（+68/-66） |
| `models/VR_Models/model_data/model_data.json` | 重构并更新 VR 模型参数配置（+272/-137） |
| `models/Demucs_Models/model_data/model_name_mapper.json` | 格式修正，添加文件末尾换行（+66/-66） |

#### 新增 MDX 模型清单

| 类别 | 模型 |
|------|------|
| **BS-Roformer** | `Viperx-1297`、`Viperx-1296`、`Viperx-1053` |
| **Mel-Roformer** | `Viperx-1143` |
| **MB-Roformer** | `Inst-v1`、`Inst-v2`、`Inst-v1-E`、`Duality-v1`、`Duality-v2`、`Kim`、`Karaoke` |
| **SCNet** | `Starrytong`、`Large-Starrytong`、`Large`、`XL-ZFTurbo` |
| **Bandit** | `Cinematic-Bandit-Plus`、`Cinematic-Bandit-Multi` |
| **MDX23C** | `InstVoc HQ 2`、`InstVoc D1581` |
| **其他** | `DrumSep`、`Phantom-Mid`、`Reverb HQ`、`BS-Ro-Dereverb`、`BS-Ro-Inst-EXP` |

### 新增文件

| 文件 | 说明 |
|------|------|
| `playsound.py` | `playsound3` 兼容垫片，适配新版库接口 |
| `gui_data/cr_text.txt` | 自定义文本资源文件 |
| `data.pkl` | 数据处理文件 |
| `.gitignore` | 排除 `venv/`、`__pycache__/`、`.vscode/` 等构建产物 |
| `README_zh.md` | **本中文文档** |
| `uvr_cli.py` | **命令行工具** — 查看模型列表、搜索模型信息、快速启动 GUI |
| `requirements.txt` | **重建依赖清单** — 基于当前已验证的虚拟环境生成 |

### 清理

- **重建** `requirements.txt` — 基于当前虚拟环境生成的完整依赖清单，方便新用户快速搭建环境
- **删除** `models/Demucs_Models/v3_v4_repo/demucs_models.txt` — 废弃的模型引用文件

---

## 🤝 贡献指南

- 欢迎提交 Pull Request
- 本项目完全开源（MIT 协议），可自由使用和修改
- 如需使用我们的模型，请保留 UVR 及开发者的署名

## 📜 许可证

本项目代码采用 [MIT 许可证](LICENSE)。

## 🙏 鸣谢

- [ZFTurbo](https://github.com/ZFTurbo) — MDX23C 新模型的训练与权重
- [DilanBoskan](https://github.com/DilanBoskan) — 项目早期的关键贡献
- [Bas Curtiz](https://www.youtube.com/user/bascurtiz) — 设计官方 Logo、图标、横幅和启动画面
- [tsurumeso](https://github.com/tsurumeso) — VR 架构的原始代码
- [Kuielab & Woosung Choi](https://github.com/kuielab) — MDX-Net AI 的原始代码
- [Adefossez & Demucs](https://github.com/facebookresearch/demucs) — Demucs AI 的原始代码
- [KimberleyJSN](https://github.com/KimberleyJensen) — MDX-Net 和 Demucs 训练脚本的指导
- [Hv](https://github.com/NaJeongMo/Colab-for-MDX_B) — MDX-Net 的分块处理实现

## 📚 参考文献

- [1] Takahashi et al., "Multi-scale Multi-band DenseNets for Audio Source Separation", https://arxiv.org/pdf/1706.09588.pdf
