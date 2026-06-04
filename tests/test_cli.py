"""Tests for uvr_cli.py - CLI interface."""

import json
import os
import subprocess
import sys
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).resolve().parent.parent


def run_cli(*args):
    """Run the CLI tool and return (exit_code, stdout, stderr)."""
    result = subprocess.run(
        [sys.executable, str(PROJECT_ROOT / "uvr_cli.py"), *args],
        capture_output=True,
        text=True,
        timeout=30,
    )
    return result.returncode, result.stdout, result.stderr


class TestCLICommands:
    """Test suite for CLI commands."""

    def test_version(self):
        """Test 'uvr_cli.py version' returns version info."""
        rc, out, err = run_cli("version")
        assert rc == 0, f"version command failed: {err}"
        assert "UVR" in out or "version" in out

    def test_help(self):
        """Test 'uvr_cli.py help' prints usage."""
        rc, out, err = run_cli("help")
        assert rc == 0, f"help command failed: {err}"
        assert any(
            cmd in out
            for cmd in ["list", "info", "process", "demucs", "config", "version", "gui", "help"]
        )

    def test_help_default(self):
        """Test running CLI without args shows help."""
        rc, out, err = run_cli()
        assert "用法" in out or rc != 0

    def test_list_models(self):
        """Test 'list' command lists models."""
        rc, out, err = run_cli("list")
        assert rc == 0, f"list command failed: {err}"
        assert len(out) > 0

    def test_list_json(self):
        """Test 'list --json' returns valid JSON."""
        rc, out, err = run_cli("list", "--json")
        assert rc == 0, f"list --json failed: {err}"
        try:
            data = json.loads(out)
        except json.JSONDecodeError:
            pytest.fail(f"Output is not valid JSON: {out[:200]}")
        assert isinstance(data, (list, dict))

    def test_config(self):
        """Test 'config' command runs."""
        rc, out, err = run_cli("config")
        assert rc == 0, f"config command failed: {err}"

    def test_config_json(self):
        """Test 'config --json' returns valid JSON."""
        rc, out, err = run_cli("config", "--json")
        assert rc == 0, f"config --json failed: {err}"
        try:
            data = json.loads(out)
        except json.JSONDecodeError:
            pytest.fail(f"Output is not valid JSON: {out[:200]}")
        assert isinstance(data, dict)

    @pytest.mark.slow
    def test_info_command(self):
        """Test 'info' command with a known model."""
        rc, out, err = run_cli("info", "UVR-DeNoise-Lite")
        assert rc == 0, f"info command failed: {err}"
        assert "UVR-DeNoise-Lite" in out

    def test_info_not_found(self):
        """Test 'info' with non-existent model."""
        rc, out, err = run_cli("info", "NonExistentModel_12345")
        # Should still succeed with a 'not found' message
        assert rc == 0
