---
name: uvr-cli-skills
description: UVR (Ultimate Vocal Remover) CLI 工具 — AI 人声/伴奏分离、模型管理、批量处理
version: 1.2.0
---

# UVR CLI — AI 音频源分离工具 (v1.2.0)

通过命令行调用 Demucs/MDX-Net/VR 模型，从音频文件中分离人声、伴奏、鼓、贝斯等音源。

## 适用场景

| 场景 | 用户示例 | 说明 |
|------|----------|------|
| 提取人声 | "帮我把这首歌的人声提取出来" | `process --two-stem vocals` |
| 提取伴奏 | "我要这首歌的伴奏" | `process --two-stem vocals`（得到 `no_vocals`） |
| 分离多音源 | "分离这首歌的所有音轨" | `process`（无 `--two-stem`，输出 4 轨） |
| 批量处理 | "把这个文件夹里的歌全部分离" | `process 文件夹/` |
| 查看可用模型 | "有哪些模型可以用" | `list` / `list --json` |
| 下载模型 | "帮我预下载模型" | `download-models` |
| 同步模型数据 | "更新模型数据库" | `update-model-data` |
| 配置默认值 | "以后默认用 mps 设备" | `config --key default_device --value mps` |
| 切换语言 | "切换成英文界面" | `config --key language --value en` |
| 搜索模型 | "帮我找找有没有去混响的模型" | `info reverb` / `info reverb --json` |
| 查看版本 | "当前是什么版本" | `version` / `version --json` |
| 设置输出格式 | "输出 flac 格式" | `--format flac` / `config --key output_format --value flac` |
| 只显示已下载的模型 | "我已经下载了哪些模型" | `list --downloaded` |
| 只显示未下载的模型 | "还有哪些模型没下载" | `list --missing` |
| 预览处理 | "先看看会处理哪些文件" | `process 文件夹/ --dry-run` |
| 跳过已完成 | "继续上次没处理完的" | `process 文件夹/ --resume` |
| 隐藏进度条 | "不想看进度条" | `process 歌曲.mp3 --no-progress` |
| 高质量分离 | "我要最好的分离质量" | `process 歌曲.mp3 --shifts 5` |
| Demucs v4.1 二级模式 | "用 add 模式混合伴奏" | `process 歌曲.mp3 --other-method add` |
| 删除配置项 | "取消默认设置" | `config --delete 配置项名` |
| 初始化配置 | "生成默认配置" | `config --init` |
| 列出全部配置 | "查看所有配置项" | `config --list` |
| 重置配置 | "恢复出厂设置" | `config --reset` |
| 导出/导入配置 | "把我的配置备份一下" | `config --export 文件.json` |

## 快速开始

```bash
# 进入项目目录并激活环境
cd /Users/kylin/test/uvrgui
source venv/bin/activate

# 分离人声和伴奏
python uvr_cli.py process 输入歌曲.mp3 --two-stem vocals

# 6-stem 分离（鼓/贝斯/其他/人声/吉他/钢琴）
python uvr_cli.py process 输入歌曲.mp3 --model htdemucs_6s

# 高质量分离（shifts=5 质量更高但更慢）
python uvr_cli.py process 输入歌曲.mp3 --shifts 5

# 预览但不实际处理
python uvr_cli.py process 输入歌曲.mp3 --dry-run
```

## 命令参考

### `list` — 列出所有模型

列出所有可用模型及下载状态。

```bash
# 只显示已下载的模型
python uvr_cli.py list --downloaded

# 只显示未下载的模型
python uvr_cli.py list --missing
```

```bash
# 人类可读
python uvr_cli.py list

# ✅ JSON（推荐 AI 使用）
python uvr_cli.py list --json
```

**JSON 返回结构：**
```json
{
  "models": {
    "VR Architecture": [
      {"name": "UVR-MDX-NET Main", "hash": "a1b2c3...", "output": "Vocals", "downloaded": false}
    ],
    "MDX-Net": [...],
    "Demucs": [
      {"name": "v4 | htdemucs", "file": "htdemucs.yaml", "downloaded": false}
    ]
  },
  "total": 86
}
```

---

### `info <关键词>` — 搜索模型

按名称、关键词或输出类型搜索模型。

```bash
python uvr_cli.py info vocals
python uvr_cli.py info htdemucs --json
```

**JSON 返回：**
```json
{
  "results": [
    {"arch": "Demucs", "name": "v4 | htdemucs", "file": "htdemucs.yaml"},
    {"arch": "MDX-Net", "name": "UVR-MDX-NET Main", "key": "...", "output": "Vocals"}
  ],
  "count": 5
}
```

---

### `process <输入>` — 分离音频（核心功能）

支持单个文件或整个文件夹。

```bash
# 基本用法（4-stem: 鼓/贝斯/其他/人声）
python uvr_cli.py process 歌曲.mp3

# 只提取人声（同时输出伴奏）
python uvr_cli.py process 歌曲.flac --two-stem vocals

# 指定模型
python uvr_cli.py process 歌曲.mp3 --model htdemucs_6s

# 指定设备
python uvr_cli.py process 歌曲.mp3 --device mps   # Apple Silicon GPU
python uvr_cli.py process 歌曲.mp3 --device cpu   # CPU
python uvr_cli.py process 歌曲.mp3 --device cuda  # NVIDIA GPU

# 指定输出目录
python uvr_cli.py process 歌曲.mp3 --out ./output/

# 指定输出格式（wav/flac/mp3/aiff）
python uvr_cli.py process 歌曲.mp3 --format flac

# 高质量模式（shifts=5，质量更高但更慢）
python uvr_cli.py process 歌曲.mp3 --shifts 5 --overlap 0.5

# 跳过已完成的文件（断点续传）
python uvr_cli.py process ./音乐文件夹/ --resume

# 预览模式（不实际处理）
python uvr_cli.py process 歌曲.mp3 --dry-run

# 批量处理文件夹
python uvr_cli.py process ./音乐文件夹/ --two-stem vocals

# 指定分离架构
python uvr_cli.py process 歌曲.mp3 --arch demucs

# ✅ JSON 输出（AI 推荐）
python uvr_cli.py process 歌曲.mp3 --json
```

**JSON 返回：**
```json
{
  "ok": true,
  "output_dir": "/path/to/output",
  "files": 1,
  "model": "htdemucs",
  "device": "mps",
  "format": "wav"
}
```

**输出的 progress 参数说明：**

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `--shifts N` | 1 | 随机移位次数，越大质量越高（1-5），每增 1 约慢 N 倍 |
| `--overlap N` | 0.25 | 分割重叠率 (0-1)，越大拼接越平滑但更慢 |
| `--resume` | off | 跳过输出已存在的文件 |
| `--dry-run` | off | 只列出要处理的文件，不实际执行 |
| `--no-progress` | off | 隐藏 tqdm 进度条 |
| `--other-method` | none | Demucs v4.1 二级模式: `add`/`minus`/`none` |

**输出目录结构：**
```
输出目录/
├── 歌曲名/
│   ├── 歌曲名_(vocals).wav          ← 人声
│   └── 歌曲名_(no_vocals).wav       ← 伴奏
```

**支持模型（`--model` 参数）：**

| 模型名 | 音源数 | 说明 |
|--------|--------|------|
| `htdemucs`（默认） | 4 | 鼓/贝斯/其他/人声，质量最佳 |
| `htdemucs_ft` | 4 | htdemucs 微调版 |
| `htdemucs_6s` | 6 | +吉他/钢琴，6 轨分离 |
| `htdemucs_mmi` | 4 | 多乐器版本 |
| `mdx_extra` | 4 | Demucs v3 混合模型 |
| `mdx` | 4 | Demucs v3 基础版 |
| `UVR_Model_1` | 2 | UVR 特调 2-stem |

---

### `update-model-data` — 同步模型数据

从上游 TRvlvr/application_data 拉取最新模型数据文件。

```bash
python uvr_cli.py update-model-data
python uvr_cli.py update-model-data --json   # ✅ AI 推荐
```

**JSON 返回：**
```json
{
  "ok": true,
  "updated": [
    {"file": "MDX_Net_Models/model_data/model_data.json", "status": "updated"},
    {"file": "MDX_Net_Models/model_data/model_name_mapper.json", "status": "unchanged"},
    {"file": "VR_Models/model_data/model_data.json", "status": "updated"},
    {"file": "Demucs_Models/model_data/model_name_mapper.json", "status": "unchanged"}
  ],
  "total": 4
}
```

---

### `download-models` — 预下载模型

使用 curl 高速下载（比 Python urllib 快 500x）。

```bash
python uvr_cli.py download-models
python uvr_cli.py download-models --json   # ✅ AI 推荐
```

**JSON 返回：**
```json
{
  "ok": true,
  "downloaded": [
    {"file": "955717e8-8726e21a.th", "status": "downloaded", "size_mb": 80.2, "speed_mbps": 18.4}
  ],
  "total": 9
}
```

> **注意：** `process` 命令会自动下载缺失的模型文件，通常无需手动执行此命令。

---

### `version` — 查看版本

```bash
python uvr_cli.py version
# UVR CLI v1.2.0 (基于 v5.6.0)
# 仓库: https://github.com/kasc0206/uvrgui

python uvr_cli.py version --json
```

**JSON 返回：**
```json
{"version": "v1.2.0", "base": "v5.6.0", "repo": "https://github.com/kasc0206/uvrgui"}
```

---

### `config` — 配置管理

设置默认值，避免重复输入参数。

```bash
# 显示配置
python uvr_cli.py config
python uvr_cli.py config --json

# 初始化默认配置
python uvr_cli.py config --init

# 列出所有配置项及说明
python uvr_cli.py config --list

# 设置默认设备
python uvr_cli.py config --key default_device --value mps

# 设置默认模型
python uvr_cli.py config --key default_model --value htdemucs_6s

# 设置默认输出格式
python uvr_cli.py config --key output_format --value flac

# 设置默认输出音源
python uvr_cli.py config --key two_stem --value vocals

# 切换语言
python uvr_cli.py config --key language --value en   # English
python uvr_cli.py config --key language --value zh   # 中文

# 删除配置项
python uvr_cli.py config --delete default_device

# 重置所有配置
python uvr_cli.py config --reset

# 导出配置到文件
python uvr_cli.py config --export my_config.json

# 从文件导入配置
python uvr_cli.py config --import my_config.json
```

**优先级：** CLI 参数 > 配置文件 > 程序默认值

---

### `gui` — 启动图形界面

```bash
python uvr_cli.py gui
```

---

## 设备选择指南

| 设备参数 | 适用硬件 | 性能 |
|----------|----------|------|
| `--device mps` | Apple Silicon (M1/M2/M3/M4) | ⭐⭐⭐ 推荐 |
| `--device cuda` | NVIDIA GPU | ⭐⭐⭐ 推荐 |
| `--device cpu` | 所有平台 | ⭐ 慢但兼容 |

## 常见模型推荐

| 需求 | 推荐命令 |
|------|----------|
| 🎤 提取人声 | `process 歌曲.mp3 --two-stem vocals` |
| 🎵 提取伴奏 | `process 歌曲.mp3 --two-stem vocals`（输出 `no_vocals`） |
| 🥁 分离鼓点 | `process 歌曲.mp3 --model htdemucs`（4-stem 含 drums） |
| 🎸 分离吉他 | `process 歌曲.mp3 --model htdemucs_6s`（6-stem 含 guitar） |
| 🎹 分离钢琴 | 同上，6-stem 含 piano |
| 📁 批量分离 | `process ./专辑/ --two-stem vocals --out ./输出/` |
| 🧹 去混响 | `info reverb` 找 Reverb HQ 模型（需 GUI 下载） |

## 注意事项

1. **模型自动下载**：首次运行 `process` 会自动下载模型到 `~/.cache/torch/hub/checkpoints/`，后续复用
2. **文件命名**：输出文件自动放入以原文件名命名的子目录，避免同名覆盖
3. **音频格式**：支持 `.mp3` `.wav` `.flac` `.ogg` `.m4a` `.wma` `.aiff` `.aac` `.opus`
4. **FFmpeg**：安装 FFmpeg 可处理更多格式（`.aac` `.opus` 等）
5. **输出格式**：目前固定为 44.1kHz 16-bit WAV

## 安装（供参考）

```bash
git clone https://github.com/kasc0206/uvrgui.git
cd uvrgui
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python uvr_cli.py --help
```

## CI/CD 构建工作流

推送 tag `v*` 自动触发三平台构建：

| 工作流 | 平台 | 产物 |
|--------|------|------|
| `build-windows.yml` | 🪟 Windows | `UVR_*_CPU.zip` / `UVR_*_CUDA.zip` |
| `build-macos.yml` | 🍎 macOS | `UVR_*_macOS_*.zip`（.app 包） |
| `build-linux.yml` | 🐧 Linux | `UVR_*_Linux_x86_64.tar.gz` / `*_CUDA.tar.gz` |

Windows 工作流负责创建 GitHub Release 和发布说明，macOS/Linux 自动附加产物。
