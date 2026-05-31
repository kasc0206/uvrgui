#!/usr/bin/env python3
"""
UVR CLI 工具 — Ultimate Vocal Remover 命令行助手

用法：
    python uvr_cli.py list                      列出所有可用模型及下载状态
    python uvr_cli.py gui                       启动图形界面
    python uvr_cli.py info <关键词>              查看模型详情
    python uvr_cli.py process <音频> [--model]  分离人声/伴奏（使用 Demucs）
    python uvr_cli.py demucs <音频>             使用 Demucs 分离（自动下载模型）
    python uvr_cli.py download-models           预下载 Demucs 模型（使用 curl）
    python uvr_cli.py help                      显示帮助信息

示例：
    python uvr_cli.py process 歌曲.mp3
    python uvr_cli.py demucs 歌曲.flac --two-stem vocals
    python uvr_cli.py process 歌曲.mp3 --model htdemucs_6s
    python uvr_cli.py process 输入文件夹/ --out 输出文件夹/
"""

import argparse
import json
import os
import sys
import time
from pathlib import Path

import numpy as np

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

# 架构名称到模型目录的映射
ARCH_TO_DIR = {
    "VR Architecture": "VR_Models",
    "MDX-Net": "MDX_Net_Models",
    "Demucs": "Demucs_Models",
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
        arch_dir = MODELS_DIR / ARCH_TO_DIR[arch]
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
    search_lower = search_term.lower()

    for arch in MODEL_DATA_FILES:
        model_data = load_model_data(arch)
        mapper = load_model_name_mapper(arch)

        if arch == "Demucs":
            for key, name in model_data.items():
                if search_lower in key.lower() or search_lower in name.lower():
                    print(f"\n{'='*50}")
                    print(f"  架构: {arch}")
                    print(f"  模型: {name}")
                    print(f"  文件: {key}")
                    found = True
            continue

        # 方法1: 遍历 model_data（hash 作为 key）
        for model_key, config in model_data.items():
            # 尝试在 mapper 中找显示名
            display_name = mapper.get(model_key, mapper.get(model_key, None))
            # 如果 mapper 中没找到，尝试用 hash 的反查
            if not display_name:
                display_name = model_key[:16] + "..."

            # 检查搜索词是否匹配
            matched = search_lower in model_key.lower()
            if display_name and not matched:
                matched = search_lower in display_name.lower()
            if config.get("primary_stem") and not matched:
                matched = search_lower in config["primary_stem"].lower()

            if matched:
                print("\n" + "=" * 50)
                print(f"  架构: {arch}")
                print(f"  模型: {display_name}")
                print(f"  标识: {model_key}")
                print(f"  输出: {config.get('primary_stem', '?')}")
                if config.get("compensate"):
                    print(f"  补偿: {config['compensate']}")
                if config.get("mdx_dim_f_set"):
                    print(f"  dim_f: {config['mdx_dim_f_set']}")
                if config.get("mdx_dim_t_set"):
                    print(f"  dim_t: {config['mdx_dim_t_set']}")
                if config.get("mdx_n_fft_scale_set"):
                    print(f"  n_fft: {config['mdx_n_fft_scale_set']}")
                if config.get("vr_model_param"):
                    print(f"  参数: {config['vr_model_param']}")
                if config.get("is_karaoke"):
                    print("  类型: 卡拉OK")
                if config.get("is_bv_model"):
                    print("  类型: 背景人声模型")
                found = True

        # 方法2: 遍历 mapper，查找 model_data 中没有的条目
        for mapper_key, display_name in mapper.items():
            if search_lower in mapper_key.lower() or search_lower in display_name.lower():
                if mapper_key not in model_data:
                    print("\n" + "=" * 50)
                    print(f"  架构: {arch}")
                    print(f"  模型: {display_name}")
                    print(f"  文件: {mapper_key}")
                    print("  (模型配置数据未加载)")
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


def demucs_separate(input_path, output_dir=None, two_stem=None, device=None, model_name="htdemucs"):
    """使用 Demucs 模型分离音频（模型自动下载）

    参数:
        input_path: 输入音频文件或文件夹路径
        output_dir: 输出目录（默认: 输入文件所在目录）
        two_stem: 如果设置，只分离此音源（如 'vocals'），否则分离所有音源
        device: 运行设备（'cpu', 'mps', 'cuda'），默认自动选择
        model_name: Demucs 模型名称（默认: htdemucs）
                    可选: htdemucs, htdemucs_ft, htdemucs_6s, htdemucs_mmi,
                          mdx, mdx_extra, mdx_q, mdx_extra_q, UVR_Model_1 等
    """
    import librosa
    import soundfile as sf
    import torch

    from demucs.apply import apply_model
    from demucs.pretrained import get_model

    input_path = Path(input_path)
    if not input_path.exists():
        print(f"错误: 找不到 {input_path}")
        return

    # 收集音频文件
    audio_files = []
    if input_path.is_file():
        ext = input_path.suffix.lower()
        if ext in (".mp3", ".wav", ".flac", ".ogg", ".m4a", ".wma"):
            audio_files.append(input_path)
        else:
            print(f"错误: 不支持的格式 {ext}")
            return
    else:
        for ext in ("*.mp3", "*.wav", "*.flac", "*.ogg", "*.m4a"):
            audio_files.extend(sorted(input_path.glob(ext)))
        if not audio_files:
            print(f"错误: {input_path} 中没有找到音频文件")
            return

    # 确定输出目录
    if output_dir is None:
        output_dir = input_path.parent if input_path.is_file() else input_path
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # 选择设备
    if device is None:
        if torch.cuda.is_available():
            device = "cuda"
        elif torch.backends.mps.is_available():
            device = "mps"
        else:
            device = "cpu"
    print(f"使用设备: {device}")

    # 加载 Demucs 模型（自动下载）
    print(f"正在加载模型 {model_name}...")
    model = get_model(model_name)
    model.to(device)
    model.eval()
    print("模型加载完成")

    sample_rate = model.samplerate
    sources_list: "list[str]" = model.sources  # type: ignore[assignment]

    if two_stem and two_stem not in sources_list:
        print(f"错误: 音源 '{two_stem}' 不在模型中。可用音源: {sources_list}")
        return

    total_files = len(audio_files)
    for idx, audio_path in enumerate(audio_files, 1):
        stem_name = audio_path.stem
        print(f"\n[{idx}/{total_files}] 处理: {stem_name}")

        # 每个文件独立子目录，避免文件名冲突
        file_out_dir = output_dir / stem_name
        file_out_dir.mkdir(parents=True, exist_ok=True)

        # 加载音频
        print("  加载音频...")
        mix, sr = librosa.load(str(audio_path), sr=sample_rate, mono=False)
        if mix.ndim == 1:
            mix = np.stack([mix, mix], axis=0)

        mix_tensor = torch.tensor(mix[None], dtype=torch.float32, device=device)

        # 运行模型
        print("  正在分离...")
        start = time.time()
        with torch.no_grad():
            sources = apply_model(model, mix_tensor, shifts=1, split=True, overlap=0.25, device=device)
        elapsed = time.time() - start
        print(f"  耗时: {elapsed:.1f}秒")

        # 保存结果
        result: "np.ndarray" = sources[0].cpu().numpy()  # type: ignore[assignment]

        if two_stem:
            # 只分离指定音源和其补集
            stem_idx = sources_list.index(two_stem)
            stem_audio = result[stem_idx]
            other_audio = mix - stem_audio

            out_path = file_out_dir / f"{stem_name}_({two_stem}).wav"
            sf.write(str(out_path), stem_audio.T, sample_rate)
            print(f"  ✅ 已保存: {out_path.name}")

            other_name = f"no_{two_stem}"
            out_path2 = file_out_dir / f"{stem_name}_({other_name}).wav"
            sf.write(str(out_path2), other_audio.T, sample_rate)
            print(f"  ✅ 已保存: {out_path2.name}")
        else:
            for s_idx, source_name in enumerate(sources_list):
                out_path = file_out_dir / f"{stem_name}_({source_name}).wav"
                sf.write(str(out_path), result[s_idx].T, sample_rate)
                print(f"  ✅ 已保存: {out_path.name}")

    print(f"\n✅ 全部完成！输出目录: {output_dir}")


def run_process(args):
    """处理 process 和 demucs 命令"""
    input_path = Path(args.input)
    if not input_path.exists():
        print(f"错误: 找不到 {input_path}")
        sys.exit(1)

    demucs_separate(
        input_path=input_path,
        output_dir=args.output,
        two_stem=args.two_stem,
        device=args.device,
        model_name=args.model,
    )


def download_models():
    """预下载 Demucs 模型（使用 curl 加速）"""
    import yaml

    remote_dir = BASE_DIR / "demucs" / "remote"
    files_txt = remote_dir / "files.txt"

    if not files_txt.exists():
        print("错误: 找不到模型索引文件 demucs/remote/files.txt")
        return

    # 解析 files.txt 获取模型 URL
    base_url = "https://dl.fbaipublicfiles.com/demucs/"
    cache_dir = Path.home() / ".cache" / "torch" / "hub" / "checkpoints"
    cache_dir.mkdir(parents=True, exist_ok=True)

    urls = []
    root = ""
    with open(files_txt) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if line.startswith("root:"):
                root = line.split(":", 1)[1].strip()
            else:
                urls.append(base_url + root + line)

    # 也解析 YAML bag 中的模型签名
    sigs_to_download = set()
    for yaml_file in remote_dir.glob("*.yaml"):
        bag = yaml.safe_load(open(yaml_file))
        for sig in bag.get("models", []):
            sigs_to_download.add(sig)

    # 从 files.txt 中找到对应的 URL
    model_urls = {}
    root = ""
    with open(files_txt) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if line.startswith("root:"):
                root = line.split(":", 1)[1].strip()
            else:
                sig = line.split("-", 1)[0]
                model_urls[sig] = base_url + root + line

    total = len(sigs_to_download)
    if total == 0:
        print("没有需要下载的模型")
        return

    print(f"共 {total} 个模型需要下载\n")

    for i, sig in enumerate(sigs_to_download, 1):
        if sig not in model_urls:
            print(f"[{i}/{total}] ⏭️  {sig} (未知 URL)")
            continue

        url = model_urls[sig]
        filename = url.rstrip("/").split("/")[-1]
        cached_path = cache_dir / filename

        if cached_path.exists():
            size_mb = cached_path.stat().st_size / 1024 / 1024
            print(f"[{i}/{total}] ✅  {filename} ({size_mb:.0f}MB, 已缓存)")
            continue

        print(f"[{i}/{total}] ⬇️  正在下载 {filename} ...")
        start = time.time()
        cmd = ["curl", "-L", "-o", str(cached_path), "--retry", "3", url]
        import subprocess
        result = subprocess.run(cmd, capture_output=True, text=True)
        elapsed = time.time() - start

        if result.returncode == 0:
            size_mb = cached_path.stat().st_size / 1024 / 1024
            speed = size_mb / elapsed if elapsed > 0 else 0
            print(f"[{i}/{total}] ✅  {filename} ({size_mb:.0f}MB, {speed:.0f}MB/s)")
        else:
            print(f"[{i}/{total}] ❌  {filename} 下载失败: {result.stderr.strip()}")

    print(f"\n✅ 全部完成！模型缓存目录: {cache_dir}")


def print_help():
    """显示帮助信息"""
    print(__doc__)


def main():
    parser = argparse.ArgumentParser(
        description="Ultimate Vocal Remover CLI 工具",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("command", nargs="?", help="list | gui | info | process | demucs | help")
    parser.add_argument("input", nargs="?", help="输入音频文件或目录")
    parser.add_argument("--out", "-o", dest="output", help="输出目录")
    parser.add_argument("--two-stem", "-2", dest="two_stem",
                        help="提取指定音源（如 vocals），同时输出其补集")
    parser.add_argument("--device", "-d", default=None,
                        help="运行设备 (cpu/mps/cuda)，默认自动选择")
    parser.add_argument("--model", "-m", default="htdemucs",
                        help="Demucs 模型 (htdemucs/htdemucs_6s/mdx_extra 等)")

    args = parser.parse_args()

    if not args.command or args.command == "help":
        print_help()
        sys.exit(0)

    command = args.command

    if command == "list":
        list_models()
    elif command == "gui":
        launch_gui()
    elif command == "info":
        if not args.input:
            print("用法: python uvr_cli.py info <关键词>")
            sys.exit(1)
        show_model_info(args.input)
    elif command in ("process", "demucs"):
        if not args.input:
            print(f"用法: python uvr_cli.py {command} <音频文件或目录> [选项]")
            sys.exit(1)
        run_process(args)
    elif command == "download-models":
        download_models()
    else:
        print(f"未知命令: {command}")
        print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
