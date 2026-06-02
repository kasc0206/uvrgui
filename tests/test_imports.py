"""Tests for __version__.py and basic imports."""
import pytest


def test_version_module():
    """Test that __version__.py can be imported and has required attributes."""
    from __version__ import FORK_REPO, FORK_VERSION, VERSION

    assert VERSION is not None
    assert FORK_VERSION is not None
    assert FORK_REPO is not None
    assert "kasc0206" in FORK_REPO


def test_playsound_import():
    """Test that playsound shim can be imported."""
    import playsound

    assert hasattr(playsound, "playsound")


def test_core_imports():
    """Test that key modules can be imported without errors."""
    import gui_data.constants as c

    assert c.VR_ARCH_TYPE is not None
    assert c.MDX_ARCH_TYPE is not None
    assert c.DEMUCS_ARCH_TYPE is not None

    import gui_data.app_size_values as asv

    assert asv.FONT_SIZE_5 is not None


def test_secondary_stem():
    """Test the secondary_stem mapping function."""
    from separate import secondary_stem

    assert secondary_stem("Vocals") == "Instrumental"
    assert secondary_stem("Instrumental") == "Vocals"
    # Other stems map to "No {Stem}" via STEM_PAIR_MAPPER_FULL
    assert secondary_stem("Drums") is not None
    assert secondary_stem("Bass") is not None
    assert secondary_stem("Other") is not None
    assert secondary_stem("Guitar") is not None


def test_secondary_stem_constants():
    """Test secondary_stem with constant values from gui_data."""
    from gui_data.constants import INST_STEM, VOCAL_STEM
    from separate import secondary_stem

    assert secondary_stem(VOCAL_STEM) == INST_STEM
    assert secondary_stem(INST_STEM) == VOCAL_STEM


def test_save_format_types():
    """Test that save_format handles known format types."""
    from gui_data.constants import FLAC, MP3, WAV
    from separate import save_format

    # Should not raise for known types
    # (actual processing requires valid file, just test the function exists and accepts params)
    assert callable(save_format)


def test_demucs_imports():
    """Test demucs submodule imports."""
    import demucs

    assert hasattr(demucs, "apply")
    assert hasattr(demucs, "demucs")
    assert hasattr(demucs, "hdemucs")
    assert hasattr(demucs, "htdemucs")
