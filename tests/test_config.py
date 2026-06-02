"""Tests for configuration loading/saving."""
import json
import os
import tempfile
from pathlib import Path

import pytest


@pytest.fixture
def config_file():
    """Create a temporary config file for testing."""
    data = {
        "default_device": None,
        "default_model": "htdemucs",
        "output_format": "wav",
        "two_stem": None,
    }
    tmp = tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False)
    json.dump(data, tmp)
    tmp.close()
    yield Path(tmp.name)
    os.unlink(tmp.name)


def test_config_file_exists():
    """The default config file should exist."""
    cfg = Path(__file__).parent.parent / "uvr_config.json"
    assert cfg.exists(), "uvr_config.json not found in project root"


def test_config_file_valid_json():
    """The config file must be valid JSON."""
    cfg = Path(__file__).parent.parent / "uvr_config.json"
    with open(cfg) as f:
        data = json.load(f)
    assert isinstance(data, dict)


def test_config_has_expected_keys():
    """Config should have the standard keys."""
    cfg = Path(__file__).parent.parent / "uvr_config.json"
    with open(cfg) as f:
        data = json.load(f)
    expected = {"default_device", "default_model", "output_format", "two_stem"}
    assert expected.issubset(data.keys())


def test_config_load_from_cli():
    """load_config() from uvr_cli should return a dict."""
    from uvr_cli import load_config

    cfg = load_config()
    assert isinstance(cfg, dict)


def test_config_save_and_reload():
    """save_config() then load_config() should round-trip."""
    from uvr_cli import load_config, save_config

    save_config({"test_key": "test_value"})
    cfg = load_config()
    assert cfg.get("test_key") == "test_value"

    # Cleanup
    from uvr_cli import CONFIG_FILE
    if CONFIG_FILE.exists():
        with open(CONFIG_FILE) as f:
            data = json.load(f)
        data.pop("test_key", None)
        with open(CONFIG_FILE, "w") as f:
            json.dump(data, f, indent=2)
