---
name: uvr-cli-skills
description: UVR (Ultimate Vocal Remover) CLI 工具 — AI 人声/伴奏分离、模型管理、批量处理
version: 1.0.0
---

# UVR CLI — AI 音频源分离工具

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
| 配置默认值 | "以后默认用 mps 设备" | `config --key default_device --value mps` |
| 搜索模型 | "帮我找找有没有去混响的模型" | `info reverb` / `info reverb --json` |
| 查看版本 | "当前是什么版本" | `version` / `version --json` |
| 设置输出格式 | "输出 flac 格式" | `--format flac` / `config --key output_format --value flac` |

## 快速开始

```bash
# 进入项目目录并激活环境
cd /Users/kylin/test/uvrgui
source venv/bin/activate

# 分离人声和伴奏
python uvr_cli.py process 输入歌曲.mp3 --two-stem vocals

# 6-stem 分离（鼓/贝斯/其他/人声/吉他/钢琴）
python uvr_cli.py process 输入歌曲.mp3 --model htdemucs_6s
```

## 命令参考

### `list` — 列出所有模型

列出所有可用模型及下载状态。

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

# 批量处理文件夹
python uvr_cli.py process ./音乐文件夹/ --two-stem vocals

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
# UVR CLI v5.6.0-fork (基于 v5.6.0)
# 仓库: https://github.com/kasc0206/uvrgui

python uvr_cli.py version --json
```

**JSON 返回：**
```json
{"version": "v5.6.0-fork", "base": "v5.6.0", "repo": "https://github.com/kasc0206/uvrgui"}
```

---

### `config` — 配置管理

设置默认值，避免重复输入参数。

```bash
# 查看配置
python uvr_cli.py config
python uvr_cli.py config --json

# 设置默认设备
python uvr_cli.py config --key default_device --value mps

# 设置默认模型
python uvr_cli.py config --key default_model --value htdemucs_6s

# 设置默认输出格式
python uvr_cli.py config --key output_format --value flac

# 设置默认输出音源
python uvr_cli.py config --key two_stem --value vocals
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
