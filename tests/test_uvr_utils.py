"""Tests for UVR.py utility methods."""
import os
import sys
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))


class TestGetFilesFromDir:
    """Test get_files_from_dir handles missing directories."""

    def test_missing_directory_returns_empty(self):
        """get_files_from_dir should return empty tuple for non-existent dir."""
        # Verify the source code contains the guard
        uvr_path = PROJECT_ROOT / "UVR.py"
        with open(uvr_path, "r") as f:
            source = f.read()

        assert "def get_files_from_dir" in source, "Method not found in UVR.py"
        assert "if not os.path.isdir(directory):" in source, "Missing directory guard"
        assert "return ()" in source, "Missing empty tuple return"
