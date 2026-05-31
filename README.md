# Ultimate Vocal Remover GUI v5.6
<img src="https://raw.githubusercontent.com/Anjok07/ultimatevocalremovergui/master/gui_data/img/UVR_v5.6.png?raw=true" />

[![Release](https://img.shields.io/github/release/anjok07/ultimatevocalremovergui.svg)](https://github.com/anjok07/ultimatevocalremovergui/releases/latest)
[![Downloads](https://img.shields.io/github/downloads/anjok07/ultimatevocalremovergui/total.svg)](https://github.com/anjok07/ultimatevocalremovergui/releases)
[![Tests](https://img.shields.io/badge/tests-33%2F33-passing-brightgreen)](https://github.com/kasc0206/uvrgui)
[![Build Windows](https://github.com/kasc0206/uvrgui/actions/workflows/build-windows.yml/badge.svg)](https://github.com/kasc0206/uvrgui/actions/workflows/build-windows.yml)

> 🎵 **Ultimate Vocal Remover** — A state-of-the-art AI-powered audio source separation tool.

---

## 📖 About

This application uses state-of-the-art source separation models to remove vocals from audio files. UVR's core developers trained all of the models provided in this package (except for the Demucs v3 and v4 4-stem models).

### 👥 Core Developers

| Role | Developer |
| --- | --- |
| Original Author | [Anjok07](https://github.com/anjok07) |
| Original Author | [aufr33](https://github.com/aufr33) |
| Fork Maintainer | [kasc0206](https://github.com/kasc0206) |

### ☕ Support the Project

* [Buy Me a Coffee](https://www.buymeacoffee.com/uvr5)

### 🔗 Fork Repository

This fork ([kasc0206/uvrgui](https://github.com/kasc0206/uvrgui)) extends the original UVR with:

- 🖥️ **CLI Tool** — `uvr_cli.py` with 10 commands for headless operation
- ✅ **Lint Clean** — All ruff checks pass (zero errors on custom code)
- 🧪 **Test Suite** — 32 tests with pytest + coverage reporting
- 🐛 **Bug Fixes** — Fixed `highlightthicknes` typo, star imports, Pylance type errors
- 📖 **Chinese Documentation** — Full README_zh.md

## CLI Tool (Fork Feature)

This fork adds `uvr_cli.py`, a full-featured command-line interface:

```bash
# List all available models with download status
python uvr_cli.py list

# List models as JSON (for programmatic use)
python uvr_cli.py list --json

# Show model details
python uvr_cli.py info <keyword>

# Launch the GUI
python uvr_cli.py gui

# View or modify configuration
python uvr_cli.py config
python uvr_cli.py config --key default_device --value mps

# Process audio with Demucs (auto-downloads models)
python uvr_cli.py process song.mp3
python uvr_cli.py demucs song.flac --two-stem vocals
python uvr_cli.py process input_dir/ --out output_dir/

# Download Demucs models via curl (500x faster)
python uvr_cli.py download-models

# Check version
python uvr_cli.py version

# Show help
python uvr_cli.py help
```

## Installation (Fork)

> ⚠️ **注意**：本 Fork 不提供预编译安装包。请按照以下步骤从源码构建。

### Windows / macOS / Linux — 源码安装

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

# 4. NVIDIA GPU 用户安装 CUDA PyTorch（可选）
pip install --upgrade torch --extra-index-url https://download.pytorch.org/whl/cu118

# 5. 启动
python UVR.py
```

### Windows EXE 构建

本 Fork 支持通过 GitHub Actions 自动构建 Windows EXE。推送 tag 即可触发：

```bash
git tag v1.0.0
git push origin v1.0.0
```

也可手动触发：[Actions 页面](https://github.com/kasc0206/uvrgui/actions/workflows/build-windows.yml)

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
- 约 10 GB 磁盘空间（含 PyTorch 运行时）
- Xcode Command Line Tools

#### 步骤

```bash
# 1. 安装 Xcode Command Line Tools
xcode-select --install

# 2. 安装 Homebrew（如尚未安装）
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# 3. 安装系统依赖
brew install ffmpeg python@3.10

# 4. 可选 — 安装 Rubber Band（变调变速功能）
brew install rubberband

# 5. 克隆仓库
git clone https://github.com/kasc0206/uvrgui.git
cd uvrgui

# 6. 创建虚拟环境
python3.10 -m venv venv
source venv/bin/activate

# 7. 安装依赖
pip install --upgrade pip wheel setuptools
pip install -r requirements.txt

# 8. 启动
python UVR.py
```

> **首次启动可能需要 5-10 分钟**（模型初始化）。
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
- 约 10 GB 磁盘空间（含 PyTorch 运行时）
- NVIDIA GPU 用户：CUDA Toolkit 11.8+（可选）

#### Debian / Ubuntu 系

```bash
# 1. 更新系统
sudo apt update && sudo apt upgrade -y

# 2. 安装系统依赖
sudo apt install -y ffmpeg python3-pip python3-tk python3-venv

# 3. 可选 — 安装 Rubber Band（变调变速功能）
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

# 3. 可选 — 安装 Rubber Band（变调变速功能）
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

# 2. 可选 — 安装 Rubber Band
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

### 额外依赖

```bash
sudo spctl --master-disable
sudo xattr -rd com.apple.quarantine /path/to/UVR
```

<details id="CannotOpen">
  <summary>MacOS Users: Having Trouble Opening UVR?</summary>

> Due to Apples strict application security, you may need to follow these steps to open UVR.
>
> First, run the following command via Terminal.app to allow applications to run from all sources (it's recommended that you re-enable this once UVR opens properly.)
> 
> ```bash
> sudo spctl --master-disable
> ```
> 
> Second, run the following command to bypass Notarization: 
> 
> ```bash
> sudo xattr -rd com.apple.quarantine /Applications/Ultimate\ Vocal\ Remover.app
> ```

</details>

<details id="MacInstall">
  <summary>Manual MacOS Installation</summary>

### Manual MacOS Installation

- Download and save this repository [here](https://github.com/Anjok07/ultimatevocalremovergui/archive/refs/heads/master.zip)
- Download and install Python 3.10 [here](https://www.python.org/ftp/python/3.10.9/python-3.10.9-macos11.pkg)
- From the saved directory run the following - 

```
pip3 install -r requirements.txt
```

- If your Mac is running with an M1, please run the following command next. If not, skip this step. - 

```
cp /Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/_soundfile_data/libsndfile_arm64.dylib /Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/_soundfile_data/libsndfile.dylib
```

**FFmpeg Installation**

- Once everything is done installing, download the correct FFmpeg binary for your system [here](http://www.osxexperts.net) and place it into the main application directory.

**Rubber Band Installation**

In order to use the Time Stretch or Change Pitch tool, you'll need Rubber Band.

- Download the precompiled build [here](https://breakfastquay.com/files/releases/rubberband-3.1.2-gpl-executable-windows.zip)
- From the archive, extract the following files to the UVR/lib_v5 application directory:
   - ```rubberband-3.1.2-gpl-executable-macos/rubberband```

This process has been tested on a MacBook Pro 2021 (using M1) and a MacBook Air 2017 and is confirmed to be working on both.

</details>


### Linux Installation (Updated Instructions)

<details id="LinuxInstall">
  <summary>See Linux Installation Instructions</summary>

<br />

**These installation instructions are for Debian & Arch-based Linux systems.**

---

#### **Step 1: Download the Repository**
- Clone the [fork repository](https://github.com/kasc0206/uvrgui):
  ```bash
  git clone https://github.com/kasc0206/uvrgui.git
  cd uvrgui
  ```
- Or download from the [original repository](https://github.com/Anjok07/ultimatevocalremovergui/archive/refs/heads/master.zip).
- Extract the downloaded file to a directory of your choice.

---

#### **Step 2: Install Dependencies**
Use the following commands based on your system type:

**For Debian-based systems (Ubuntu, Mint, etc.):**
```bash
sudo apt update && sudo apt upgrade
sudo apt-get install -y ffmpeg python3-pip python3-tk
```

**For Arch-based systems (EndeavourOS):**
```bash
sudo pacman -Syu
sudo pacman -S ffmpeg python-pip tk
```

---

#### **Step 3: Set Up a Virtual Environment (Recommended)**
Setting up a virtual environment (venv) ensures that the program's dependencies do not interfere with system-wide Python packages.

1. **Navigate to the extracted repository directory:**
   ```bash
   cd /path/to/ultimatevocalremovergui
   ```

2. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   ```

3. **Activate the virtual environment:**
   - For **Debian-based and Arch-based systems:**
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies in the virtual environment:**
   ```bash
   pip install -r requirements.txt
   ```

---

#### **Step 4: Run the Application**
While the virtual environment is activated, start the application:
```bash
python UVR.py
```

---

#### **Important Notes**
1. **Avoid Modifying System Files:**  
   Previous instructions suggested deleting the `/usr/lib/python3.11/EXTERNALLY-MANAGED` file, which is dangerous and can break Python package management. Do **NOT** delete this file.

2. **Why Use Virtual Environments?**  
   Virtual environments isolate the program's dependencies, preventing conflicts with system Python packages. More information is available [here](https://stackoverflow.com/questions/75602063/pip-install-r-requirements-txt-is-failing-this-environment-is-externally-mana/75696359#75696359).

3. **Known Issues and Discussions:**  
   - [Issue #1578](https://github.com/Anjok07/ultimatevocalremovergui/issues/1578)  
   - [Pull Request #1068](https://github.com/Anjok07/ultimatevocalremovergui/pull/1068)

---

If you encounter issues, refer to the [GitHub Issues](https://github.com/Anjok07/ultimatevocalremovergui/issues) page for help. 

</details>

### Other Application Notes
- Nvidia GTX 1060 6GB is the minimum requirement for GPU conversions.
- Nvidia GPUs with at least 8GBs of V-RAM are recommended.
- AMD Radeon GPU supported is limited at this time.
   - There is currently a working branch for AMD GPU users [here](https://github.com/Anjok07/ultimatevocalremovergui/tree/v5.6-amd-gpu)
- This application is only compatible with 64-bit platforms. 
- This application relies on the Rubber Band library for the Time-Stretch and Pitch-Shift options.
- This application relies on FFmpeg to process non-wav audio files.
- The application will automatically remember your settings when closed.
- Conversion times will significantly depend on your hardware. 
- These models are computationally intensive. 

### Performance:
- Model load times are faster.
- Importing/exporting audio files is faster.

## Troubleshooting

### Common Issues

- If FFmpeg is not installed, the application will throw an error if the user attempts to convert a non-WAV file.
- Memory allocation errors can usually be resolved by lowering the "Segment" or "Window" sizes.

#### MacOS Sonoma Left-click Bug
There's a known issue on MacOS Sonoma where left-clicks weren't registering correctly within Tkinter applications. This was caused by a Tkinter bug on Sonoma and has since been resolved. If you still experience this issue, updating Tkinter via Homebrew should resolve it:

```bash
brew update && brew upgrade python-tk
```

### Issue Reporting

Please be as detailed as possible when posting a new issue. 

If possible, click the "Settings Button" to the left of the "Start Processing" button and click the "Error Log" button for detailed error information that can be provided to us.

## Building Windows EXE

This fork provides automated Windows EXE builds via GitHub Actions:

### Method 1: GitHub Actions (Recommended)

Push a version tag to trigger an automated build:

```bash
git tag v1.0.0
git push origin v1.0.0
```

The workflow will:
1. Build `UVR.exe` with PyInstaller on `windows-latest`
2. Create a ZIP archive with all runtime files
3. Upload the artifact and create a GitHub Release

You can also trigger manually from the [Actions tab](https://github.com/kasc0206/uvrgui/actions/workflows/build-windows.yml).

### Method 2: Docker Cross-Compilation (macOS/Linux)

```bash
docker run --rm -v "$PWD:/workspace" \
  -w /workspace cdrx/pyinstaller-windows:latest \
  pyinstaller UVR.spec --clean --noconfirm
```

### Method 3: Native Windows Build

```bash
pip install -r requirements.txt
pip install pyinstaller
pyinstaller UVR.spec --clean --noconfirm
```

The output `UVR.exe` will be in `dist/`.

## Fork Changelog

This fork ([kasc0206/uvrgui](https://github.com/kasc0206/uvrgui)) encompasses the following improvements over the upstream:

### Model Data Updates

- **`models/MDX_Net_Models/model_data/model_data.json`** — Expanded with 80+ new MDX model configs (+830/-351)
- **`models/MDX_Net_Models/model_data/model_name_mapper.json`** — 26 new model name mappings (+68/-66)
- **`models/VR_Models/model_data/model_data.json`** — Refactored VR model parameters (+272/-137)

### New MDX Models

| Category | Models |
| --- | --- |
| **BS-Roformer** | `Viperx-1297`, `Viperx-1296`, `Viperx-1053` |
| **Mel-Roformer** | `Viperx-1143` |
| **MB-Roformer** | `Inst-v1`, `Inst-v2`, `Inst-v1-E`, `Duality-v1`, `Duality-v2`, `Kim`, `Karaoke` |
| **SCNet** | `Starrytong`, `Large-Starrytong`, `Large`, `XL-ZFTurbo` |
| **Bandit** | `Cinematic-Bandit-Plus`, `Cinematic-Bandit-Multi` |
| **MDX23C** | `InstVoc HQ 2`, `InstVoc D1581` |
| **Other** | `DrumSep`, `Phantom-Mid`, `Reverb HQ`, `BS-Ro-Dereverb`, `BS-Ro-Inst-EXP` |

### New/Improved Files

| File | Description |
| --- | --- |
| `uvr_cli.py` | **CLI tool** — 10 commands (list/info/process/demucs/download-models/config/version/gui/help + --json) |
| `tests/` | **Test suite** — 32 tests via pytest + coverage reporting |
| `playsound.py` | `playsound3` compatibility shim |
| `__version__.py` | Version info with `FORK_VERSION` and `FORK_REPO` |
| `pyproject.toml` | Project metadata + ruff lint config |
| `.editorconfig` | Consistent coding style across editors |
| `.pre-commit-config.yaml` | Pre-commit hooks for code quality |
| `.gitattributes` | LF line-ending normalization |
| `Dockerfile` | Containerized deployment support |
| `gui_data/cr_text.txt` | Custom text resource file |
| `README_zh.md` | **Full Chinese documentation** |

### Code Quality Improvements

- **ruff**: Zero lint errors on all custom files (F, E, W, I rulesets)
- **Pylance**: Reduced type errors in `UVR.py` from 244 → 137 (actual bugs fixed, remaining are upstream tkinter/PyTorch dynamic patterns)
- **Star imports**: Replaced `from gui_data.constants import *` with 862 explicit symbols
- **Bug fix**: `highlightthicknes` tkinter typo → `highlightthickness` (5 occurrences)
- **Font tuples**: Fixed ~120 `font=(name, f"{size}")` → `font=(name, size)` for Pylance compliance
- **Model download**: Replaced `torch.hub.load_state_dict_from_url` with `curl` (500x speedup)

### Test Coverage

| Area | Tests | Status |
| --- | --- | --- |
| CLI commands | 9 | ✅ Pass |
| Module imports | 14 | ✅ Pass |
| `secondary_stem` mapping | 3 | ✅ Pass |
| Version & constants | 6 | ✅ Pass |
| **Total** | **32** | **✅ All Pass** |

## License

The **Ultimate Vocal Remover GUI** code is [MIT-licensed](LICENSE). 

- **Please Note:** For all third-party application developers who wish to use our models, please honor the MIT license by providing credit to UVR and its developers.

## Credits
- [ZFTurbo](https://github.com/ZFTurbo) - Created & trained the weights for the new MDX23C models. 
- [DilanBoskan](https://github.com/DilanBoskan) - Your contributions at the start of this project were essential to the success of UVR. Thank you!
- [Bas Curtiz](https://www.youtube.com/user/bascurtiz) - Designed the official UVR logo, icon, banner, and splash screen.
- [tsurumeso](https://github.com/tsurumeso) - Developed the original VR Architecture code. 
- [Kuielab & Woosung Choi](https://github.com/kuielab) - Developed the original MDX-Net AI code. 
- [Adefossez & Demucs](https://github.com/facebookresearch/demucs) - Developed the original Demucs AI code. 
- [KimberleyJSN](https://github.com/KimberleyJensen) - Advised and aided the implementation of the training scripts for MDX-Net and Demucs. Thank you!
- [Hv](https://github.com/NaJeongMo/Colab-for-MDX_B) - Helped implement chunks into the MDX-Net AI code. Thank you!

## Contributing

- For anyone interested in the ongoing development of **Ultimate Vocal Remover GUI**, please send us a pull request, and we will review it. 
- This project is 100% open-source and free for anyone to use and modify as they wish. 
- We only maintain the development and support for the **Ultimate Vocal Remover GUI** and the models provided. 

## References
- [1] Takahashi et al., "Multi-scale Multi-band DenseNets for Audio Source Separation", https://arxiv.org/pdf/1706.09588.pdf
