"""Tests for model registry functions."""

from pathlib import Path

import pytest


def test_get_model_hash():
    """get_model_hash extracts stem without extension."""
    from uvr_cli import get_model_hash

    assert get_model_hash("abc123.pth") == "abc123"
    assert get_model_hash("abc123.ckpt") == "abc123"
    assert get_model_hash("model.yaml") == "model"


def test_get_model_hash_path():
    """get_model_hash works with Path objects."""
    from uvr_cli import get_model_hash

    assert get_model_hash(Path("some/path/model.th")) == "model"


def test_scan_downloaded_returns_dict():
    """scan_downloaded_models should return a dict."""
    from uvr_cli import scan_downloaded_models

    result = scan_downloaded_models()
    assert isinstance(result, dict)


def test_scan_downloaded_keys():
    """Result keys should be architecture names."""
    from uvr_cli import scan_downloaded_models

    result = scan_downloaded_models()
    valid_keys = {"VR Architecture", "MDX-Net", "Demucs"}
    # Only valid keys, but may be empty
    for k in result:
        assert k in valid_keys, f"Unexpected key: {k}"


def test_load_model_data_vr():
    """load_model_data for VR Architecture should return dict."""
    from uvr_cli import load_model_data

    data = load_model_data("VR Architecture")
    assert isinstance(data, dict)


def test_load_model_data_mdx():
    """load_model_data for MDX-Net should return dict."""
    from uvr_cli import load_model_data

    data = load_model_data("MDX-Net")
    assert isinstance(data, dict)


def test_load_model_data_demucs():
    """load_model_data for Demucs should return dict."""
    from uvr_cli import load_model_data

    data = load_model_data("Demucs")
    assert isinstance(data, dict)


def test_get_model_display_name_unknown():
    """Unknown key should return the key itself."""
    from uvr_cli import get_model_display_name

    name = get_model_display_name("VR Architecture", "nonexistent_key")
    assert name == "nonexistent_key"


def test_model_data_files_exist():
    """Model data JSON files should exist on disk."""
    from uvr_cli import MODEL_DATA_FILES

    for arch, path in MODEL_DATA_FILES.items():
        assert path.exists(), f"{arch} model data not found: {path}"
