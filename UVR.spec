# -*- mode: python ; coding: utf-8 -*-
"""
PyInstaller build script for Ultimate Vocal Remover GUI (Windows).
Usage: pyinstaller UVR.spec
"""

from pathlib import Path

BLOCK_CIPHER_KEY = None
block_cipher = None

# ─── Project paths ───
ROOT = Path(__file__).resolve().parent
GUI_DATA = ROOT / "gui_data"
MODELS = ROOT / "models"
LIB_V5 = ROOT / "lib_v5"
DEMUCS = ROOT / "demucs"

# ─── Collect all data directories ───
a = Analysis(
    [str(ROOT / "UVR.py")],
    pathex=[str(ROOT)],
    binaries=[],
    datas=[
        (str(GUI_DATA / "cr_text.txt"), "gui_data"),
        (str(GUI_DATA / "own_font.json"), "gui_data"),
        (str(GUI_DATA / "img"), "gui_data/img"),
        (str(GUI_DATA / "fonts"), "gui_data/fonts"),
        (str(GUI_DATA / "saved_ensembles"), "gui_data/saved_ensembles"),
        (str(GUI_DATA / "saved_settings"), "gui_data/saved_settings"),
        (str(GUI_DATA / "sv_ttk"), "gui_data/sv_ttk"),
        (str(GUI_DATA / "tkinterdnd2"), "gui_data/tkinterdnd2"),
        (str(GUI_DATA / "tkinterdnd2/tkdnd"), "gui_data/tkinterdnd2/tkdnd"),
        (str(MODELS / "VR_Models/model_data"), "models/VR_Models/model_data"),
        (str(MODELS / "MDX_Net_Models/model_data"), "models/MDX_Net_Models/model_data"),
        (str(MODELS / "Demucs_Models/model_data"), "models/Demucs_Models/model_data"),
        (str(LIB_V5 / "mixer.ckpt"), "lib_v5"),
    ],
    hiddenimports=[
        "PIL",
        "PIL._tkinter_finder",
        "librosa",
        "soundfile",
        "soundfile._soundfile",
        "numpy",
        "torch",
        "torchvision",
        "scipy",
        "scipy.special",
        "scipy.signal",
        "matchering",
        "pyglet",
        "pyperclip",
        "psutil",
        "kthread",
        "cryptography",
        "cryptography.fernet",
        "cryptography.hazmat.primitives",
        "cryptography.hazmat.primitives.kdf.pbkdf2",
        "natsort",
        "audioread",
        "requests",
        "yaml",
        "gui_data",
        "gui_data.constants",
        "gui_data.app_size_values",
        "gui_data.error_handling",
        "gui_data.old_data_check",
        "gui_data.sv_ttk",
        "gui_data.tkinterdnd2",
        "lib_v5",
        "lib_v5.spec_utils",
        "lib_v5.mdxnet",
        "lib_v5.modules",
        "lib_v5.pyrb",
        "lib_v5.tfc_tdf_v3",
        "lib_v5.vr_network",
        "lib_v5.vr_network.layers",
        "lib_v5.vr_network.layers_new",
        "lib_v5.vr_network.model_param_init",
        "lib_v5.vr_network.nets",
        "lib_v5.vr_network.nets_new",
        "demucs",
        "demucs.apply",
        "demucs.demucs",
        "demucs.filtering",
        "demucs.hdemucs",
        "demucs.htdemucs",
        "demucs.model",
        "demucs.model_v2",
        "demucs.pretrained",
        "demucs.repo",
        "demucs.spec",
        "demucs.states",
        "demucs.tasnet",
        "demucs.tasnet_v2",
        "demucs.transformer",
        "demucs.utils",
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        "matplotlib",
        "tensorflow",
        "tensorboard",
        "notebook",
        "jupyter",
        "ipython",
        "test",
        "tests",
        "setuptools",
        "pip",
        "wheel",
        "tkinter.test",
        "idlelib",
        "unittest",
        "pydoc",
    ],
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.contents,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name="UVR",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=str(GUI_DATA / "img" / "UVR.ico") if (GUI_DATA / "img" / "UVR.ico").exists() else None,
)
