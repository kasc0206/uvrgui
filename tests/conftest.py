"""Pytest configuration and shared fixtures for UVR tests."""
import os
import sys
import tempfile
from pathlib import Path

import pytest

# Add project root to path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))


@pytest.fixture
def temp_dir():
    """Provide a temporary directory for test outputs."""
    with tempfile.TemporaryDirectory() as tmpdir:
        old_cwd = os.getcwd()
        os.chdir(tmpdir)
        yield Path(tmpdir)
        os.chdir(old_cwd)


@pytest.fixture
def sample_wav(temp_dir):
    """Create a minimal valid WAV file for testing."""
    import struct
    import wave

    filepath = temp_dir / "test_sine.wav"
    sample_rate = 22050
    duration = 1.0  # seconds
    num_samples = int(sample_rate * duration)

    with wave.open(str(filepath), "wb") as wav:
        wav.setnchannels(1)
        wav.setsampwidth(2)
        wav.setframerate(sample_rate)
        # Generate a 440Hz sine wave
        for i in range(num_samples):
            import math
            sample = int(16000 * math.sin(2 * math.pi * 440 * i / sample_rate))
            wav.writeframes(struct.pack("<h", sample))

    return filepath


@pytest.fixture
def sample_stereo_wav(temp_dir):
    """Create a minimal stereo WAV file."""
    import math
    import struct
    import wave

    filepath = temp_dir / "test_stereo.wav"
    sample_rate = 44100
    duration = 0.5
    num_samples = int(sample_rate * duration)

    with wave.open(str(filepath), "wb") as wav:
        wav.setnchannels(2)
        wav.setsampwidth(2)
        wav.setframerate(sample_rate)
        for i in range(num_samples):
            val = int(16000 * math.sin(2 * math.pi * 440 * i / sample_rate))
            wav.writeframes(struct.pack("<hh", val, val))

    return filepath
