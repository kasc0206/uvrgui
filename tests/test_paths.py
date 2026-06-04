"""Tests for project path constants."""

from pathlib import Path

import pytest


def test_project_root():
    """The project root should contain key files."""
    root = Path(__file__).parent.parent
    assert (root / "uvr_cli.py").exists()
    assert (root / "UVR.py").exists()
    assert (root / "separate.py").exists()
    assert (root / "pyproject.toml").exists()


def test_models_dir_exists():
    """models/ directory should exist (even if empty)."""
    root = Path(__file__).parent.parent
    models_dir = root / "models"
    assert models_dir.is_dir()


def test_models_subdirs_exist():
    """models/ should contain subdirectories for each architecture."""
    root = Path(__file__).parent.parent
    models_dir = root / "models"
    subdirs = {"VR_Models", "MDX_Net_Models", "Demucs_Models"}
    existing = {d.name for d in models_dir.iterdir() if d.is_dir()}
    # At least one architecture dir should exist
    assert subdirs & existing, f"None of {subdirs} found in {models_dir}"


def test_gui_data_exists():
    """gui_data/ directory with constants."""
    root = Path(__file__).parent.parent
    assert (root / "gui_data" / "constants.py").exists()
    assert (root / "gui_data" / "app_size_values.py").exists()


def test_demucs_package():
    """demucs/ package should be importable."""
    import demucs

    # demucs is a namespace package; verify modules exist as files
    root = Path(__file__).parent.parent
    demucs_dir = root / "demucs"
    assert (demucs_dir / "apply.py").exists()
    assert (demucs_dir / "demucs.py").exists()
    assert (demucs_dir / "hdemucs.py").exists()


def test_config_file_in_root():
    """uvr_config.json should be in the project root."""
    from uvr_cli import CONFIG_FILE

    assert CONFIG_FILE.exists()


def test_base_dir_points_to_root():
    """BASE_DIR should be the project root."""
    from uvr_cli import BASE_DIR

    assert (BASE_DIR / "uvr_cli.py").exists()


def test_models_dir_path():
    """MODELS_DIR should point to models/ in the project root."""
    from uvr_cli import MODELS_DIR

    assert MODELS_DIR.name == "models"
    assert MODELS_DIR.parent.name == Path(__file__).parent.parent.name
