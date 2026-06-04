"""Tests for separate.py - audio separation logic."""

import os
import sys
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))


class TestSeperateAttributes:
    """Test the base SeperateAttributes class."""

    def test_model_data_types(self):
        """Test model data type constants are accessible."""
        from gui_data.constants import DEMUCS_ARCH_TYPE, MDX_ARCH_TYPE, VR_ARCH_TYPE

        assert VR_ARCH_TYPE is not None
        assert MDX_ARCH_TYPE is not None
        assert DEMUCS_ARCH_TYPE is not None

    def test_save_format_exists(self):
        """Test save_format function is callable."""
        from separate import save_format

        assert callable(save_format)


class TestProcessSecondaryModel:
    """Test secondary model processing logic."""

    def test_secondary_stem_mapping(self):
        """Test the secondary_stem function mapping."""
        from separate import secondary_stem
        from gui_data.constants import VOCAL_STEM, INST_STEM

        # Test all defined mappings
        cases = {
            VOCAL_STEM: INST_STEM,
            INST_STEM: VOCAL_STEM,
        }
        for stem, expected in cases.items():
            assert secondary_stem(stem) == expected, f"stem='{stem}' expected={expected}"


class TestPitchShift:
    """Test pitch_shift utility."""

    def test_pitch_shift_exists(self):
        """Test that pitch_shift function exists and is callable."""
        from separate import pitch_shift

        assert callable(pitch_shift)


class TestGatherSources:
    """Test gather_sources function."""

    def test_gather_sources_exists(self):
        """Test gather_sources function exists."""
        from separate import gather_sources

        assert callable(gather_sources)
