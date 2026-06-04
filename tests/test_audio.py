"""Tests for audio utility functions (lightweight tests only).

Heavy tests (importing separate.py) are excluded because separate.py pulls in
torch, onnx, and other large dependencies that slow down CI significantly.
"""

import pytest


def test_secondary_stem_vocals():
    """secondary_stem(VOCAL_STEM) should return INST_STEM."""
    from gui_data.constants import INST_STEM, VOCAL_STEM, secondary_stem

    assert secondary_stem(VOCAL_STEM) == INST_STEM


def test_secondary_stem_instrumental():
    """secondary_stem(INST_STEM) should return VOCAL_STEM."""
    from gui_data.constants import INST_STEM, VOCAL_STEM, secondary_stem

    assert secondary_stem(INST_STEM) == VOCAL_STEM


def test_stem_constants():
    """VOCAL_STEM and INST_STEM constants are defined."""
    from gui_data.constants import INST_STEM, VOCAL_STEM

    assert VOCAL_STEM is not None
    assert INST_STEM is not None


def test_arch_constants():
    """Architecture type constants are defined."""
    from gui_data.constants import DEMUCS_ARCH_TYPE, MDX_ARCH_TYPE, VR_ARCH_TYPE

    assert VR_ARCH_TYPE is not None
    assert MDX_ARCH_TYPE is not None
    assert DEMUCS_ARCH_TYPE is not None
