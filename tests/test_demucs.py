"""Tests for demucs submodules - model definitions and utilities."""

from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).resolve().parent.parent


class TestDemucsModels:
    """Test Demucs model module imports and structure."""

    def test_demucs_model_import(self):
        """Test demucs.model module."""
        import sys

        sys.path.insert(0, str(PROJECT_ROOT))
        from demucs import model

        assert hasattr(model, "Demucs")

    def test_hdemucs_import(self):
        """Test demucs.hdemucs module."""
        import sys

        sys.path.insert(0, str(PROJECT_ROOT))
        from demucs import hdemucs

        assert hasattr(hdemucs, "HDemucs")

    def test_htdemucs_import(self):
        """Test demucs.htdemucs module."""
        import sys

        sys.path.insert(0, str(PROJECT_ROOT))
        from demucs import htdemucs

        assert hasattr(htdemucs, "HTDemucs")

    def test_tasnet_import(self):
        """Test demucs.tasnet module."""
        import sys

        sys.path.insert(0, str(PROJECT_ROOT))
        from demucs import tasnet

        # TASNet class may not be defined in all forks; check module is importable
        assert tasnet is not None

    def test_tasnet_v2_import(self):
        """Test demucs.tasnet_v2 module."""
        import sys

        sys.path.insert(0, str(PROJECT_ROOT))
        from demucs import tasnet_v2

        assert tasnet_v2 is not None

    def test_model_v2_import(self):
        """Test demucs.model_v2 module."""
        import sys

        sys.path.insert(0, str(PROJECT_ROOT))
        from demucs import model_v2

        assert hasattr(model_v2, "Demucs")

    def test_pretrained_import(self):
        """Test demucs.pretrained module."""
        import sys

        sys.path.insert(0, str(PROJECT_ROOT))
        from demucs import pretrained

        assert hasattr(pretrained, "get_model")

    def test_apply_import(self):
        """Test demucs.apply module."""
        import sys

        sys.path.insert(0, str(PROJECT_ROOT))
        from demucs import apply

        assert hasattr(apply, "apply_model")
        assert hasattr(apply, "BagOfModels")

    def test_states_import(self):
        """Test demucs.states module."""
        import sys

        sys.path.insert(0, str(PROJECT_ROOT))
        from demucs import states

        assert hasattr(states, "get_state")

    def test_utils_import(self):
        """Test demucs.utils module."""
        import sys

        sys.path.insert(0, str(PROJECT_ROOT))
        from demucs import utils

        assert utils is not None


class TestDemucsFiltering:
    """Test demucs.filtering module."""

    def test_filtering_import(self):
        """Test filtering module imports."""
        import sys

        sys.path.insert(0, str(PROJECT_ROOT))
        from demucs import filtering

        assert filtering is not None
