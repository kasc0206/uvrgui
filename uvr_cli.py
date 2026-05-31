#!/usr/bin/env python3
"""
UVR CLI 工具 — Ultimate Vocal Remover 命令行助手

用法：
    python uvr_cli.py list          列出所有可用模型及下载状态
    python uvr_cli.py gui           启动图形界面
    python uvr_cli.py info <模型名>  查看模型详情
    python uvr_cli.py help          显示帮助信息
"""

import json
import os
import sys
import glob
from pathlib import Path

BASE_DIR = Path(__file__).parent
MODELS_DIR = BASE_DIR / "models"

# 模型数据文件路径
MODEL_DATA_FILES = {
    "VR Architecture": MODELS_DIR / "VR_Models" / "model_data" / "model_data.json",
    "MDX-Net": MODELS_DIR / "MDX_Net_Models" / "model_data" / "model_data.json",
    "Demucs": MODELS_DIR / "Demucs_Models" / "model_data" / "model_name_mapper.json",
}

MODEL_NAME_MAPPER = {
    "MDX-Net": MODELS_DIR / "MDX_Net_Models" / "model_data" / "model_name_mapper.json",
}

# 模型文件扩展名
MODEL_EXTENSIONS = {
    "VR Architecture": ".pth",
    "MDX-Net": (".ckpt", ".pth"),
    "Demucs": (".th", ".yaml"),
}


def get_model_hash(filename):
    """从文件名提取 MD5 hash（不含扩展名）"""
    return Path(filename).stem


def scan_downloaded_models():
    """扫描已下载的模型文件，返回 {架构: [模型文件名]}"""
    downloaded = {}
    for arch, exts in MODEL_EXTENSIONS.items():
        arch_dir = MODELS_DIR / arch.split()[0] + "_Models"
        files = []
        if isinstance(exts, str):
            exts = (exts,)
        for ext in exts:
            found = list(arch_dir.rglob(f"*{ext}"))
            # 排除 model_data 等配置目录
            found = [f for f in found if "model_data" not in f.parts]
            files.extend(f.stem for f in found)
        if files:
            downloaded[arch] = sorted(set(files))
    return downloaded


def load_model_data(arch):
    """加载指定架构的模型数据 JSON"""
    path = MODEL_DATA_FILES.get(arch)
    if not path or not path.exists():
        return {}
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {}


def load_model_name_mapper(arch):
    """加载模型名称映射（MDX-Net 专用）"""
    path = MODEL_NAME_MAPPER.get(arch)
    if not path or not path.exists():
        return {}
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {}


def get_model_display_name(arch, model_key):
    """获取模型的可读名称"""
    mapper = load_model_name_mapper(arch)
    return mapper.get(model_key, model_key)


def list_models():
    """列出所有可用模型及下载状态"""
    downloaded = scan_downloaded_models()

    for arch, data_path in MODEL_DATA_FILES.items():
        print(f"\n{'='*60}")
        print(f"  {arch}")
        print(f"{'='*60}")

        if not data_path.exists():
            print(f"  [配置缺失] {data_path}")
            continue

        model_data = load_model_data(arch)
        mapper = load_model_name_mapper(arch)

        if not model_data:
            print("  (无模型数据)")
            continue

        # 如果是 Demucs，model_data 本身就是名称映射
        if arch == "Demucs":
            items = list(model_data.items())
            print(f"  共 {len(items)} 个模型配置\n")
            for model_key, display_name in items[:30]:
                model_file = model_key.replace(".yaml", "").replace(".th", "")
                status = "✅ 已下载" if model_file in downloaded.get(arch, []) else "⬜ 未下载"
                print(f"    {display_name:<35} {status}")
            if len(items) > 30:
                print(f"    ... 还有 {len(items) - 30} 个模型未显示")
            continue

        # VR / MDX-Net: model_data 是 {hash: config}
        items = list(model_data.items())
        print(f"  共 {len(items)} 个模型配置\n")

        for model_hash, config in items:
            display_name = mapper.get(model_hash, model_hash[:12] + "...")
            primary = config.get("primary_stem", "?")
            status = "✅" if model_hash in downloaded.get(arch, []) else "⬜"

            extra = ""
            if config.get("is_karaoke"):
                extra = " 🎤卡拉OK"
            if config.get("is_bv_model"):
                extra = " 🎤背景人声"

            print(f"    [{status}] {display_name:<35} → {primary}{extra}")

    print()


def show_model_info(search_term):
    """查看特定模型的信息"""
    found = False
    for arch in MODEL_DATA_FILES:
        model_data = load_model_data(arch)
        mapper = load_model_name_mapper(arch)

        if arch == "Demucs":
            for key, name in model_data.items():
                if search_term.lower() in key.lower() or search_term.lower() in name.lower():
                    print(f"\n{'='*50}")
                    print(f"  架构: {arch}")
                    print(f"  模型: {name}")
                    print(f"  文件: {key}")
                    found = True
            continue

        for model_hash, config in model_data.items():
            name = mapper.get(model_hash, model_hash)
            if search_term.lower() in name.lower() or search_term.lower() in model_hash.lower():
                print(f"\n{'='*50}")
                print(f"  架构: {arch}")
                print(f"  模型: {name}")
                print(f"  Hash: {model_hash}")
                print(f"  输出: {config.get('primary_stem', '?')}")
                if config.get("compensate"):
                    print(f"  补偿: {config['compensate']}")
                if config.get("mdx_dim_f_set"):
                    print(f"  dim_f: {config['mdx_dim_f_set']}")
                if config.get("mdx_dim_t_set"):
                    print(f"  dim_t: {config['mdx_dim_t_set']}")
                if config.get("vr_model_param"):
                    print(f"  参数: {config['vr_model_param']}")
                if config.get("is_karaoke"):
                    print(f"  类型: 卡拉OK")
                if config.get("is_bv_model"):
                    print(f"  类型: 背景人声模型")
                found = True

    if not found:
        print(f"\n未找到匹配 \"{search_term}\" 的模型")


def launch_gui():
    """启动 UVR 图形界面"""
    gui_path = BASE_DIR / "UVR.py"
    if not gui_path.exists():
        print("错误: 找不到 UVR.py")
        sys.exit(1)

    print("正在启动 UVR 图形界面...")
    os.chdir(BASE_DIR)
    os.execv(sys.executable, [sys.executable, str(gui_path)])


def print_help():
    """显示帮助信息"""
    print(__doc__)


def main():
    if len(sys.argv) < 2:
        print_help()
        sys.exit(1)

    command = sys.argv[1]

    if command == "list":
        list_models()
    elif command == "gui":
        launch_gui()
    elif command == "info":
        if len(sys.argv) < 3:
            print("用法: python uvr_cli.py info <模型名>")
            sys.exit(1)
        show_model_info(" ".join(sys.argv[2:]))
    elif command == "help" or command == "--help" or command == "-h":
        print_help()
    else:
        print(f"未知命令: {command}")
        print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
