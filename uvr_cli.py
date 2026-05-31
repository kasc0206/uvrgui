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
    python uvr_cli.py config                    查看配置
    python uvr_cli.py config --key x --value y  设置配置项
    python uvr_cli.py version                   查看版本信息
    python uvr_cli.py help                      显示帮助信息

示例：
    python uvr_cli.py process 歌曲.mp3
    python uvr_cli.py demucs 歌曲.flac --two-stem vocals
    python uvr_cli.py process 歌曲.mp3 --model htdemucs_6s
    python uvr_cli.py process 输入文件夹/ --out 输出文件夹/
    python uvr_cli.py config --key default_device --value mps
    python uvr_cli.py config --key default_model --value htdemucs_6s
"""

import argparse
import json
import os
import sys
import time
from pathlib import Path

import numpy as np

from __version__ import FORK_REPO, FORK_VERSION, VERSION

CONFIG_FILE = Path(__file__).parent / "uvr_config.json"

# 全局 JSON 输出模式（通过 --json 启用）
JSON_MODE = False


class Output:
    """统一输出接口，支持人类可读和 JSON 两种模式"""

    @staticmethod
    def print(*args, **kwargs):
        if not JSON_MODE:
            print(*args, **kwargs)

    @staticmethod
    def json(data: dict):
        """输出 JSON（始终输出到 stdout）"""
        print(json.dumps(data, ensure_ascii=False, default=str))

    @staticmethod
    def result(data: dict):
        """输出结果：JSON 模式输出 JSON，否则输出可读文本"""
        if JSON_MODE:
            Output.json(data)
        # 可读文本由调用方自行 print

    @staticmethod
    def error(message: str, code: int = 1):
        """输出错误并以指定码退出"""
        if JSON_MODE:
            Output.json({"error": message, "code": code})
        else:
            print(f"错误: {message}", file=sys.stderr)
        sys.exit(code)

    @staticmethod
    def ok(data: dict):
        """输出成功结果并退出"""
        if JSON_MODE:
            Output.json({"ok": True, **data})
        sys.exit(0)


def load_config():
    """加载用户配置文件，不存在时返回空字典"""
    if not CONFIG_FILE.exists():
        return {}
    try:
        with open(CONFIG_FILE) as f:
            cfg = json.load(f)
            return {k: v for k, v in cfg.items() if v is not None}
    except (json.JSONDecodeError, IOError):
        return {}


def save_config(config: dict):
    """保存配置项到文件（保留既有配置）"""
    existing = {}
    if CONFIG_FILE.exists():
        try:
            with open(CONFIG_FILE) as f:
                existing = json.load(f)
            existing.update(config)
        except (json.JSONDecodeError, IOError):
            existing = config
    with open(CONFIG_FILE, "w") as f:
        json.dump(existing, f, indent=2)
        f.write("\n")


def _ensure_model_downloaded(model_name: str):
    """确保 Demucs 模型文件已缓存，缺失时自动用 curl 下载"""
    import subprocess

    import yaml

    remote_dir = BASE_DIR / "demucs" / "remote"
    files_txt = remote_dir / "files.txt"
    cache_dir = Path.home() / ".cache" / "torch" / "hub" / "checkpoints"
    cache_dir.mkdir(parents=True, exist_ok=True)

    base_url = "https://dl.fbaipublicfiles.com/demucs/"
    model_urls = {}
    root = ""
    if files_txt.exists():
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

    yaml_path = remote_dir / f"{model_name}.yaml"
    if not yaml_path.exists():
        return

    bag = yaml.safe_load(open(yaml_path))
    signatures = bag.get("models", [])

    missing = []
    for sig in signatures:
        if sig not in model_urls:
            continue
        url = model_urls[sig]
        filename = url.rstrip("/").split("/")[-1]
        cached_path = cache_dir / filename
        if not cached_path.exists():
            missing.append((filename, url))

    if not missing:
        return

    total = len(missing)
    print(f"需要下载 {total} 个模型文件...")
    for i, (name, url) in enumerate(missing, 1):
        print(f"  [{i}/{total}] {name}")
        subprocess.run(
            ["curl", "-L", "-o", str(cache_dir / name), "--retry", "3", "-s", url],
            capture_output=True, check=True,
        )
    print("模型文件下载完成")


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
    result = {}

    for arch, data_path in MODEL_DATA_FILES.items():
        if not data_path.exists():
            continue

        model_data = load_model_data(arch)
        mapper = load_model_name_mapper(arch)
        arch_models = []

        if arch == "Demucs":
            for model_key, display_name in model_data.items():
                model_file = model_key.replace(".yaml", "").replace(".th", "")
                downloaded_flag = model_file in downloaded.get(arch, [])
                arch_models.append({
                    "name": display_name,
                    "file": model_key,
                    "downloaded": downloaded_flag,
                })
        else:
            for model_hash, config in model_data.items():
                display_name = mapper.get(model_hash, model_hash[:12] + "...")
                primary = config.get("primary_stem", "?")
                downloaded_flag = model_hash in downloaded.get(arch, [])
                entry = {
                    "name": display_name,
                    "hash": model_hash,
                    "output": primary,
                    "downloaded": downloaded_flag,
                }
                if config.get("is_karaoke"):
                    entry["type"] = "karaoke"
                if config.get("is_bv_model"):
                    entry["type"] = "backing_vocals"
                arch_models.append(entry)

        result[arch] = arch_models

    if JSON_MODE:
        Output.json({"models": result, "total": sum(len(v) for v in result.values())})
        return

    # 可读输出
    for arch, models in result.items():
        print(f"\n{'='*60}")
        print(f"  {arch}  ({len(models)} 个模型)")
        print(f"{'='*60}")
        for m in models:
            status = "✅" if m["downloaded"] else "⬜"
            extra = ""
            if m.get("type") == "karaoke":
                extra = " 🎤卡拉OK"
            elif m.get("type") == "backing_vocals":
                extra = " 🎤背景人声"
            if arch == "Demucs":
                print(f"    [{status}] {m['name']:<35}{extra}")
            else:
                print(f"    [{status}] {m['name']:<35} → {m['output']}{extra}")
    print()


def show_model_info(search_term):
    """查看特定模型的信息"""
    found = False
    search_lower = search_term.lower()
    json_results = []

    for arch in MODEL_DATA_FILES:
        model_data = load_model_data(arch)
        mapper = load_model_name_mapper(arch)

        if arch == "Demucs":
            for key, name in model_data.items():
                if search_lower in key.lower() or search_lower in name.lower():
                    entry = {"arch": arch, "name": name, "file": key}
                    if JSON_MODE:
                        json_results.append(entry)
                    else:
                        print(f"\n{'='*50}")
                        print(f"  架构: {arch}")
                        print(f"  模型: {name}")
                        print(f"  文件: {key}")
                    found = True
            continue

        for model_key, config in model_data.items():
            display_name = mapper.get(model_key, model_key[:16] + "...")
            matched = (search_lower in model_key.lower()
                       or (display_name and search_lower in display_name.lower())
                       or search_lower in config.get("primary_stem", "").lower())
            if not matched:
                continue

            entry = {
                "arch": arch,
                "name": display_name,
                "key": model_key,
                "output": config.get("primary_stem", "?"),
            }
            for k in ("compensate", "mdx_dim_f_set", "mdx_dim_t_set",
                      "mdx_n_fft_scale_set", "vr_model_param"):
                if config.get(k):
                    entry[k] = config[k]
            if config.get("is_karaoke"):
                entry["type"] = "karaoke"
            if config.get("is_bv_model"):
                entry["type"] = "backing_vocals"

            if JSON_MODE:
                json_results.append(entry)
            else:
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
                    entry = {"arch": arch, "name": display_name, "file": mapper_key,
                             "note": "模型配置数据未加载"}
                    if JSON_MODE:
                        json_results.append(entry)
                    else:
                        print("\n" + "=" * 50)
                        print(f"  架构: {arch}")
                        print(f"  模型: {display_name}")
                        print(f"  文件: {mapper_key}")
                        print("  (模型配置数据未加载)")
                    found = True

    if JSON_MODE:
        Output.json({"results": json_results, "count": len(json_results)})
        return

    if not found:
        print(f"\n未找到匹配 \"{search_term}\" 的模型")


def launch_gui():
    """启动 UVR 图形界面"""
    gui_path = BASE_DIR / "UVR.py"
    if not gui_path.exists():
        Output.error("找不到 UVR.py")

    if not JSON_MODE:
        print("正在启动 UVR 图形界面...")
    os.chdir(BASE_DIR)
    os.execv(sys.executable, [sys.executable, str(gui_path)])


def demucs_separate(input_path, output_dir=None, two_stem=None, device=None,
                    model_name="htdemucs", output_format="wav"):
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
    import subprocess

    import librosa
    import soundfile as sf
    import torch
    from tqdm import tqdm

    from demucs.apply import apply_model
    from demucs.pretrained import get_model

    # 支持的音频扩展名（含大写的变体）
    AUDIO_EXTS = {".mp3", ".wav", ".flac", ".ogg", ".m4a", ".wma", ".aiff", ".aac", ".opus"}
    # 支持输出格式
    FORMAT_MAP = {"wav": ".wav", "flac": ".flac", "mp3": ".mp3", "aiff": ".aiff"}
    # librosa 可以直接加载的格式
    DIRECT_EXTS = {".mp3", ".wav", ".flac", ".ogg", ".m4a", ".wma", ".aiff"}

    out_ext = FORMAT_MAP.get(output_format, ".wav")
    if output_format not in FORMAT_MAP:
        print(f"警告: 不支持的输出格式 '{output_format}'，使用 wav")

    input_path = Path(input_path)
    if not input_path.exists():
        print(f"错误: 找不到 {input_path}")
        return

    # 收集音频文件
    audio_files = []
    if input_path.is_file():
        ext = input_path.suffix.lower()
        if ext in AUDIO_EXTS:
            audio_files.append(input_path)
        else:
            print(f"错误: 不支持的文件格式 {ext}")
            print(f"支持: {', '.join(sorted(AUDIO_EXTS))}")
            return
    else:
        for ext in sorted(AUDIO_EXTS):
            audio_files.extend(sorted(input_path.glob(f"*{ext}")))
            audio_files.extend(sorted(input_path.glob(f"*{ext.upper()}")))
        if not audio_files:
            print(f"错误: {input_path} 中没有找到音频文件")
            print(f"支持: {', '.join(sorted(AUDIO_EXTS))}")
            return

    # 检查 FFmpeg 是否可用
    ffmpeg_available = False
    try:
        subprocess.run(["ffmpeg", "-version"], capture_output=True, check=True)
        ffmpeg_available = True
    except (subprocess.CalledProcessError, FileNotFoundError):
        pass

    # 确定输出目录
    if output_dir is None:
        output_dir = input_path.parent if input_path.is_file() else input_path
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # 选择设备
    if not JSON_MODE:
        print(f"使用设备: {device}")

    # 自动补全下载模型文件
    _ensure_model_downloaded(model_name)

    # 加载 Demucs 模型
    if not JSON_MODE:
        print(f"正在加载模型 {model_name}...")
    model = get_model(model_name)
    model.to(device)
    model.eval()
    if not JSON_MODE:
        print("模型加载完成")

    sample_rate = model.samplerate
    sources_list: "list[str]" = model.sources  # type: ignore[assignment]

    if two_stem and two_stem not in sources_list:
        print(f"错误: 音源 '{two_stem}' 不在模型中。可用音源: {sources_list}")
        return

    total_files = len(audio_files)
    pbar = tqdm(total=total_files, desc="处理音频", unit="个",
                disable=JSON_MODE, file=sys.stderr)
    for idx, audio_path in enumerate(audio_files, 1):
        stem_name = audio_path.stem
        ext = audio_path.suffix.lower()
        pbar.set_description(f"处理: {stem_name}")

        # 每个文件独立子目录，避免文件名冲突
        file_out_dir = output_dir / stem_name
        file_out_dir.mkdir(parents=True, exist_ok=True)

        # 加载音频
        if ext in DIRECT_EXTS:
            mix, sr = librosa.load(str(audio_path), sr=sample_rate, mono=False)
        elif ffmpeg_available:
            # FFmpeg 临时转码为 WAV
            import tempfile
            with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
                tmp_wav = tmp.name
            subprocess.run(
                ["ffmpeg", "-y", "-i", str(audio_path), "-ar", str(sample_rate),
                 "-ac", "2", "-f", "wav", tmp_wav],
                capture_output=True, check=True,
            )
            mix, sr = librosa.load(tmp_wav, sr=sample_rate, mono=False)
            os.unlink(tmp_wav)
        else:
            pbar.write(f"  ⚠️  跳过 {stem_name}: 格式 {ext} 需要 FFmpeg")
            pbar.update(1)
            continue
        mix, sr = librosa.load(str(audio_path), sr=sample_rate, mono=False)
        if mix.ndim == 1:
            mix = np.stack([mix, mix], axis=0)

        mix_tensor = torch.tensor(mix[None], dtype=torch.float32, device=device)

        # 运行模型
        start = time.time()
        with torch.no_grad():
            sources = apply_model(model, mix_tensor, shifts=1, split=True, overlap=0.25, device=device)
        elapsed = time.time() - start

        # 保存结果
        result: "np.ndarray" = sources[0].cpu().numpy()  # type: ignore[assignment]

        if two_stem:
            # 只分离指定音源和其补集
            stem_idx = sources_list.index(two_stem)
            stem_audio = result[stem_idx]
            other_audio = mix - stem_audio

            out_path = file_out_dir / f"{stem_name}_({two_stem}){out_ext}"
            sf.write(str(out_path), stem_audio.T, sample_rate)

            other_name = f"no_{two_stem}"
            out_path2 = file_out_dir / f"{stem_name}_({other_name}){out_ext}"
            sf.write(str(out_path2), other_audio.T, sample_rate)

            pbar.write(f"  ✅ {out_path.name}  ({elapsed:.1f}s)")
            pbar.write(f"  ✅ {out_path2.name}")
        else:
            for s_idx, source_name in enumerate(sources_list):
                out_path = file_out_dir / f"{stem_name}_({source_name}){out_ext}"
                sf.write(str(out_path), result[s_idx].T, sample_rate)
                pbar.write(f"  ✅ {out_path.name}  ({elapsed:.1f}s)")

        pbar.update(1)

    pbar.close()
    if JSON_MODE:
        Output.json({"ok": True,
                      "output_dir": str(output_dir),
                      "files": len(audio_files),
                      "model": model_name,
                      "device": device,
                      "format": output_format})
    else:
        tqdm.write(f"\n✅ 全部完成！输出目录: {output_dir}")


def run_process(args):
    """处理 process 和 demucs 命令"""
    cfg = load_config()

    input_path = Path(args.input)
    if not input_path.exists():
        Output.error(f"找不到 {input_path}")

    demucs_separate(
        input_path=input_path,
        output_dir=args.output,
        two_stem=args.two_stem or cfg.get("two_stem"),
        device=args.device or cfg.get("default_device"),
        model_name=args.model or cfg.get("default_model", "htdemucs"),
        output_format=args.format or cfg.get("output_format", "wav"),
    )


def cmd_config(args):
    """查看或修改配置"""
    if args.key and args.value:
        save_config({args.key: args.value})
        if JSON_MODE:
            Output.json({"ok": True, "key": args.key, "value": args.value})
        else:
            print(f"✅ 已设置 {args.key} = {args.value}")

    cfg = load_config()
    if JSON_MODE:
        Output.json({"config": cfg})
    else:
        print("当前配置:")
        print(json.dumps(cfg, indent=2, ensure_ascii=False))


def download_models():
    """预下载 Demucs 模型（使用 curl 加速）"""
    import subprocess

    import yaml

    remote_dir = BASE_DIR / "demucs" / "remote"
    cache_dir = Path.home() / ".cache" / "torch" / "hub" / "checkpoints"
    cache_dir.mkdir(parents=True, exist_ok=True)

    base_url = "https://dl.fbaipublicfiles.com/demucs/"
    cache_dir.mkdir(parents=True, exist_ok=True)

    # 解析 files.txt
    model_urls = {}
    root = ""
    files_txt = remote_dir / "files.txt"
    if files_txt.exists():
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

    # 收集所有 YAML bag 中引用的签名
    sigs_to_download = set()
    for yaml_file in sorted(remote_dir.glob("*.yaml")):
        bag = yaml.safe_load(open(yaml_file))
        for sig in bag.get("models", []):
            if sig in model_urls:
                sigs_to_download.add(sig)

    if not sigs_to_download:
        if JSON_MODE:
            Output.json({"ok": True, "downloaded": [], "total": 0})
        else:
            print("没有需要下载的模型")
        return

    results = []
    total = len(sigs_to_download)
    if not JSON_MODE:
        print(f"共 {total} 个模型需要下载\n")

    for i, sig in enumerate(sorted(sigs_to_download), 1):
        url = model_urls[sig]
        filename = url.rstrip("/").split("/")[-1]
        cached_path = cache_dir / filename

        if cached_path.exists():
            size_mb = cached_path.stat().st_size / 1024 / 1024
            results.append({"file": filename, "status": "cached", "size_mb": round(size_mb, 1)})
            if not JSON_MODE:
                print(f"[{i}/{total}] ✅  {filename} ({size_mb:.0f}MB, 已缓存)")
            continue

        if not JSON_MODE:
            print(f"[{i}/{total}] ⬇️  正在下载 {filename} ...")
        start = time.time()
        subprocess.run(["curl", "-L", "-o", str(cached_path), "--retry", "3", "-s", url],
                       capture_output=True, check=True)
        elapsed = time.time() - start
        size_mb = cached_path.stat().st_size / 1024 / 1024
        speed = size_mb / elapsed if elapsed > 0 else 0
        results.append({"file": filename, "status": "downloaded",
                        "size_mb": round(size_mb, 1), "speed_mbps": round(speed, 1)})
        if not JSON_MODE:
            print(f"[{i}/{total}] ✅  {filename} ({size_mb:.0f}MB, {speed:.0f}MB/s)")

    if JSON_MODE:
        Output.json({"ok": True, "downloaded": results, "total": total})
    else:
        print(f"\n✅ 全部完成！模型缓存目录: {cache_dir}")


def print_help():
    """显示帮助信息"""
    print(f"UVR CLI {FORK_VERSION} (基于 {VERSION})")
    print(f"仓库: {FORK_REPO}")
    print()
    print(__doc__)


def main():
    parser = argparse.ArgumentParser(
        description="Ultimate Vocal Remover CLI 工具",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("command", nargs="?", help="list | gui | info | process | demucs | download-models | config | version | help")
    parser.add_argument("input", nargs="?", help="输入音频文件或目录")
    parser.add_argument("--out", "-o", dest="output", help="输出目录")
    parser.add_argument("--two-stem", "-2", dest="two_stem",
                        help="提取指定音源（如 vocals），同时输出其补集")
    parser.add_argument("--device", "-d", default=None,
                        help="运行设备 (cpu/mps/cuda)，默认自动选择")
    parser.add_argument("--model", "-m", default=None,
                        help="Demucs 模型 (htdemucs/htdemucs_6s/mdx_extra 等)")
    parser.add_argument("--format", "-f", default=None,
                        help="输出格式 (wav/flac/mp3/aiff，默认 wav)")
    parser.add_argument("--key", help="配置项名称 (config 命令)")
    parser.add_argument("--value", help="配置项值 (config 命令)")
    parser.add_argument("--json", action="store_true", help="JSON 格式输出（AI 工具调用用）")
    parser.add_argument("--quiet", "-q", action="store_true", help="静默模式，仅输出关键信息")

    args = parser.parse_args()

    # 设为全局
    global JSON_MODE  # noqa: PLW0603
    JSON_MODE = args.json
    if args.quiet:
        JSON_MODE = True  # 静默模式也走 JSON 输出路径

    if not args.command or args.command == "help":
        print_help()
        sys.exit(0)

    # 加载配置作为默认值
    cfg = load_config()
    if args.model is None:
        args.model = cfg.get("default_model")
    if args.device is None:
        args.device = cfg.get("default_device")
    if args.two_stem is None:
        args.two_stem = cfg.get("two_stem")

    command = args.command

    if command == "list":
        list_models()
    elif command == "gui":
        launch_gui()
    elif command == "info":
        if not args.input:
            Output.error("用法: python uvr_cli.py info <关键词>")
        show_model_info(args.input)
    elif command in ("process", "demucs"):
        if not args.input:
            Output.error(f"用法: python uvr_cli.py {command} <音频文件或目录> [选项]")
        run_process(args)
    elif command == "download-models":
        download_models()
    elif command == "version":
        if JSON_MODE:
            Output.json({"version": FORK_VERSION, "base": VERSION, "repo": FORK_REPO})
        else:
            print(f"UVR CLI {FORK_VERSION} (基于 {VERSION})")
            print(f"仓库: {FORK_REPO}")
    elif command == "config":
        cmd_config(args)
    else:
        print(f"未知命令: {command}")
        print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
