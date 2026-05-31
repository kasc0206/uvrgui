#!/usr/bin/env bash
# ────────────────────────────────────────────────────────────
# UVR Windows EXE 本地构建脚本
# 注意：此脚本需要在 Windows 上运行，或在 macOS/Linux 通过
# Docker 交叉编译。建议使用 GitHub Actions（推荐方式）。
# ────────────────────────────────────────────────────────────
set -euo pipefail

echo "=== UVR Windows EXE Builder ==="
echo ""

# 检测平台
case "$(uname -s)" in
  MINGW*|MSYS*|CYGWIN*)
    echo "[✓] Windows 环境检测成功"
    PLATFORM="windows"
    PYTHON="python"
    ;;
  Darwin)
    echo "[!] macOS 检测到 — 无法直接编译 Windows EXE"
    echo ""
    echo "请使用以下方式之一："
    echo "  1. GitHub Actions（推荐）：推送 tag 自动构建"
    echo "     git tag v1.0.0 && git push origin v1.0.0"
    echo ""
    echo "  2. Docker 交叉编译："
    echo "     docker run --rm -v \"\$PWD:/workspace\" \\"
    echo "       -w /workspace cdrx/pyinstaller-windows:latest \\"
    echo "       pyinstaller UVR.spec --clean --noconfirm"
    echo ""
    echo "  3. 在 Windows 虚拟机上运行本脚本"
    exit 1
    ;;
  Linux)
    echo "[!] Linux 检测到 — 尝试通过 Docker 编译 Windows EXE"
    PLATFORM="linux"
    PYTHON="python3"
    ;;
esac

# 检查 PyInstaller
if ! command -v pyinstaller &>/dev/null; then
    echo "[*] 安装 PyInstaller..."
    pip install pyinstaller
fi

# 安装依赖
echo "[*] 安装项目依赖..."
pip install -r requirements.txt

# 检查 UVR.spec
if [ ! -f "UVR.spec" ]; then
    echo "[!] UVR.spec 不存在！"
    exit 1
fi

echo "[*] 开始构建..."
pyinstaller UVR.spec --clean --noconfirm

echo ""
echo "[✓] 构建完成！"
echo "    输出目录: dist/UVR.exe"

# 打包为 ZIP
if command -v 7z &>/dev/null; then
    echo "[*] 创建 ZIP 压缩包..."
    VERSION="${1:-v1.0.0}"
    7z a "UVR_${VERSION}_Windows_x86_64.zip" ./dist/*
    echo "[✓] 压缩包: UVR_${VERSION}_Windows_x86_64.zip"
fi
