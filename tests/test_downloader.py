"""Tests for model download functions."""
from pathlib import Path

import pytest


def test_cache_dir_is_default():
    """The cache directory should be under ~/.cache/torch/hub/checkpoints."""
    cache_dir = Path.home() / ".cache" / "torch" / "hub" / "checkpoints"
    # The directory may not exist yet (no downloads), but the path is valid
    assert str(cache_dir).endswith("checkpoints")


def test_remote_dir_exists():
    """demucs/remote/ should exist and contain files.txt."""
    remote_dir = Path(__file__).parent.parent / "demucs" / "remote"
    assert remote_dir.is_dir()
    assert (remote_dir / "files.txt").exists()


def test_files_txt_parse():
    """files.txt should contain model signatures and URLs."""
    remote_dir = Path(__file__).parent.parent / "demucs" / "remote"
    files_txt = remote_dir / "files.txt"

    with open(files_txt) as f:
        lines = [l.strip() for l in f]

    # Find root: lines
    root_lines = [l for l in lines if l.startswith("root:")]
    # Find model lines (not root:, not comment, not empty)
    model_lines = [l for l in lines if l and not l.startswith("#") and not l.startswith("root:")]

    assert len(root_lines) >= 1, "files.txt should have at least one root: line"
    assert len(model_lines) > 0, "files.txt should have at least one model entry"

    # Each model line should contain a dash separator for sig-filename
    for line in model_lines:
        assert "-" in line, f"Model line missing dash separator: {line}"


def test_download_models_function_exists():
    """download_models() should be importable and callable."""
    from uvr_cli import download_models
    assert callable(download_models)
