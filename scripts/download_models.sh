#!/bin/bash
# 预下载 Demucs 模型（使用 curl 加速）
# 用法: bash scripts/download_models.sh

set -e

cd "$(dirname "$0")/.."

# 尝试激活虚拟环境
if [ -f venv/bin/activate ]; then
    source venv/bin/activate
fi

echo "正在下载 Demucs 模型..."
python uvr_cli.py download-models
echo "完成！"
