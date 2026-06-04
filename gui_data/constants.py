import platform
from pathlib import Path
import json
from gui_data.l10n import _

# Platform Details
OPERATING_SYSTEM = platform.system()
SYSTEM_ARCH = platform.platform()
SYSTEM_PROC = platform.processor()
ARM = "arm"

is_macos = False

CPU = "cpu"
CUDA_DEVICE = "cuda"
DIRECTML_DEVICE = "privateuseone"

# MAIN_FONT_NAME = "Century Gothic"
OPT_SEPARATOR_SAVE = "─" * 25
BG_COLOR = "#0e0e0f"
FG_COLOR = "#13849f"

# Model Types
VR_ARCH_TYPE = "VR Arc"
MDX_ARCH_TYPE = "MDX-Net"
DEMUCS_ARCH_TYPE = "Demucs"
VR_ARCH_PM = _("VR_ARCH_PM")
ENSEMBLE_MODE = _("ENSEMBLE_MODE")
ENSEMBLE_STEM_CHECK = _("ENSEMBLE_STEM_CHECK")
SECONDARY_MODEL = _("SECONDARY_MODEL")
DEMUCS_6_STEM_MODEL = "htdemucs_6s"
DEFAULT = _("DEFAULT")
ALIGNMENT_TOOL = _("ALIGNMENT_TOOL")

SINGLE_FILE = "SINGLE_FILE"
MULTIPLE_FILE = "MULTI_FILE"
MAIN_MULTIPLE_FILE = "MAIN_MULTI_FILE"
CHOOSE_EXPORT_FIR = "CHOOSE_EXPORT_FIR"

DUAL = "dual"
FOUR_STEM = "fourstem"
ANY_STEM = _("ANY_STEM")

DEMUCS_V3_ARCH_TYPE = "Demucs v3"
DEMUCS_V4_ARCH_TYPE = "Demucs v4"
DEMUCS_NEWER_ARCH_TYPES = [DEMUCS_V3_ARCH_TYPE, DEMUCS_V4_ARCH_TYPE]

DEMUCS_V1 = "v1"
DEMUCS_V2 = "v2"
DEMUCS_V3 = "v3"
DEMUCS_V4 = "v4"

DEMUCS_V1_TAG = "v1 | "
DEMUCS_V2_TAG = "v2 | "
DEMUCS_V3_TAG = "v3 | "
DEMUCS_V4_TAG = "v4 | "
DEMUCS_NEWER_TAGS = [DEMUCS_V3_TAG, DEMUCS_V4_TAG]

DEMUCS_VERSION_MAPPER = {
    DEMUCS_V1: DEMUCS_V1_TAG,
    DEMUCS_V2: DEMUCS_V2_TAG,
    DEMUCS_V3: DEMUCS_V3_TAG,
    DEMUCS_V4: DEMUCS_V4_TAG,
}

# Download Center
DOWNLOAD_FAILED = _("DOWNLOAD_FAILED")
DOWNLOAD_STOPPED = _("DOWNLOAD_STOPPED")
DOWNLOAD_COMPLETE = _("DOWNLOAD_COMPLETE")
DOWNLOAD_UPDATE_COMPLETE = _("DOWNLOAD_UPDATE_COMPLETE")
SETTINGS_MENU_EXIT = "exit"
NO_CONNECTION = _("NO_CONNECTION")
VIP_SELECTION = "VIP:"
DEVELOPER_SELECTION = "VIP:"
NO_NEW_MODELS = _("NO_NEW_MODELS")
ENSEMBLE_PARTITION = ": "
NO_MODEL = _("NO_MODEL")
CHOOSE_MODEL = _("CHOOSE_MODEL")
SINGLE_DOWNLOAD = _("SINGLE_DOWNLOAD")
DOWNLOADING_ITEM = _("DOWNLOADING_ITEM")
FILE_EXISTS = _("FILE_EXISTS")
DOWNLOADING_UPDATE = _("DOWNLOADING_UPDATE")
DOWNLOAD_MORE = _("DOWNLOAD_MORE")
IS_KARAOKEE = "is_karaoke"
IS_BV_MODEL = "is_bv_model"
IS_BV_MODEL_REBAL = "is_bv_model_rebalanced"
INPUT_STEM_NAME = _("INPUT_STEM_NAME")

# Menu Options

AUTO_SELECT = _("AUTO_SELECT")

# LINKS
DOWNLOAD_CHECKS = (
    "https://raw.githubusercontent.com/TRvlvr/application_data/main/filelists/download_checks.json"
)
MDX_MODEL_DATA_LINK = "https://raw.githubusercontent.com/TRvlvr/application_data/main/mdx_model_data/model_data_new.json"
VR_MODEL_DATA_LINK = "https://raw.githubusercontent.com/TRvlvr/application_data/main/vr_model_data/model_data_new.json"
MDX23_CONFIG_CHECKS = (
    "https://raw.githubusercontent.com/TRvlvr/application_data/main/mdx_model_data/mdx_c_configs/"
)
BULLETIN_CHECK = "https://raw.githubusercontent.com/TRvlvr/application_data/main/bulletin.txt"

DEMUCS_MODEL_NAME_DATA_LINK = "https://raw.githubusercontent.com/TRvlvr/application_data/main/demucs_model_data/model_name_mapper.json"
MDX_MODEL_NAME_DATA_LINK = "https://raw.githubusercontent.com/TRvlvr/application_data/main/mdx_model_data/model_name_mapper.json"

DONATE_LINK_BMAC = "https://www.buymeacoffee.com/uvr5"
DONATE_LINK_PATREON = "https://www.patreon.com/uvr"

# DOWNLOAD REPOS
NORMAL_REPO = "https://github.com/TRvlvr/model_repo/releases/download/all_public_uvr_models/"
UPDATE_REPO = "https://github.com/TRvlvr/model_repo/releases/download/uvr_update_patches/"

UPDATE_MAC_ARM_REPO = "https://github.com/Anjok07/ultimatevocalremovergui/releases/download/v5.6/Ultimate_Vocal_Remover_v5_6_MacOS_arm64.dmg"
UPDATE_MAC_X86_64_REPO = "https://github.com/Anjok07/ultimatevocalremovergui/releases/download/v5.6/Ultimate_Vocal_Remover_v5_6_MacOS_x86_64.dmg"
UPDATE_LINUX_REPO = "https://github.com/Anjok07/ultimatevocalremovergui#linux-installation"

ISSUE_LINK = "https://github.com/Anjok07/ultimatevocalremovergui/issues/new"
VIP_REPO = (
    b"\xf3\xc2W\x19\x1foI)\xc2\xa9\xcc\xb67(Z\xf5",
    b"gAAAAABjQAIQ-NpNMMxMedpKHHb7ze_nqB05hw0YhbOy3pFzuzDrfqumn8_qvraxEoUpZC5ZXC0gGvfDxFMqyq9VWbYKlA67SUFI_wZB6QoVyGI581vs7kaGfUqlXHIdDS6tQ_U-BfjbEAK9EU_74-R2zXjz8Xzekw==",
)
NO_CODE = "incorrect_code"

# Extensions
ONNX = ".onnx"
CKPT = ".ckpt"
CKPT_C = ".ckptc"
YAML = ".yaml"
PTH = ".pth"
TH_EXT = ".th"
JSON = ".json"

# GUI Buttons
START_PROCESSING = _("START_PROCESSING")
WAIT_PROCESSING = _("WAIT_PROCESSING")
STOP_PROCESSING = _("STOP_PROCESSING")
LOADING_MODELS = _("LOADING_MODELS")

# ---Messages and Logs----

MISSING_MODEL = _("MISSING_MODEL")
MODEL_PRESENT = _("MODEL_PRESENT")

ALL_STEMS = _("ALL_STEMS")
VOCAL_STEM = _("VOCAL_STEM")
INST_STEM = _("INST_STEM")
OTHER_STEM = _("OTHER_STEM")
BASS_STEM = _("BASS_STEM")
DRUM_STEM = _("DRUM_STEM")
GUITAR_STEM = _("GUITAR_STEM")
PIANO_STEM = _("PIANO_STEM")
SYNTH_STEM = _("SYNTH_STEM")
STRINGS_STEM = _("STRINGS_STEM")
WOODWINDS_STEM = _("WOODWINDS_STEM")
BRASS_STEM = _("BRASS_STEM")
WIND_INST_STEM = _("WIND_INST_STEM")
NO_OTHER_STEM = _("NO_OTHER_STEM")
NO_BASS_STEM = _("NO_BASS_STEM")
NO_DRUM_STEM = _("NO_DRUM_STEM")
NO_GUITAR_STEM = _("NO_GUITAR_STEM")
NO_PIANO_STEM = _("NO_PIANO_STEM")
NO_SYNTH_STEM = _("NO_SYNTH_STEM")
NO_STRINGS_STEM = _("NO_STRINGS_STEM")
NO_WOODWINDS_STEM = _("NO_WOODWINDS_STEM")
NO_WIND_INST_STEM = _("NO_WIND_INST_STEM")
NO_BRASS_STEM = _("NO_BRASS_STEM")
PRIMARY_STEM = _("PRIMARY_STEM")
SECONDARY_STEM = _("SECONDARY_STEM")
LEAD_VOCAL_STEM = "lead_only"
BV_VOCAL_STEM = "backing_only"
LEAD_VOCAL_STEM_I = "with_lead_vocals"
BV_VOCAL_STEM_I = "with_backing_vocals"
LEAD_VOCAL_STEM_LABEL = _("LEAD_VOCAL_STEM_LABEL")
BV_VOCAL_STEM_LABEL = _("BV_VOCAL_STEM_LABEL")

VOCAL_STEM_ONLY = f"{VOCAL_STEM} Only"
INST_STEM_ONLY = f"{INST_STEM} Only"
PRIMARY_STEM_ONLY = f"{PRIMARY_STEM} Only"

IS_SAVE_INST_ONLY = f"save_only_inst"
IS_SAVE_VOC_ONLY = f"save_only_voc"

DEVERB_MAPPER = {
    "Main Vocals Only": VOCAL_STEM,
    "Lead Vocals Only": LEAD_VOCAL_STEM_LABEL,
    "Backing Vocals Only": BV_VOCAL_STEM_LABEL,
    "All Vocal Types": "ALL",
}

BALANCE_VALUES = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

# Other Constants
DEMUCS_2_SOURCE = ["instrumental", "vocals"]
DEMUCS_4_SOURCE = ["drums", "bass", "other", "vocals"]

DEMUCS_2_SOURCE_MAPPER = {INST_STEM: 0, VOCAL_STEM: 1}

DEMUCS_4_SOURCE_MAPPER = {BASS_STEM: 0, DRUM_STEM: 1, OTHER_STEM: 2, VOCAL_STEM: 3}

DEMUCS_6_SOURCE_MAPPER = {
    BASS_STEM: 0,
    DRUM_STEM: 1,
    OTHER_STEM: 2,
    VOCAL_STEM: 3,
    GUITAR_STEM: 4,
    PIANO_STEM: 5,
}

DEMUCS_4_SOURCE_LIST = [BASS_STEM, DRUM_STEM, OTHER_STEM, VOCAL_STEM]
DEMUCS_6_SOURCE_LIST = [BASS_STEM, DRUM_STEM, OTHER_STEM, VOCAL_STEM, GUITAR_STEM, PIANO_STEM]

DEMUCS_UVR_MODEL = _("DEMUCS_UVR_MODEL")

CHOOSE_STEM_PAIR = _("CHOOSE_STEM_PAIR")

STEM_SET_MENU = (
    VOCAL_STEM,
    INST_STEM,
    OTHER_STEM,
    BASS_STEM,
    DRUM_STEM,
    GUITAR_STEM,
    PIANO_STEM,
    SYNTH_STEM,
    STRINGS_STEM,
    WOODWINDS_STEM,
    BRASS_STEM,
    WIND_INST_STEM,
)

STEM_SET_MENU_ONLY = list(STEM_SET_MENU) + [OPT_SEPARATOR_SAVE, INPUT_STEM_NAME]

STEM_SET_MENU_2 = (
    OTHER_STEM,
    BASS_STEM,
    DRUM_STEM,
    GUITAR_STEM,
    PIANO_STEM,
    SYNTH_STEM,
    STRINGS_STEM,
    WOODWINDS_STEM,
    BRASS_STEM,
    WIND_INST_STEM,
    "Noise",
    "Reverb",
)

STEM_PAIR_MAPPER = {
    VOCAL_STEM: INST_STEM,
    INST_STEM: VOCAL_STEM,
    LEAD_VOCAL_STEM: BV_VOCAL_STEM,
    BV_VOCAL_STEM: LEAD_VOCAL_STEM,
    PRIMARY_STEM: SECONDARY_STEM,
}

STEM_PAIR_MAPPER_FULL = {
    VOCAL_STEM: INST_STEM,
    INST_STEM: VOCAL_STEM,
    OTHER_STEM: NO_OTHER_STEM,
    BASS_STEM: NO_BASS_STEM,
    DRUM_STEM: NO_DRUM_STEM,
    GUITAR_STEM: NO_GUITAR_STEM,
    PIANO_STEM: NO_PIANO_STEM,
    SYNTH_STEM: NO_SYNTH_STEM,
    STRINGS_STEM: NO_STRINGS_STEM,
    WOODWINDS_STEM: NO_WOODWINDS_STEM,
    BRASS_STEM: NO_BRASS_STEM,
    WIND_INST_STEM: NO_WIND_INST_STEM,
    NO_OTHER_STEM: OTHER_STEM,
    NO_BASS_STEM: BASS_STEM,
    NO_DRUM_STEM: DRUM_STEM,
    NO_GUITAR_STEM: GUITAR_STEM,
    NO_PIANO_STEM: PIANO_STEM,
    NO_SYNTH_STEM: SYNTH_STEM,
    NO_STRINGS_STEM: STRINGS_STEM,
    NO_WOODWINDS_STEM: WOODWINDS_STEM,
    NO_BRASS_STEM: BRASS_STEM,
    NO_WIND_INST_STEM: WIND_INST_STEM,
    PRIMARY_STEM: SECONDARY_STEM,
}

NO_STEM = _("NO_STEM")

NON_ACCOM_STEMS = (
    VOCAL_STEM,
    OTHER_STEM,
    BASS_STEM,
    DRUM_STEM,
    GUITAR_STEM,
    PIANO_STEM,
    SYNTH_STEM,
    STRINGS_STEM,
    WOODWINDS_STEM,
    BRASS_STEM,
    WIND_INST_STEM,
)

MDX_NET_FREQ_CUT = [VOCAL_STEM, INST_STEM]

DEMUCS_4_STEM_OPTIONS = (ALL_STEMS, VOCAL_STEM, OTHER_STEM, BASS_STEM, DRUM_STEM)
DEMUCS_6_STEM_OPTIONS = (
    ALL_STEMS,
    VOCAL_STEM,
    OTHER_STEM,
    BASS_STEM,
    DRUM_STEM,
    GUITAR_STEM,
    PIANO_STEM,
)
DEMUCS_2_STEM_OPTIONS = (VOCAL_STEM, INST_STEM)
DEMUCS_4_STEM_CHECK = (OTHER_STEM, BASS_STEM, DRUM_STEM)

# Menu Dropdowns

VOCAL_PAIR = f"{VOCAL_STEM}/{INST_STEM}"
INST_PAIR = f"{INST_STEM}/{VOCAL_STEM}"
OTHER_PAIR = f"{OTHER_STEM}/{NO_OTHER_STEM}"
DRUM_PAIR = f"{DRUM_STEM}/{NO_DRUM_STEM}"
BASS_PAIR = f"{BASS_STEM}/{NO_BASS_STEM}"
FOUR_STEM_ENSEMBLE = _("FOUR_STEM_ENSEMBLE")
MULTI_STEM_ENSEMBLE = _("MULTI_STEM_ENSEMBLE")

ENSEMBLE_MAIN_STEM = (
    CHOOSE_STEM_PAIR,
    VOCAL_PAIR,
    OTHER_PAIR,
    DRUM_PAIR,
    BASS_PAIR,
    FOUR_STEM_ENSEMBLE,
    MULTI_STEM_ENSEMBLE,
)

MIN_SPEC = _("MIN_SPEC")
MAX_SPEC = _("MAX_SPEC")
AUDIO_AVERAGE = _("AUDIO_AVERAGE")

MAX_MIN = f"{MAX_SPEC}/{MIN_SPEC}"
MAX_MAX = f"{MAX_SPEC}/{MAX_SPEC}"
MAX_AVE = f"{MAX_SPEC}/{AUDIO_AVERAGE}"
MIN_MAX = f"{MIN_SPEC}/{MAX_SPEC}"
MIN_MIX = f"{MIN_SPEC}/{MIN_SPEC}"
MIN_AVE = f"{MIN_SPEC}/{AUDIO_AVERAGE}"
AVE_MAX = f"{AUDIO_AVERAGE}/{MAX_SPEC}"
AVE_MIN = f"{AUDIO_AVERAGE}/{MIN_SPEC}"
AVE_AVE = f"{AUDIO_AVERAGE}/{AUDIO_AVERAGE}"

ENSEMBLE_TYPE = (MAX_MIN, MAX_MAX, MAX_AVE, MIN_MAX, MIN_MIX, MIN_AVE, AVE_MAX, AVE_MIN, AVE_AVE)
ENSEMBLE_TYPE_4_STEM = (MAX_SPEC, MIN_SPEC, AUDIO_AVERAGE)

BATCH_MODE = _("BATCH_MODE")
BETA_VERSION = _("BETA_VERSION")
DEF_OPT = _("DEF_OPT")
USER_INPUT = _("USER_INPUT")
OPT_SEPARATOR = _("OPT_SEPARATOR") * 65

CHUNKS = (
    AUTO_SELECT,
    "1",
    "5",
    "10",
    "15",
    "20",
    "25",
    "30",
    "35",
    "40",
    "45",
    "50",
    "55",
    "60",
    "65",
    "70",
    "75",
    "80",
    "85",
    "90",
    "95",
    "Full",
)

BATCH_SIZE = (DEF_OPT, "2", "3", "4", "5", "6", "7", "8", "9", "10")

VOL_COMPENSATION = (AUTO_SELECT, "1.035", "1.08")

MARGIN_SIZE = ("44100", "22050", "11025")

AUDIO_TOOLS = _("AUDIO_TOOLS")

MANUAL_ENSEMBLE = _("MANUAL_ENSEMBLE")
TIME_STRETCH = _("TIME_STRETCH")
CHANGE_PITCH = _("CHANGE_PITCH")
ALIGN_INPUTS = _("ALIGN_INPUTS")
MATCH_INPUTS = _("MATCH_INPUTS")
COMBINE_INPUTS = _("COMBINE_INPUTS")

if OPERATING_SYSTEM == "Windows" or OPERATING_SYSTEM == "Darwin":
    AUDIO_TOOL_OPTIONS = (MANUAL_ENSEMBLE, TIME_STRETCH, CHANGE_PITCH, ALIGN_INPUTS, MATCH_INPUTS)
else:
    AUDIO_TOOL_OPTIONS = (MANUAL_ENSEMBLE, ALIGN_INPUTS, MATCH_INPUTS)

MANUAL_ENSEMBLE_OPTIONS = (MIN_SPEC, MAX_SPEC, AUDIO_AVERAGE, COMBINE_INPUTS)

PROCESS_METHODS = (VR_ARCH_PM, MDX_ARCH_TYPE, DEMUCS_ARCH_TYPE, ENSEMBLE_MODE, AUDIO_TOOLS)

DEMUCS_SEGMENTS = (
    DEF_OPT,
    "1",
    "5",
    "10",
    "15",
    "20",
    "25",
    "30",
    "35",
    "40",
    "45",
    "50",
    "55",
    "60",
    "65",
    "70",
    "75",
    "80",
    "85",
    "90",
    "95",
    "100",
)

DEMUCS_SHIFTS = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
SEMI_DEF = ["0"]
SEMITONE_SEL = (
    -12,
    -11,
    -10,
    -9,
    -8,
    -7,
    -6,
    -5,
    -4,
    -3,
    -2,
    -1,
    0,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
)

NOUT_SEL = (8, 16, 32, 48, 64)
NOUT_LSTM_SEL = (64, 128)

DEMUCS_OVERLAP = (0.25, 0.50, 0.75, 0.99)
MDX_OVERLAP = (DEF_OPT, 0.25, 0.50, 0.75, 0.99)
MDX23_OVERLAP = range(2, 51)
VR_AGGRESSION = range(0, 51)

TIME_WINDOW_MAPPER = {
    "None": None,
    "1": [0.0625],
    "2": [0.125],
    "3": [0.25],
    "4": [0.5],
    "5": [0.75],
    "6": [1],
    "7": [2],
    "Shifts: Low": [0.0625, 0.5],
    "Shifts: Medium": [0.0625, 0.125, 0.5],
    "Shifts: High": [0.0625, 0.125, 0.25, 0.5],
    # "Shifts: Very High": [0.0625, 0.125, 0.25, 0.5, 0.75, 1],
}

INTRO_MAPPER = {
    "Default": [10],
    "1": [8],
    "2": [6],
    "3": [4],
    "4": [2],
    "Shifts: Low": [1, 10],
    "Shifts: Medium": [1, 10, 8],
    "Shifts: High": [1, 10, 8, 6, 4],
}

VOLUME_MAPPER = {
    "None": (0, [0]),
    "Low": (-4, range(0, 8)),
    "Medium": (-6, range(0, 12)),
    "High": (-6, [x * 0.5 for x in range(0, 25)]),
    "Very High": (-10, [x * 0.5 for x in range(0, 41)]),
}
# "Max": (-10, [x * 0.3 for x in range(0, int(20 / 0.3) + 1)])}

PHASE_MAPPER = {
    "None": [0],
    "Shifts Low": [0, 180],
    "Shifts Medium": [0],
    "Shifts High": [0],
    "Shifts Very High": [0],
}

NONE_P = _("NONE_P")
VLOW_P = _("VLOW_P")
LOW_P = _("LOW_P")
MED_P = _("MED_P")
HIGH_P = _("HIGH_P")
VHIGH_P = _("VHIGH_P")
VMAX_P = _("VMAX_P")

PHASE_SHIFTS_OPT = {
    NONE_P: 190,
    VLOW_P: 180,
    LOW_P: 90,
    MED_P: 45,
    HIGH_P: 20,
    VHIGH_P: 10,
    VMAX_P: 1,
}

VR_WINDOW = ("320", "512", "1024")
VR_CROP = ("256", "512", "1024")
POST_PROCESSES_THREASHOLD_VALUES = ("0.1", "0.2", "0.3")

MDX_POP_PRO = (
    "MDX-NET_Noise_Profile_14_kHz",
    "MDX-NET_Noise_Profile_17_kHz",
    "MDX-NET_Noise_Profile_Full_Band",
)
MDX_POP_STEMS = ("人声", "伴奏", "其他", "鼓点", "贝斯")
MDX_POP_NFFT = ("4096", "5120", "6144", "7680", "8192", "16384")
MDX_POP_DIMF = ("2048", "3072", "4096")
DENOISE_NONE, DENOISE_S, DENOISE_M = "无", "标准", "降噪模型"
MDX_DENOISE_OPTION = [DENOISE_NONE, DENOISE_S, DENOISE_M]
MDX_SEGMENTS = list(range(32, 4000 + 1, 32))

SAVE_ENSEMBLE = _("SAVE_ENSEMBLE")
CLEAR_ENSEMBLE = _("CLEAR_ENSEMBLE")
MENU_SEPARATOR = 35 * "•"
CHOOSE_ENSEMBLE_OPTION = _("CHOOSE_ENSEMBLE_OPTION")
ALL_TYPES = _("ALL_TYPES")
INVALID_ENTRY = _("INVALID_ENTRY")
ENSEMBLE_INPUT_RULE = _("ENSEMBLE_INPUT_RULE")
STEM_INPUT_RULE = _("STEM_INPUT_RULE")

ENSEMBLE_OPTIONS = [OPT_SEPARATOR_SAVE, SAVE_ENSEMBLE, CLEAR_ENSEMBLE]
ENSEMBLE_CHECK = _("ENSEMBLE_CHECK")
KARAOKEE_CHECK = _("KARAOKEE_CHECK")

AUTO_PHASE = _("AUTO_PHASE")
POSITIVE_PHASE = _("POSITIVE_PHASE")
NEGATIVE_PHASE = _("NEGATIVE_PHASE")
OFF_PHASE = _("OFF_PHASE")

ALIGN_PHASE_OPTIONS = [AUTO_PHASE, POSITIVE_PHASE, NEGATIVE_PHASE, OFF_PHASE]

SELECT_SAVED_ENSEMBLE = _("SELECT_SAVED_ENSEMBLE")
SELECT_SAVED_SETTING = _("SELECT_SAVED_SETTING")
ENSEMBLE_OPTION = _("ENSEMBLE_OPTION")
MDX_OPTION = _("MDX_OPTION")
DEMUCS_OPTION = _("DEMUCS_OPTION")
VR_OPTION = _("VR_OPTION")
HELP_OPTION = _("HELP_OPTION")
ERROR_OPTION = _("ERROR_OPTION")
VERIFY_BEGIN = _("VERIFY_BEGIN")
SAMPLE_BEGIN = _("SAMPLE_BEGIN")
MODEL_MISSING_CHECK = _("MODEL_MISSING_CHECK")
OPTION_LIST = [
    VR_OPTION,
    MDX_OPTION,
    DEMUCS_OPTION,
    ENSEMBLE_OPTION,
    ALIGNMENT_TOOL,
    HELP_OPTION,
    ERROR_OPTION,
]

# Menu Strings
VR_MENU = _("VR_MENU")
DEMUCS_MENU = _("DEMUCS_MENU")
MDX_MENU = _("MDX_MENU")
ENSEMBLE_MENU = _("ENSEMBLE_MENU")
HELP_MENU = _("HELP_MENU")
ERROR_MENU = _("ERROR_MENU")
INPUTS_MENU = _("INPUTS_MENU")
ALIGN_MENU = _("ALIGN_MENU")

# Audio Player
PLAYING_SONG = _("PLAYING_SONG")
PAUSE_SONG = _("PAUSE_SONG")
STOP_SONG = _("STOP_SONG")

SELECTED_VER = _("SELECTED_VER")
DETECTED_VER = _("DETECTED_VER")

SAMPLE_MODE_CHECKBOX = lambda v: f"采样模式 ({v}秒)"
REMOVED_FILES = lambda r, e: f"音频输入验证报告：\n\n已移除文件：\n\n{r}\n\n错误详情：\n\n{e}"
ADVANCED_SETTINGS = (
    ENSEMBLE_OPTION,
    MDX_OPTION,
    DEMUCS_OPTION,
    VR_OPTION,
    HELP_OPTION,
    ERROR_OPTION,
)

WAV = "WAV"
FLAC = "FLAC"
MP3 = "MP3"

MP3_BIT_RATES = ("96k", "128k", "160k", "224k", "256k", "320k")
WAV_TYPE = ("PCM_U8", "PCM_16", "PCM_24", "PCM_32", "32-bit Float", "64-bit Float")
GPU_DEVICE_NUM_OPTS = (DEFAULT, "0", "1", "2", "3", "4", "5", "6", "7", "8")

SELECT_SAVED_SET = _("SELECT_SAVED_SET")
SAVE_SETTINGS = _("SAVE_SETTINGS")
RESET_TO_DEFAULT = _("RESET_TO_DEFAULT")
RESET_FULL_TO_DEFAULT = _("RESET_FULL_TO_DEFAULT")
RESET_PM_TO_DEFAULT = _("RESET_PM_TO_DEFAULT")

SAVE_SET_OPTIONS = [OPT_SEPARATOR_SAVE, SAVE_SETTINGS, RESET_TO_DEFAULT]

TIME_PITCH = ("1.0", "2.0", "3.0", "4.0")
TIME_TEXT = _("TIME_TEXT")
PITCH_TEXT = _("PITCH_TEXT")

# RegEx Input Validation
REG_PITCH = r"^[-+]?(1[0]|[0-9]([.][0-9]*)?)$"
REG_TIME = r"^[+]?(1[0]|[0-9]([.][0-9]*)?)$"
REG_COMPENSATION = r"\b^(1[0]|[0-9]([.][0-9]*)?|Auto|None)$\b"
REG_THES_POSTPORCESS = r"\b^([0]([.][0-9]{0,6})?)$\b"
REG_CHUNKS = r"\b^(200|1[0-9][0-9]|[1-9][0-9]?|Auto|Full)$\b"
REG_CHUNKS_DEMUCS = r"\b^(200|1[0-9][0-9]|[1-9][0-9]?|Auto|Full)$\b"
REG_MARGIN = r"\b^[0-9]*$\b"
REG_SEGMENTS = r"\b^(200|1[0-9][0-9]|[1-9][0-9]?|Default)$\b"
REG_SAVE_INPUT = r"\b^([a-zA-Z0-9 -]{0,25})$\b"
REG_INPUT_STEM_NAME = r"^(Wind Inst|[a-zA-Z]{1,25})$"
REG_SEMITONES = r"^-?(20\.00|[01]?\d(\.\d{1,2})?|20)$"
REG_AGGRESSION = r"^[-+]?[0-9]\d*?$"
REG_WINDOW = r"\b^[0-9]{0,4}$\b"
REG_SHIFTS = r"\b^[0-9]*$\b"
REG_BATCHES = r"\b^([0-9]*?|Default)$\b"
REG_OVERLAP = r"\b^([0]([.][0-9]{0,6})?|Default)$\b"  # r"(Default|[0-9]+(\.[0-9]+)?)"#
REG_OVERLAP23 = r"\b^([1][0-9]|[2-9][0-9]*|Default)$\b"  # r'\b^([2-9][0-9]*?|Default)$\b'
REG_MDX_SEG = r"\b(?:" + "|".join([str(num) for num in range(32, 1000001, 32)]) + r")\b"
REG_ALIGN = r"^[-+]?[0-9]\d*?$"
REG_VOL_COMP = r"^\d+\.\d{1,9}$"

# Sub Menu
VR_ARCH_SETTING_LOAD = _("VR_ARCH_SETTING_LOAD")
MDX_SETTING_LOAD = _("MDX_SETTING_LOAD")
DEMUCS_SETTING_LOAD = _("DEMUCS_SETTING_LOAD")
ALL_ARCH_SETTING_LOAD = _("ALL_ARCH_SETTING_LOAD")

# Mappers

DEFAULT_DATA = {
    "chosen_process_method": MDX_ARCH_TYPE,
    "vr_model": CHOOSE_MODEL,
    "aggression_setting": 5,
    "window_size": 512,
    "mdx_segment_size": 256,
    "batch_size": DEF_OPT,
    "crop_size": 256,
    "is_tta": False,
    "is_output_image": False,
    "is_post_process": False,
    "is_high_end_process": False,
    "post_process_threshold": 0.2,
    "vr_voc_inst_secondary_model": NO_MODEL,
    "vr_other_secondary_model": NO_MODEL,
    "vr_bass_secondary_model": NO_MODEL,
    "vr_drums_secondary_model": NO_MODEL,
    "vr_is_secondary_model_activate": False,
    "vr_voc_inst_secondary_model_scale": 0.9,
    "vr_other_secondary_model_scale": 0.7,
    "vr_bass_secondary_model_scale": 0.5,
    "vr_drums_secondary_model_scale": 0.5,
    "demucs_model": CHOOSE_MODEL,
    "segment": DEMUCS_SEGMENTS[0],
    "overlap": DEMUCS_OVERLAP[0],
    "overlap_mdx": MDX_OVERLAP[0],
    "overlap_mdx23": "8",
    "shifts": 2,
    "chunks_demucs": CHUNKS[0],
    "margin_demucs": 44100,
    "is_chunk_demucs": False,
    "is_chunk_mdxnet": False,
    "is_primary_stem_only_Demucs": False,
    "is_secondary_stem_only_Demucs": False,
    "is_split_mode": True,
    "is_demucs_combine_stems": True,  #
    "is_mdx23_combine_stems": True,  #
    "demucs_voc_inst_secondary_model": NO_MODEL,
    "demucs_other_secondary_model": NO_MODEL,
    "demucs_bass_secondary_model": NO_MODEL,
    "demucs_drums_secondary_model": NO_MODEL,
    "demucs_is_secondary_model_activate": False,
    "demucs_voc_inst_secondary_model_scale": 0.9,
    "demucs_other_secondary_model_scale": 0.7,
    "demucs_bass_secondary_model_scale": 0.5,
    "demucs_drums_secondary_model_scale": 0.5,
    "demucs_stems": ALL_STEMS,
    "demucs_pre_proc_model": NO_MODEL,
    "is_demucs_pre_proc_model_activate": False,
    "is_demucs_pre_proc_model_inst_mix": False,
    "mdx_net_model": CHOOSE_MODEL,
    "chunks": CHUNKS[0],
    "margin": 44100,
    "compensate": AUTO_SELECT,
    "is_denoise": False,  #
    "denoise_option": "None",  #
    "phase_option": AUTO_PHASE,
    "phase_shifts": NONE_P,  #
    "is_save_align": False,  # ,
    "is_match_frequency_pitch": True,  #
    "is_match_silence": True,  #
    "is_spec_match": False,  #
    "is_mdx_c_seg_def": False,
    "is_invert_spec": False,  #
    "is_deverb_vocals": False,  #
    "deverb_vocal_opt": "Main Vocals Only",  #
    "voc_split_save_opt": "Lead Only",  #
    "is_mixer_mode": False,
    "mdx_batch_size": DEF_OPT,
    "mdx_voc_inst_secondary_model": NO_MODEL,
    "mdx_other_secondary_model": NO_MODEL,
    "mdx_bass_secondary_model": NO_MODEL,
    "mdx_drums_secondary_model": NO_MODEL,
    "mdx_is_secondary_model_activate": False,
    "mdx_voc_inst_secondary_model_scale": 0.9,
    "mdx_other_secondary_model_scale": 0.7,
    "mdx_bass_secondary_model_scale": 0.5,
    "mdx_drums_secondary_model_scale": 0.5,
    "mdx_stems": ALL_STEMS,
    "is_save_all_outputs_ensemble": True,
    "is_append_ensemble_name": False,
    "chosen_audio_tool": AUDIO_TOOL_OPTIONS[0],
    "choose_algorithm": MANUAL_ENSEMBLE_OPTIONS[0],
    "time_stretch_rate": 2.0,
    "pitch_rate": 2.0,
    "is_time_correction": True,
    "is_gpu_conversion": False,
    "is_primary_stem_only": False,
    "is_secondary_stem_only": False,
    "is_testing_audio": False,  #
    "is_auto_update_model_params": True,  #
    "is_add_model_name": False,
    "is_accept_any_input": False,
    "is_task_complete": False,
    "is_normalization": False,
    "is_use_opencl": False,
    "is_wav_ensemble": False,
    "is_create_model_folder": False,
    "mp3_bit_set": "320k",  #
    "semitone_shift": "0",  #
    "save_format": WAV,
    "wav_type_set": "PCM_16",
    "device_set": DEFAULT,
    "user_code": "",
    "export_path": "",
    "input_paths": [],
    "lastDir": None,
    "time_window": "3",
    "intro_analysis": DEFAULT,
    "db_analysis": "Medium",
    "fileOneEntry": "",
    "fileOneEntry_Full": "",
    "fileTwoEntry": "",
    "fileTwoEntry_Full": "",
    "DualBatch_inputPaths": [],
    "model_hash_table": {},
    "help_hints_var": True,
    "set_vocal_splitter": NO_MODEL,
    "is_set_vocal_splitter": False,  #
    "is_save_inst_set_vocal_splitter": False,  #
    "model_sample_mode": False,
    "model_sample_mode_duration": 30,
}

SETTING_CHECK = (
    "vr_model",
    "aggression_setting",
    "window_size",
    "mdx_segment_size",
    "batch_size",
    "crop_size",
    "is_tta",
    "is_output_image",
    "is_post_process",
    "is_high_end_process",
    "post_process_threshold",
    "vr_voc_inst_secondary_model",
    "vr_other_secondary_model",
    "vr_bass_secondary_model",
    "vr_drums_secondary_model",
    "vr_is_secondary_model_activate",
    "vr_voc_inst_secondary_model_scale",
    "vr_other_secondary_model_scale",
    "vr_bass_secondary_model_scale",
    "vr_drums_secondary_model_scale",
    "demucs_model",
    "segment",
    "overlap",
    "overlap_mdx",
    "shifts",
    "chunks_demucs",
    "margin_demucs",
    "is_chunk_demucs",
    "is_primary_stem_only_Demucs",
    "is_secondary_stem_only_Demucs",
    "is_split_mode",
    "is_demucs_combine_stems",  #
    "is_mdx23_combine_stems",  #
    "demucs_voc_inst_secondary_model",
    "demucs_other_secondary_model",
    "demucs_bass_secondary_model",
    "demucs_drums_secondary_model",
    "demucs_is_secondary_model_activate",
    "demucs_voc_inst_secondary_model_scale",
    "demucs_other_secondary_model_scale",
    "demucs_bass_secondary_model_scale",
    "demucs_drums_secondary_model_scale",
    "demucs_stems",
    "mdx_net_model",
    "chunks",
    "margin",
    "compensate",
    "is_denoise",  #
    "denoise_option",  #
    "phase_option",  #
    "phase_shifts",  #
    "is_save_align",  # ,
    "is_match_silence",
    "is_spec_match",  # ,
    "is_match_frequency_pitch",  #
    "is_mdx_c_seg_def",
    "is_invert_spec",  #
    "is_deverb_vocals",  #
    "deverb_vocal_opt",  #
    "voc_split_save_opt",  #
    "mdx_batch_size",
    "mdx_voc_inst_secondary_model",
    "mdx_other_secondary_model",
    "mdx_bass_secondary_model",
    "mdx_drums_secondary_model",
    "mdx_is_secondary_model_activate",
    "mdx_voc_inst_secondary_model_scale",
    "mdx_other_secondary_model_scale",
    "mdx_bass_secondary_model_scale",
    "mdx_drums_secondary_model_scale",
    "is_save_all_outputs_ensemble",
    "is_append_ensemble_name",
    "chosen_audio_tool",
    "choose_algorithm",
    "time_stretch_rate",
    "pitch_rate",
    "is_time_correction",
    "is_primary_stem_only",
    "is_secondary_stem_only",
    "is_testing_audio",  #
    "is_auto_update_model_params",  #
    "is_add_model_name",
    "is_accept_any_input",
    "is_task_complete",
    "is_create_model_folder",
    "mp3_bit_set",  #
    "semitone_shift",  #
    "save_format",
    "wav_type_set",
    "device_set",
    "user_code",
    "is_gpu_conversion",
    "is_normalization",
    "is_use_opencl",
    "is_wav_ensemble",
    "help_hints_var",
    "set_vocal_splitter",
    "is_set_vocal_splitter",  #
    "is_save_inst_set_vocal_splitter",  #
    "model_sample_mode",
    "model_sample_mode_duration",
    "time_window",
    "intro_analysis",
    "db_analysis",
    "fileOneEntry",
    "fileOneEntry_Full",
    "fileTwoEntry",
    "fileTwoEntry_Full",
    "DualBatch_inputPaths",
)

NEW_LINES = "\n\n"
NEW_LINE = "\n"
NO_LINE = ""

FFMPEG_EXT = (
    ".aac",
    ".aiff",
    ".alac",
    ".flac",
    ".FLAC",
    ".mov",
    ".mp4",
    ".MP4",
    ".m4a",
    ".M4A",
    ".mp2",
    ".mp3",
    "MP3",
    ".mpc",
    ".mpc8",
    ".mpeg",
    ".ogg",
    ".OGG",
    ".tta",
    ".wav",
    ".wave",
    ".WAV",
    ".WAVE",
    ".wma",
    ".webm",
    ".eac3",
    ".mkv",
    ".opus",
    ".OPUS",
)

FFMPEG_MORE_EXT = (
    ".aa",
    ".aac",
    ".ac3",
    ".aiff",
    ".alac",
    ".avi",
    ".f4v",
    ".flac",
    ".flic",
    ".flv",
    ".m4v",
    ".mlv",
    ".mov",
    ".mp4",
    ".m4a",
    ".mp2",
    ".mp3",
    ".mp4",
    ".mpc",
    ".mpc8",
    ".mpeg",
    ".ogg",
    ".tta",
    ".tty",
    ".vcd",
    ".wav",
    ".wma",
)
ANY_EXT = ""

# Secondary Menu Constants

VOCAL_PAIR_PLACEMENT = 1, 2, 3, 4
OTHER_PAIR_PLACEMENT = 5, 6, 7, 8
BASS_PAIR_PLACEMENT = 9, 10, 11, 12
DRUMS_PAIR_PLACEMENT = 13, 14, 15, 16

# Drag n Drop String Checks

DOUBLE_BRACKET = _("DOUBLE_BRACKET")
RIGHT_BRACKET = _("RIGHT_BRACKET")
LEFT_BRACKET = _("LEFT_BRACKET")
# DND CONSTS

MAC_DND_CHECK = ("/Users/", "/Applications/", "/Library/", "/System/")
LINUX_DND_CHECK = ("/home/", "/usr/")
WINDOWS_DND_CHECK = (
    "A:",
    "B:",
    "C:",
    "D:",
    "E:",
    "F:",
    "G:",
    "H:",
    "I:",
    "J:",
    "K:",
    "L:",
    "M:",
    "N:",
    "O:",
    "P:",
    "Q:",
    "R:",
    "S:",
    "T:",
    "U:",
    "V:",
    "W:",
    "X:",
    "Y:",
    "Z:",
)

WOOD_INST_MODEL_HASH = _("WOOD_INST_MODEL_HASH")
WOOD_INST_PARAMS = {"vr_model_param": "4band_v3", "primary_stem": NO_WIND_INST_STEM}

READ_ONLY = "readonly"

FILE_1 = "file1"
FILE_2 = "file2"

FILE_1_LB = _("FILE_1_LB")
FILE_2_LB = _("FILE_2_LB")
BATCH_MODE_DUAL = _("BATCH_MODE_DUAL")

CODEC_DICT = {
    "PCM_U8": {"sample_width": 1, "codec": None},  # 8-bit unsigned PCM
    "PCM_16": {"sample_width": 2, "codec": None},  # 16-bit signed PCM
    "PCM_24": {"sample_width": 3, "codec": None},  # 24-bit signed PCM
    "PCM_32": {"sample_width": 4, "codec": None},  # 32-bit signed PCM
    "FLOAT32": {"sample_width": None, "codec": "pcm_f32le"},  # 32-bit float
    "FLOAT64": {"sample_width": None, "codec": "pcm_f64le"},  # 64-bit float
}


# Manual Downloads
VR_PLACEMENT_TEXT = _("VR_PLACEMENT_TEXT")
MDX_PLACEMENT_TEXT = _("MDX_PLACEMENT_TEXT")
DEMUCS_PLACEMENT_TEXT = _("DEMUCS_PLACEMENT_TEXT")
DEMUCS_V3_V4_PLACEMENT_TEXT = _("DEMUCS_V3_V4_PLACEMENT_TEXT")
MDX_23_NAME = _("MDX_23_NAME")

# Liscense info
if OPERATING_SYSTEM == "Darwin":
    is_macos = True
    LICENSE_OS_SPECIFIC_TEXT = (
        "• This application is intended for those running macOS Catalina and above.\n"
        + "• Application functionality for systems running macOS Mojave or lower is not guaranteed.\n"
        + "• Application functionality for older or budget Mac systems is not guaranteed.\n\n"
    )
elif OPERATING_SYSTEM == "Linux":
    LICENSE_OS_SPECIFIC_TEXT = (
        "• This application is intended for those running Linux Ubuntu 18.04+.\n"
        + "• Application functionality for systems running other Linux platforms is not guaranteed.\n"
        + "• Application functionality for older or budget systems is not guaranteed.\n\n"
    )
elif OPERATING_SYSTEM == "Windows":
    LICENSE_OS_SPECIFIC_TEXT = (
        "• This application is intended for those running Windows 10 or higher.\n"
        + "• Application functionality for systems running Windows 7 or lower is not guaranteed.\n"
        + "• Application functionality for Intel Pentium & Celeron CPUs systems is not guaranteed.\n\n"
    )

LICENSE_TEXT = lambda a, p: (
    f"Current Application Version: Ultimate Vocal Remover {a}\n"
    + f"Current Patch Version: {p}\n\n"
    + "Copyright (c) 2022 Ultimate Vocal Remover\n\n"
    + "UVR is free and open-source, but MIT licensed. Please credit us if you use our\n"
    + f"models or code for projects unrelated to UVR.\n\n{LICENSE_OS_SPECIFIC_TEXT}"
    + "This bundle contains the UVR interface, Python, PyTorch, and other\n"
    + "dependencies needed to run the application effectively.\n\n"
    + "Website Links: This application, System or Service(s) may contain links to\n"
    + "other websites and downloads, and they are solely provided to you as an\n"
    + "additional convenience. You understand and acknowledge that by clicking\n"
    + "or activating such links you are accessing a site or service outside of\n"
    + "this application, and that we do not screen, review, approve, or otherwise\n"
    + "endorse any content or information contained in these linked websites.\n"
    + "You acknowledge and agree that we, our affiliates and partners are not\n"
    + "responsible for the contents of any of these linked websites, including\n"
    + "the accuracy or availability of information provided by the linked websites,\n"
    + "and we make no representations or warranties regarding your use of\n"
    + "the linked websites.\n\n"
    + "This application is MIT Licensed\n\n"
    + "Permission is hereby granted, free of charge, to any person obtaining a copy\n"
    + 'of this software and associated documentation files (the "Software"), to deal\n'
    + "in the Software without restriction, including without limitation the rights\n"
    + "to use, copy, modify, merge, publish, distribute, sublicense, and/or sell\n"
    + "copies of the Software, and to permit persons to whom the Software is\n"
    + "furnished to do so, subject to the following conditions:\n\n"
    + "The above copyright notice and this permission notice shall be included in all\n"
    + "copies or substantial portions of the Software.\n\n"
    + 'THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\n'
    + "IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\n"
    + "FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\n"
    + "AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\n"
    + "LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\n"
    + "OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE\n"
    + "SOFTWARE."
)

# Message Box Text
INVALID_INPUT = _("INVALID_INPUT"), "输入无效。\n\n请验证输入仍然存在或有效，然后重试。"
INVALID_EXPORT = _("INVALID_EXPORT"), "您选择了一个无效的导出目录。\n\n请确保所选目录仍然存在。"
INVALID_ENSEMBLE = _("INVALID_ENSEMBLE"), "您必须选择 2 个或更多模型才能运行集成。"
INVALID_MODEL = _("INVALID_MODEL"), "请先选择一个模型。"
MISSING_MODEL = _("MISSING_MODEL"), "所选模型缺失或无效。"
ERROR_OCCURED = _("ERROR_OCCURED"), "\n\n是否要打开错误日志查看详情？\n"
PROCESS_COMPLETE = "\n处理完成\n"
PROCESS_COMPLETE_2 = _("PROCESS_COMPLETE_2")

# GUI Text Constants
BACK_TO_MAIN_MENU = _("BACK_TO_MAIN_MENU")

# Help Hint Text
INTERNAL_MODEL_ATT = _("INTERNAL_MODEL_ATT")
STOP_HELP = _("STOP_HELP")
SETTINGS_HELP = _("SETTINGS_HELP")
COMMAND_TEXT_HELP = _("COMMAND_TEXT_HELP")
SAVE_CURRENT_SETTINGS_HELP = _("SAVE_CURRENT_SETTINGS_HELP")
PITCH_SHIFT_HELP = (
    "Choose the pitch for processing tracks:\n\n"
    "• Whole numbers indicate semitones.\n"
    "• Using higher pitches may cut the upper bandwidth, even in high-quality models.\n"
    "• Upping the pitch can be better for tracks with deeper vocals.\n"
    "• Dropping the pitch may take more processing time but works well for tracks with high-pitched vocals."
)
AGGRESSION_SETTING_HELP = (
    "Adjust the intensity of primary stem extraction:\n\n"
    "• It ranges from -100 - 100.\n"
    "• Bigger values mean deeper extractions.\n"
    "• Typically, it's set to 5 for vocals & instrumentals. \n"
    "• Values beyond 5 might muddy the sound for non-vocal models."
)
WINDOW_SIZE_HELP = (
    "Select window size to balance quality and speed:\n\n"
    "• 1024 - Quick but lesser quality.\n"
    "• 512 - Medium speed and quality.\n"
    "• 320 - Takes longer but may offer better quality."
)
MDX_SEGMENT_SIZE_HELP = (
    "Pick a segment size to balance speed, resource use, and quality:\n"
    "• Smaller sizes consume less resources.\n"
    "• Bigger sizes consume more resources, but may provide better results.\n"
    "• Default size is 256. Quality can change based on your pick."
)
DEMUCS_STEMS_HELP = (
    "Select a stem for extraction with the chosen model:\n\n"
    "• All Stems - Extracts all available stems.\n"
    '• Vocals - Only the "vocals" stem.\n'
    '• Other - Only the "other" stem.\n'
    '• Bass - Only the "bass" stem.\n'
    '• Drums - Only the "drums" stem.'
)
SEGMENT_HELP = (
    "Adjust segments to manage RAM or V-RAM usage:\n\n"
    "• Smaller sizes consume less resources.\n"
    "• Bigger sizes consume more resources, but may provide better results.\n"
    '• "Default" picks the optimal size.'
)

ENSEMBLE_MAIN_STEM_HELP = (
    "Select the stem type for ensembling:\n\n"
    f"• {VOCAL_PAIR}:\n"
    "  - Primary Stem: Vocals\n"
    "  - Secondary Stem: Instrumental (mixture minus vocals)\n\n"
    f"• {OTHER_PAIR}:\n"
    "  - Primary Stem: Other\n"
    '  - Secondary Stem: No Other (mixture minus "other")\n\n'
    f"• {BASS_PAIR}:\n"
    "  - Primary Stem: Bass\n"
    "  - Secondary Stem: No Bass (mixture minus bass)\n\n"
    f"• {DRUM_PAIR}:\n"
    "  - Primary Stem: Drums\n"
    "  - Secondary Stem: No Drums (mixture minus drums)\n\n"
    f"• {FOUR_STEM_ENSEMBLE}:\n"
    "  - Gathers all 4-stem Demucs models and ensembles all outputs.\n\n"
    f"• {MULTI_STEM_ENSEMBLE}:\n"
    '  - The "Jungle Ensemble" gathers all models and ensembles any related outputs.'
)

ENSEMBLE_TYPE_HELP = (
    "Choose the ensemble algorithm for generating the final output:\n\n"
    f"• {MAX_MIN}:\n"
    '  - Primary stem processed with "Max Spec" algorithm.\n'
    '  - Secondary stem processed with "Min Spec" algorithm.\n\n'
    'Note: For the "4 Stem Ensemble" option, only one algorithm will be displayed.\n\n'
    "Algorithm Details:\n"
    f"• {MAX_SPEC}:\n"
    "  - Produces the highest possible output.\n"
    "  - Ideal for vocal stems for a fuller sound, but might introduce unwanted artifacts.\n"
    "  - Works well with instrumental stems, but avoid using VR Arch models in the ensemble.\n\n"
    f"• {MIN_SPEC}:\n"
    "  - Produces the lowest possible output.\n"
    '  - Ideal for instrumental stems for a cleaner result. Might result in a "muddy" sound.\n\n'
    f"• {AUDIO_AVERAGE}:\n"
    "  - Averages all results together for the final output."
)

ENSEMBLE_LISTBOX_HELP = "Displays all available models for the chosen main stem pair."

if OPERATING_SYSTEM == "darwin":
    IS_GPU_CONVERSION_HELP = (
        "• Use GPU for Processing (if available):\n"
        "  - If checked, the application will attempt to use your GPU for faster processing.\n"
        "  - If a GPU is not detected, it will default to CPU processing.\n"
        "  - GPU processing for MacOS only works with VR Arch models.\n\n"
        "• Please Note:\n"
        "  - CPU processing is significantly slower than GPU processing.\n"
        "  - Only Macs with M1 chips can be used for GPU processing."
    )
else:
    IS_GPU_CONVERSION_HELP = (
        "• Use GPU for Processing (if available):\n"
        "  - If checked, the application will attempt to use your GPU for faster processing.\n"
        "  - If a GPU is not detected, it will default to CPU processing.\n\n"
        "• Please Note:\n"
        "  - CPU processing is significantly slower than GPU processing.\n"
        "  - Only Nvidia GPUs can be used for GPU processing."
    )

IS_TIME_CORRECTION_HELP = "选中后，输出将保留输入的原始 BPM。"
SAVE_STEM_ONLY_HELP = _("SAVE_STEM_ONLY_HELP")
IS_NORMALIZATION_HELP = _("IS_NORMALIZATION_HELP")
IS_CUDA_SELECT_HELP = _("IS_CUDA_SELECT_HELP")
CROP_SIZE_HELP = _("CROP_SIZE_HELP")
IS_TTA_HELP = (
    "This option performs Test-Time-Augmentation to improve the separation quality.\n\n"
    "Note: Having this selected will increase the time it takes to complete a conversion"
)
IS_POST_PROCESS_HELP = (
    "This option can potentially identify leftover instrumental artifacts within the vocal outputs. \nThis option may improve the separation of some songs.\n\n"
    + "Note: Selecting this option can adversely affect the conversion process, depending on the track. Because of this, it is only recommended as a last resort."
)
IS_HIGH_END_PROCESS_HELP = _("IS_HIGH_END_PROCESS_HELP")
SHIFTS_HELP = (
    "Performs multiple predictions with random shifts of the input and averages them.\n\n"
    "• The higher number of shifts, the longer the prediction will take. \n- Not recommended unless you have a GPU."
)
OVERLAP_HELP = (
    "• This option controls the amount of overlap between prediction windows.\n"
    "       - Higher values can provide better results, but will lead to longer processing times.\n"
    "       - You can choose between 0.001-0.999"
)
MDX_OVERLAP_HELP = (
    "• This option controls the amount of overlap between prediction windows.\n"
    "       - Higher values can provide better results, but will lead to longer processing times.\n"
    "       - For Non-MDX23C models: You can choose between 0.001-0.999"
)
OVERLAP_23_HELP = (
    "• This option controls the amount of overlap between prediction windows.\n"
    "       - Higher values can provide better results, but will lead to longer processing times."
)
IS_SEGMENT_DEFAULT_HELP = _("IS_SEGMENT_DEFAULT_HELP")
IS_SPLIT_MODE_HELP = _("IS_SPLIT_MODE_HELP")
IS_DEMUCS_COMBINE_STEMS_HELP = _("IS_DEMUCS_COMBINE_STEMS_HELP")
COMPENSATE_HELP = _("COMPENSATE_HELP")
IS_DENOISE_HELP = (
    "• Standard: This setting reduces the noise created by MDX-Net models.\n"
    "       - This option only reduces noise in non-MDX23 models.\n"
    "• Denoise Model: This setting employs a special denoise model to eliminate noise produced by any MDX-Net model.\n"
    "       - This option works on all MDX-Net models.\n"
    '       - You must have the "UVR-DeNoise-Lite" VR Arch model installed to use this option.\n'
    "• Please Note: Both options will increase separation time."
)

VOC_SPLIT_MODEL_SELECT_HELP = _("VOC_SPLIT_MODEL_SELECT_HELP")
IS_VOC_SPLIT_INST_SAVE_SELECT_HELP = _("IS_VOC_SPLIT_INST_SAVE_SELECT_HELP")
IS_VOC_SPLIT_MODEL_SELECT_HELP = (
    "• When activated, this option auto-processes generated vocal stems, using either a karaoke model to remove lead vocals or another to remove backing vocals.\n"
    "       - This option splits the vocal track into two separate parts: lead vocals and backing vocals, providing two extra vocal outputs.\n"
    "       - The results will be organized in the same way, whether you use a karaoke model or a background vocal model.\n"
    "       - This option does not work in ensemble mode at this time."
)
IS_DEVERB_OPT_HELP = (
    "• Select the vocal type you wish to deverb automatically.\n"
    '       - Example: Choosing "Lead Vocals Only" will only remove reverb from a lead vocal stem.'
)
IS_DEVERB_VOC_HELP = (
    "• This option removes reverb from a vocal stem.\n"
    '       - You must have the "UVR-DeEcho-DeReverb" VR Arch model installed to use this option.\n'
    "       - This option does not work in ensemble mode at this time."
)
IS_FREQUENCY_MATCH_HELP = _("IS_FREQUENCY_MATCH_HELP")
CLEAR_CACHE_HELP = _("CLEAR_CACHE_HELP")
IS_SAVE_ALL_OUTPUTS_ENSEMBLE_HELP = _("IS_SAVE_ALL_OUTPUTS_ENSEMBLE_HELP")
IS_APPEND_ENSEMBLE_NAME_HELP = _("IS_APPEND_ENSEMBLE_NAME_HELP")
IS_WAV_ENSEMBLE_HELP = (
    "Processes ensemble algorithms with waveforms instead of spectrograms when activated:\n"
    "• Might lead to increased distortion.\n"
    "• Waveform ensembling is faster than spectrogram ensembling."
)
DONATE_HELP = _("DONATE_HELP")
IS_INVERT_SPEC_HELP = (
    "Potentially enhances the secondary stem quality:\n"
    "• Inverts primary stem using spectrograms, instead of waveforms.\n"
    "• Slightly slower inversion method."
)
IS_TESTING_AUDIO_HELP = _("IS_TESTING_AUDIO_HELP")
IS_MODEL_TESTING_AUDIO_HELP = _("IS_MODEL_TESTING_AUDIO_HELP")
IS_ACCEPT_ANY_INPUT_HELP = (
    "Allows all types of inputs when enabled, even non-audio formats.\n"
    "For experimental use only. Not recommended for regular use."
)
IS_TASK_COMPLETE_HELP = _("IS_TASK_COMPLETE_HELP")
DELETE_YOUR_SETTINGS_HELP = "Contains your saved settings. Confirmation will be requested before deleting a selected setting."
SET_STEM_NAME_HELP = _("SET_STEM_NAME_HELP")
IS_CREATE_MODEL_FOLDER_HELP = (
    "Two new directories will be generated for the outputs in the export directory after each conversion.\n\n"
    "• Example: \n"
    "─ Export Directory\n"
    "   └── First Directory (Named after the model)\n"
    "           └── Second Directory (Named after the track)\n"
    "                    └── Output File(s)"
)
MDX_DIM_T_SET_HELP = INTERNAL_MODEL_ATT
MDX_DIM_F_SET_HELP = INTERNAL_MODEL_ATT

MDX_N_FFT_SCALE_SET_HELP = _("MDX_N_FFT_SCALE_SET_HELP")
POPUP_COMPENSATE_HELP = (
    f"Select the appropriate volume compensation for the chosen model.\nReminder: {COMPENSATE_HELP}"
)
VR_MODEL_PARAM_HELP = _("VR_MODEL_PARAM_HELP")
CHOSEN_ENSEMBLE_HELP = (
    "Default Ensemble Selections:\n"
    "• Save the current ensemble configuration.\n"
    "• Clear all selected models.\n"
    "Note: You can also select previously saved ensembles."
)
CHOSEN_PROCESS_METHOD_HELP = (
    "Choose a Processing Method:\n"
    "Select from various AI networks and algorithms to process your track:\n"
    "\n"
    "• VR Architecture: Uses magnitude spectrograms for source separation.\n"
    "• MDX-Net: Employs a Hybrid Spectrogram network for source separation.\n"
    "• Demucs v3: Also utilizes a Hybrid Spectrogram network for source separation.\n"
    "• Ensemble Mode: Combine results from multiple models and networks for optimal results.\n"
    "• Audio Tools: Additional utilities for added convenience."
)

INPUT_FOLDER_ENTRY_HELP = "Select Input:\nChoose the audio file(s) you want to process."
INPUT_FOLDER_ENTRY_HELP_2 = "Input Option Menu:\nClick to access the input option menu."
OUTPUT_FOLDER_ENTRY_HELP = (
    "Select Output:\nChoose the directory where the processed files will be saved."
)
INPUT_FOLDER_BUTTON_HELP = (
    "Open Input Folder Button:\nOpen the directory containing the selected input audio file(s)."
)
OUTPUT_FOLDER_BUTTON_HELP = "Open Output Folder Button:\nOpen the selected output folder."
CHOOSE_MODEL_HELP = (
    "Each processing method has its own set of options and models.\n"
    "Choose the model associated with the selected processing method here."
)
FORMAT_SETTING_HELP = _("FORMAT_SETTING_HELP")
SECONDARY_MODEL_ACTIVATE_HELP = "When enabled, the application will perform an additional inference using the selected model(s) above."
SECONDARY_MODEL_HELP = (
    "Choose the Secondary Model:\n"
    "Select the secondary model associated with the stem you want to process with the current method."
)

INPUT_SEC_FIELDS_HELP = "Right click here to choose your inputs!"

SECONDARY_MODEL_SCALE_HELP = (
    "The scale determines how the final audio outputs will be averaged between the primary and secondary models.\n\nFor example:\n\n"
    "• 10% - 10 percent of the main model result will be factored into the final result.\n"
    "• 50% - The results from the main and secondary models will be averaged evenly.\n"
    "• 90% - 90 percent of the main model result will be factored into the final result."
)
PRE_PROC_MODEL_ACTIVATE_HELP = (
    "When enabled, the application will use the selected model to isolate the instrumental stem.\n"
    "Subsequently, all non-vocal stems will be extracted from this generated instrumental.\n"
    "\n"
    "Key Points:\n"
    "• This feature can significantly reduce vocal bleed in non-vocal stems.\n"
    "• Available exclusively in the Demucs tool.\n"
    "• Compatible only with non-vocal and non-instrumental stem outputs.\n"
    "• Expect an increase in total processing time.\n"
    "• Only the VR or MDX-Net Vocal Instrumental/Vocals models can be chosen for this process."
)

AUDIO_TOOLS_HELP = (
    "Select from various audio tools to process your track:\n"
    "\n"
    "• Manual Ensemble: Requires 2 or more selected files as inputs. This allows tracks to be processed using the algorithms from Ensemble Mode.\n"
    "• Time Stretch: Adjust the playback speed of the selected inputs to be faster or slower.\n"
    "• Change Pitch: Modify the pitch of the selected inputs.\n"
    "• Align Inputs: Choose 2 audio file and the application will align them and provide the difference in alignment.\n"
    '    - This tool provides similar functionality to "Utagoe."\n'
    "    - Primary Audio: This is usually a mixture.\n"
    "    - Secondary Audio: This is usually an instrumental.\n"
    "• Matchering: Choose 2 audio files. The matchering algorithm will master the target audio to have the same RMS, FR, peak amplitude, and stereo width as the reference audio."
)

PRE_PROC_MODEL_INST_MIX_HELP = _("PRE_PROC_MODEL_INST_MIX_HELP")
MODEL_SAMPLE_MODE_HELP = (
    "Allows the user to process only part of a track to sample settings or a model without running a full conversion.\n\nNotes:\n\n"
    "• The number in the parentheses is the current number of seconds the generated sample will be.\n"
    '• You can choose the number of seconds to extract from the track in the "Additional Settings" menu.'
)

POST_PROCESS_THREASHOLD_HELP = (
    "Allows the user to control the intensity of the Post_process option.\n\nNotes:\n\n"
    "• Higher values potentially remove more artifacts. However, bleed might increase.\n"
    "• Lower values limit artifact removal."
)

BATCH_SIZE_HELP = (
    "Specify the number of batches to be processed at a time.\n\nNotes:\n\n"
    "• Higher values mean more RAM usage but slightly faster processing times.\n"
    "• Lower values mean less RAM usage but slightly longer processing times.\n"
    "• Batch size value has no effect on output quality."
)

VR_MODEL_NOUT_HELP = ""
VR_MODEL_NOUT_LSTM_HELP = ""

IS_PHASE_HELP = _("IS_PHASE_HELP")
IS_ALIGN_TRACK_HELP = _("IS_ALIGN_TRACK_HELP")
IS_MATCH_SILENCE_HELP = (
    "Aligns the initial silence of the secondary audio with the primary audio.\n"
    "• Note: Avoid using this option if the primary audio begins solely with vocals."
)
IS_MATCH_SPEC_HELP = _("IS_MATCH_SPEC_HELP")

TIME_WINDOW_ALIGN_HELP = (
    "This setting determines the window size for alignment analysis, especially for pairs with minor timing variations:\n"
    "\n"
    "• None: Disables time window analysis.\n"
    "• 1: Analyzes pair by 0.0625-second windows.\n"
    "• 2: Analyzes pair by 0.125-second windows.\n"
    "• 3: Analyzes pair by 0.25-second windows.\n"
    "• 4: Analyzes pair by 0.50-second windows.\n"
    "• 5: Analyzes pair by 0.75-second windows.\n"
    "• 6: Analyzes pair by 1-second windows.\n"
    "• 7: Analyzes pair by 2-second windows.\n"
    "\n"
    "Shifts Options:\n"
    "• Low: Cycles through 0.0625 and 0.5-second windows to find an optimal match.\n"
    "• Medium: Cycles through 0.0625, 0.125, and 0.5-second windows to find an optimal match.\n"
    "• High: Cycles through 0.0625, 0.125, 0.25, and 0.5-second windows to find an optimal match.\n"
    "\n"
    "Important Points to Consider:\n"
    '    - Using the "Shifts" option may require more processing time and might not guarantee better results.\n'
    "    - Opting for smaller analysis windows can increase processing times.\n"
    "    - The best settings are likely to vary based on the specific tracks being processed."
)
INTRO_ANALYSIS_ALIGN_HELP = (
    "This setting determines the portion of the audio input to be analyzed for initial alignment.\n"
    "\n"
    "• Default: Analyzes 10% (or 1/10th) of the audio's total length.\n"
    "• 1: Analyzes 12.5% (or 1/8th) of the audio's total length.\n"
    "• 2: Analyzes 16.67% (or 1/6th) of the audio's total length.\n"
    "• 3: Analyzes 25% (or 1/4th) of the audio's total length.\n"
    "• 4: Analyzes 50% (or half) of the audio's total length.\n"
    "\n"
    "Shifts Options:\n"
    "• Low: Cycles through 2 intro analysis values.\n"
    "• Medium: Cycles through 3 intro analysis values.\n"
    "• High: Cycles through 5 intro analysis values.\n"
    "\n"
    "Important Points to Consider:\n"
    '    - Using the "Shifts" option will require more processing time and might not guarantee better results.\n'
    "    - Optimal settings may vary depending on the specific tracks being processed."
)

VOLUME_ANALYSIS_ALIGN_HELP = (
    "This setting specifies the volume adjustments to be made on the secondary input:\n"
    "\n"
    "• None: No volume adjustments are made.\n"
    "• Low: Analyzes the audio within a 4dB range, adjusting in 1dB increments.\n"
    "• Medium: Analyzes the audio within a 6dB range, adjusting in 1dB increments.\n"
    "• High: Analyzes the audio within a 6dB range, adjusting in 0.5dB increments.\n"
    "• Very High: Analyzes the audio within a 10dB range, adjusting in 0.5dB increments.\n"
    "\n"
    "Important Points to Consider:\n"
    "    - Selecting more extensive analysis options (e.g., High, Very High) will lead to longer processing times.\n"
    "    - Optimal settings might vary based on the specific tracks being processed."
)

PHASE_SHIFTS_ALIGN_HELP = (
    "This setting specifies the phase adjustments to be made on the secondary input:\n"
    "\n"
    "Shifts Options:\n"
    "• None: No phase adjustments are made.\n"
    "• Very Low: Analyzes the audio within range of 2 different phase positions.\n"
    "• Low: Analyzes the audio within range of 4 different phase positions.\n"
    "• Medium: Analyzes the audio within range of 8 different phase positions.\n"
    "• High: Analyzes the audio within range of 18 different phase positions.\n"
    "• Very High: Analyzes the audio within range of 36 different phase positions.\n"
    "• Maximum: Analyzes the audio in all 360 phase positions.\n"
    "\n"
    "Important Points to Consider:\n"
    "    - This option only works with time correction.\n"
    "    - This option can be helpful if one of the inputs were from an analog source.\n"
    "    - Selecting more extensive analysis options (e.g., High, Very High) will lead to longer processing times.\n"
    '    - Selecting "Maximum" can take hours to process.\n'
    "    - Optimal settings might vary based on the specific tracks being processed."
)

# Warning Messages
STORAGE_ERROR = (
    _("STORAGE_ERROR"),
    "主驱动器存储空间不足，无法继续。主驱动器必须至少有 3 GB 的可用空间才能正常运行。\n\n请确保主驱动器至少有 3 GB 可用空间，然后重试。\n\n",
)
STORAGE_WARNING = (
    _("STORAGE_WARNING"),
    "主驱动器存储空间即将用尽。主驱动器必须至少有 3 GB 的可用空间才能正常运行。\n\n",
)
CONFIRM_WARNING = "\n确定要继续吗？"
PROCESS_FAILED = _("PROCESS_FAILED")
EXIT_PROCESS_ERROR = _("EXIT_PROCESS_ERROR"), "请先停止活动进程或等待其完成后再退出。"
EXIT_HALTED_PROCESS_ERROR = _("EXIT_HALTED_PROCESS_ERROR"), "请等待应用完成停止进程后再退出。"
EXIT_DOWNLOAD_ERROR = _("EXIT_DOWNLOAD_ERROR"), "请先停止下载或等待其完成后再退出。"
SET_TO_DEFAULT_PROCESS_ERROR = (
    _("SET_TO_DEFAULT_PROCESS_ERROR"),
    "无法在活动进程中重置所有应用设置。",
)
SET_TO_ANY_PROCESS_ERROR = _("SET_TO_ANY_PROCESS_ERROR"), "无法在活动进程中重置应用设置。"
RESET_ALL_TO_DEFAULT_WARNING = (
    _("RESET_ALL_TO_DEFAULT_WARNING"),
    "所有应用设置将恢复为出厂默认值。\n\n确定要继续吗？",
)
AUDIO_VERIFICATION_CHECK = lambda i, e: (
    f"++++++++++++++++++++++++++++++++++++++++++++++++++++\n\n已移除损坏文件：\n\n{i}\n\n错误详情：\n\n{e}\n++++++++++++++++++++++++++++++++++++++++++++++++++++"
)
INVALID_ONNX_MODEL_ERROR = (
    _("INVALID_ONNX_MODEL_ERROR"),
    "The file selected is not a valid MDX-Net model. Please see the error log for more information.",
)
INVALID_PARAM_MODEL_ERROR = (
    _("INVALID_PARAM_MODEL_ERROR"),
    "Please choose a model param or click 'Cancel'.",
)
UNRECOGNIZED_MODEL = _("UNRECOGNIZED_MODEL"), " 是未知模型。\n\n" + "是否在继续之前选择正确的参数？"
STOP_PROCESS_CONFIRM = (
    _("STOP_PROCESS_CONFIRM"),
    "You are about to stop all active processes.\n\nAre you sure you wish to continue?",
)
NO_ENSEMBLE_SELECTED = _("NO_ENSEMBLE_SELECTED"), "Please select ensemble and try again."
PICKLE_CORRU = (
    _("PICKLE_CORRU"),
    "Unable to load this ensemble.\n\n" + "Would you like to remove this ensemble from your list?",
)
DELETE_ENS_ENTRY = _("DELETE_ENS_ENTRY"), "Are you sure you want to remove this entry?"

# Separation Text
LOADING_MODEL = _("LOADING_MODEL")
INFERENCE_STEP_1 = _("INFERENCE_STEP_1")
INFERENCE_STEP_1_SEC = _("INFERENCE_STEP_1_SEC")
INFERENCE_STEP_1_4_STEM = lambda stem: f"正在推理（{stem}的二级模型）..."
INFERENCE_STEP_1_PRE = _("INFERENCE_STEP_1_PRE")
INFERENCE_STEP_1_VOC_S = _("INFERENCE_STEP_1_VOC_S")
INFERENCE_STEP_2_PRE = lambda pm, m: f"Loading pre-process model ({pm}: {m})..."
INFERENCE_STEP_2_SEC = lambda pm, m: f"Loading secondary model ({pm}: {m})..."
INFERENCE_STEP_2_VOC_S = lambda pm, m: f"Loading vocal splitter model ({pm}: {m})..."
INFERENCE_STEP_2_SEC_CACHED_MODOEL = lambda pm, m: f"Secondary model ({pm}: {m}) cache loaded.\n"
INFERENCE_STEP_2_PRE_CACHED_MODOEL = lambda pm, m: f"Pre-process model ({pm}: {m}) cache loaded.\n"
INFERENCE_STEP_2_SEC_CACHED = _("INFERENCE_STEP_2_SEC_CACHED")
INFERENCE_STEP_2_PRIMARY_CACHED = _("INFERENCE_STEP_2_PRIMARY_CACHED")
INFERENCE_STEP_2 = _("INFERENCE_STEP_2")
INFERENCE_STEP_DEVERBING = _("INFERENCE_STEP_DEVERBING")
SAVING_STEM = _("SAVING_STEM"), " 音轨..."
SAVING_ALL_STEMS = _("SAVING_ALL_STEMS")
ENSEMBLING_OUTPUTS = _("ENSEMBLING_OUTPUTS")
DONE = _("DONE")
ENSEMBLES_SAVED = _("ENSEMBLES_SAVED")

# Additional Text
CHOOSE_PROC_METHOD_MAIN_LABEL = _("CHOOSE_PROC_METHOD_MAIN_LABEL")
SELECT_SAVED_SETTINGS_MAIN_LABEL = _("SELECT_SAVED_SETTINGS_MAIN_LABEL")
CHOOSE_MDX_MODEL_MAIN_LABEL = _("CHOOSE_MDX_MODEL_MAIN_LABEL")
BATCHES_MDX_MAIN_LABEL = _("BATCHES_MDX_MAIN_LABEL")
VOL_COMP_MDX_MAIN_LABEL = _("VOL_COMP_MDX_MAIN_LABEL")
SEGMENT_MDX_MAIN_LABEL = _("SEGMENT_MDX_MAIN_LABEL")
SELECT_VR_MODEL_MAIN_LABEL = _("SELECT_VR_MODEL_MAIN_LABEL")
AGGRESSION_SETTING_MAIN_LABEL = _("AGGRESSION_SETTING_MAIN_LABEL")
WINDOW_SIZE_MAIN_LABEL = _("WINDOW_SIZE_MAIN_LABEL")
CHOOSE_DEMUCS_MODEL_MAIN_LABEL = _("CHOOSE_DEMUCS_MODEL_MAIN_LABEL")
CHOOSE_STEMS_MAIN_LABEL = _("CHOOSE_STEMS_MAIN_LABEL")
CHOOSE_SEGMENT_MAIN_LABEL = _("CHOOSE_SEGMENT_MAIN_LABEL")
ENSEMBLE_OPTIONS_MAIN_LABEL = _("ENSEMBLE_OPTIONS_MAIN_LABEL")
CHOOSE_MAIN_PAIR_MAIN_LABEL = _("CHOOSE_MAIN_PAIR_MAIN_LABEL")
CHOOSE_ENSEMBLE_ALGORITHM_MAIN_LABEL = _("CHOOSE_ENSEMBLE_ALGORITHM_MAIN_LABEL")
AVAILABLE_MODELS_MAIN_LABEL = _("AVAILABLE_MODELS_MAIN_LABEL")
CHOOSE_AUDIO_TOOLS_MAIN_LABEL = _("CHOOSE_AUDIO_TOOLS_MAIN_LABEL")
CHOOSE_MANUAL_ALGORITHM_MAIN_LABEL = _("CHOOSE_MANUAL_ALGORITHM_MAIN_LABEL")
CHOOSE_RATE_MAIN_LABEL = _("CHOOSE_RATE_MAIN_LABEL")
CHOOSE_SEMITONES_MAIN_LABEL = _("CHOOSE_SEMITONES_MAIN_LABEL")
GPU_CONVERSION_MAIN_LABEL = _("GPU_CONVERSION_MAIN_LABEL")
CHANGE_LOG_HEADER = lambda patch: f"补丁版本：\n\n{patch}"
INVALID_INPUT_E = _("INVALID_INPUT_E")
LB_UP = _("LB_UP")
LB_DOWN = _("LB_DOWN")
LB_CLEAR = _("LB_CLEAR")
LB_MOVE_OVER_P = _("LB_MOVE_OVER_P")
LB_MOVE_OVER_S = _("LB_MOVE_OVER_S")
FILE_ONE_MAIN_LABEL = _("FILE_ONE_MAIN_LABEL")
FILE_TWO_MAIN_LABEL = _("FILE_TWO_MAIN_LABEL")
FILE_ONE_MATCH_MAIN_LABEL = _("FILE_ONE_MATCH_MAIN_LABEL")
FILE_TWO_MATCH_MAIN_LABEL = _("FILE_TWO_MATCH_MAIN_LABEL")
TIME_WINDOW_MAIN_LABEL = _("TIME_WINDOW_MAIN_LABEL")
INTRO_ANALYSIS_MAIN_LABEL = _("INTRO_ANALYSIS_MAIN_LABEL")
VOLUME_ADJUSTMENT_MAIN_LABEL = _("VOLUME_ADJUSTMENT_MAIN_LABEL")
SELECT_INPUTS = _("SELECT_INPUTS")
SELECTED_INPUTS = _("SELECTED_INPUTS")
WIDEN_BOX = _("WIDEN_BOX")
CONFIRM_ENTRIES = _("CONFIRM_ENTRIES")
CLOSE_WINDOW = _("CLOSE_WINDOW")
DUAL_AUDIO_PROCESSING = _("DUAL_AUDIO_PROCESSING")
CANCEL_TEXT = _("CANCEL_TEXT")
CONFIRM_TEXT = _("CONFIRM_TEXT")
SELECT_MODEL_TEXT = _("SELECT_MODEL_TEXT")
NONE_SELECTED = _("NONE_SELECTED")
SAVE_TEXT = _("SAVE_TEXT")
OVERLAP_TEXT = _("OVERLAP_TEXT")
ACCEPT_ANY_INPUT_TEXT = _("ACCEPT_ANY_INPUT_TEXT")
ACTIVATE_PRE_PROCESS_MODEL_TEXT = _("ACTIVATE_PRE_PROCESS_MODEL_TEXT")
ACTIVATE_SECONDARY_MODEL_TEXT = _("ACTIVATE_SECONDARY_MODEL_TEXT")
ADDITIONAL_MENUS_INFORMATION_TEXT = _("ADDITIONAL_MENUS_INFORMATION_TEXT")
ADDITIONAL_SETTINGS_TEXT = _("ADDITIONAL_SETTINGS_TEXT")
ADVANCED_ALIGN_TOOL_OPTIONS_TEXT = _("ADVANCED_ALIGN_TOOL_OPTIONS_TEXT")
ADVANCED_DEMUCS_OPTIONS_TEXT = _("ADVANCED_DEMUCS_OPTIONS_TEXT")
ADVANCED_ENSEMBLE_OPTIONS_TEXT = _("ADVANCED_ENSEMBLE_OPTIONS_TEXT")
ADVANCED_MDXNET23_OPTIONS_TEXT = _("ADVANCED_MDXNET23_OPTIONS_TEXT")
ADVANCED_MDXNET_OPTIONS_TEXT = _("ADVANCED_MDXNET_OPTIONS_TEXT")
ADVANCED_OPTION_MENU_TEXT = _("ADVANCED_OPTION_MENU_TEXT")
ADVANCED_VR_OPTIONS_TEXT = _("ADVANCED_VR_OPTIONS_TEXT")
AGGRESSION_SETTING_TEXT = _("AGGRESSION_SETTING_TEXT")
APPEND_ENSEMBLE_NAME_TEXT = _("APPEND_ENSEMBLE_NAME_TEXT")
APPLICATION_DOWNLOAD_CENTER_TEXT = _("APPLICATION_DOWNLOAD_CENTER_TEXT")
APPLICATION_UPDATES_TEXT = _("APPLICATION_UPDATES_TEXT")
AUDIO_FORMAT_SETTINGS_TEXT = _("AUDIO_FORMAT_SETTINGS_TEXT")
BALANCE_VALUE_TEXT = _("BALANCE_VALUE_TEXT")
BATCH_SIZE_TEXT = _("BATCH_SIZE_TEXT")
BV_MODEL_TEXT = _("BV_MODEL_TEXT")
CHANGE_MODEL_DEFAULT_TEXT = _("CHANGE_MODEL_DEFAULT_TEXT")
CHANGE_MODEL_DEFAULTS_TEXT = _("CHANGE_MODEL_DEFAULTS_TEXT")
CHANGE_PARAMETERS_TEXT = _("CHANGE_PARAMETERS_TEXT")
CHOOSE_ADVANCED_MENU_TEXT = _("CHOOSE_ADVANCED_MENU_TEXT")
CHOOSE_MODEL_PARAM_TEXT = _("CHOOSE_MODEL_PARAM_TEXT")
CLEAR_AUTOSET_CACHE_TEXT = _("CLEAR_AUTOSET_CACHE_TEXT")
COMBINE_STEMS_TEXT = _("COMBINE_STEMS_TEXT")
CONFIRM_UPDATE_TEXT = _("CONFIRM_UPDATE_TEXT")
COPIED_TEXT = _("COPIED_TEXT")
COPY_ALL_TEXT_TEXT = _("COPY_ALL_TEXT_TEXT")
DEFINED_PARAMETERS_DELETED_TEXT = _("DEFINED_PARAMETERS_DELETED_TEXT")
DELETE_PARAMETERS_TEXT = _("DELETE_PARAMETERS_TEXT")
DELETE_USER_SAVED_SETTING_TEXT = _("DELETE_USER_SAVED_SETTING_TEXT")
DEMUCS_TEXT = "Demucs"
DENOISE_OUTPUT_TEXT = _("DENOISE_OUTPUT_TEXT")
DEVERB_VOCALS_TEXT = _("DEVERB_VOCALS_TEXT")
DONE_TEXT = _("DONE_TEXT")
DOWNLOAD_CENTER_TEXT = _("DOWNLOAD_CENTER_TEXT")
DOWNLOAD_CODE_TEXT = _("DOWNLOAD_CODE_TEXT")
DOWNLOAD_LINKS_TEXT = _("DOWNLOAD_LINKS_TEXT")
DOWNLOAD_UPDATE_IN_APPLICATION_TEXT = _("DOWNLOAD_UPDATE_IN_APPLICATION_TEXT")
ENABLE_HELP_HINTS_TEXT = _("ENABLE_HELP_HINTS_TEXT")
ENABLE_TTA_TEXT = _("ENABLE_TTA_TEXT")
ENABLE_VOCAL_SPLIT_MODE_TEXT = _("ENABLE_VOCAL_SPLIT_MODE_TEXT")
ENSEMBLE_NAME_TEXT = _("ENSEMBLE_NAME_TEXT")
ENSEMBLE_WAVFORMS_TEXT = _("ENSEMBLE_WAVFORMS_TEXT")
ERROR_CONSOLE_TEXT = _("ERROR_CONSOLE_TEXT")
GENERAL_MENU_TEXT = _("GENERAL_MENU_TEXT")
GENERAL_PROCESS_SETTINGS_TEXT = _("GENERAL_PROCESS_SETTINGS_TEXT")
GENERATE_MODEL_FOLDER_TEXT = _("GENERATE_MODEL_FOLDER_TEXT")
HIGHEND_PROCESS_TEXT = _("HIGHEND_PROCESS_TEXT")
INPUT_CODE_TEXT = _("INPUT_CODE_TEXT")
INPUT_STEM_NAME_TEXT = _("INPUT_STEM_NAME_TEXT")
INPUT_UNIQUE_STEM_NAME_TEXT = _("INPUT_UNIQUE_STEM_NAME_TEXT")
IS_INVERSE_STEM_TEXT = _("IS_INVERSE_STEM_TEXT")
KARAOKE_MODEL_TEXT = _("KARAOKE_MODEL_TEXT")
MANUAL_DOWNLOADS_TEXT = _("MANUAL_DOWNLOADS_TEXT")
MATCH_FREQ_CUTOFF_TEXT = _("MATCH_FREQ_CUTOFF_TEXT")
MDXNET_C_MODEL_PARAMETERS_TEXT = _("MDXNET_C_MODEL_PARAMETERS_TEXT")
MDXNET_MODEL_SETTINGS_TEXT = _("MDXNET_MODEL_SETTINGS_TEXT")
MDXNET_TEXT = "MDX-Net"
MODEL_PARAMETERS_CHANGED_TEXT = _("MODEL_PARAMETERS_CHANGED_TEXT")
MODEL_SAMPLE_MODE_SETTINGS_TEXT = _("MODEL_SAMPLE_MODE_SETTINGS_TEXT")
MODEL_TEST_MODE_TEXT = _("MODEL_TEST_MODE_TEXT")
MP3_BITRATE_TEXT = _("MP3_BITRATE_TEXT")
NAME_SETTINGS_TEXT = _("NAME_SETTINGS_TEXT")
NO_DEFINED_PARAMETERS_FOUND_TEXT = _("NO_DEFINED_PARAMETERS_FOUND_TEXT")
NO_TEXT = _("NO_TEXT")
NORMALIZE_OUTPUT_TEXT = _("NORMALIZE_OUTPUT_TEXT")
USE_OPENCL_TEXT = _("USE_OPENCL_TEXT")
NOT_ENOUGH_MODELS_TEXT = _("NOT_ENOUGH_MODELS_TEXT")
NOTIFICATION_CHIMES_TEXT = _("NOTIFICATION_CHIMES_TEXT")
OPEN_APPLICATION_DIRECTORY_TEXT = _("OPEN_APPLICATION_DIRECTORY_TEXT")
OPEN_LINK_TO_MODEL_TEXT = _("OPEN_LINK_TO_MODEL_TEXT")
OPEN_MODEL_DIRECTORY_TEXT = _("OPEN_MODEL_DIRECTORY_TEXT")
OPEN_MODEL_FOLDER_TEXT = _("OPEN_MODEL_FOLDER_TEXT")
OPEN_MODELS_FOLDER_TEXT = _("OPEN_MODELS_FOLDER_TEXT")
PHASE_SHIFTS_TEXT = _("PHASE_SHIFTS_TEXT")
POST_PROCESS_TEXT = _("POST_PROCESS_TEXT")
POST_PROCESS_THRESHOLD_TEXT = _("POST_PROCESS_THRESHOLD_TEXT")
PREPROCESS_MODEL_CHOOSE_TEXT = _("PREPROCESS_MODEL_CHOOSE_TEXT")
PRIMARY_STEM_TEXT = _("PRIMARY_STEM_TEXT")
REFRESH_LIST_TEXT = _("REFRESH_LIST_TEXT")
REMOVE_SAVED_ENSEMBLE_TEXT = _("REMOVE_SAVED_ENSEMBLE_TEXT")
REPORT_ISSUE_TEXT = _("REPORT_ISSUE_TEXT")
RESET_ALL_SETTINGS_TO_DEFAULT_TEXT = _("RESET_ALL_SETTINGS_TO_DEFAULT_TEXT")
RESTART_APPLICATION_TEXT = _("RESTART_APPLICATION_TEXT")
SAMPLE_CLIP_DURATION_TEXT = _("SAMPLE_CLIP_DURATION_TEXT")
SAVE_ALIGNED_TRACK_TEXT = _("SAVE_ALIGNED_TRACK_TEXT")
SAVE_ALL_OUTPUTS_TEXT = _("SAVE_ALL_OUTPUTS_TEXT")
SAVE_CURRENT_ENSEMBLE_TEXT = _("SAVE_CURRENT_ENSEMBLE_TEXT")
SAVE_CURRENT_SETTINGS_TEXT = _("SAVE_CURRENT_SETTINGS_TEXT")
SAVE_INSTRUMENTAL_MIXTURE_TEXT = _("SAVE_INSTRUMENTAL_MIXTURE_TEXT")
SAVE_SPLIT_VOCAL_INSTRUMENTALS_TEXT = _("SAVE_SPLIT_VOCAL_INSTRUMENTALS_TEXT")
SECONDARY_MODEL_TEXT = _("SECONDARY_MODEL_TEXT")
SECONDARY_PHASE_TEXT = _("SECONDARY_PHASE_TEXT")
SECONDS_TEXT = _("SECONDS_TEXT")
SEGMENT_DEFAULT_TEXT = _("SEGMENT_DEFAULT_TEXT")
SEGMENT_SIZE_TEXT = _("SEGMENT_SIZE_TEXT")
SEGMENTS_TEXT = _("SEGMENTS_TEXT")
SELECT_DOWNLOAD_TEXT = _("SELECT_DOWNLOAD_TEXT")
SELECT_MODEL_PARAM_TEXT = _("SELECT_MODEL_PARAM_TEXT")
SELECT_VOCAL_TYPE_TO_DEVERB_TEXT = _("SELECT_VOCAL_TYPE_TO_DEVERB_TEXT")
SELECTED_MODEL_PLACEMENT_PATH_TEXT = _("SELECTED_MODEL_PLACEMENT_PATH_TEXT")
SETTINGS_GUIDE_TEXT = _("SETTINGS_GUIDE_TEXT")
SETTINGS_TEST_MODE_TEXT = _("SETTINGS_TEST_MODE_TEXT")
SHIFT_CONVERSION_PITCH_TEXT = _("SHIFT_CONVERSION_PITCH_TEXT")
SHIFTS_TEXT = _("SHIFTS_TEXT")
SILENCE_MATCHING_TEXT = _("SILENCE_MATCHING_TEXT")
SPECIFY_MDX_NET_MODEL_PARAMETERS_TEXT = _("SPECIFY_MDX_NET_MODEL_PARAMETERS_TEXT")
SPECIFY_PARAMETERS_TEXT = _("SPECIFY_PARAMETERS_TEXT")
SPECIFY_VR_MODEL_PARAMETERS_TEXT = _("SPECIFY_VR_MODEL_PARAMETERS_TEXT")
SPECTRAL_INVERSION_TEXT = _("SPECTRAL_INVERSION_TEXT")
SPECTRAL_MATCHING_TEXT = _("SPECTRAL_MATCHING_TEXT")
SPLIT_MODE_TEXT = _("SPLIT_MODE_TEXT")
STEM_NAME_TEXT = _("STEM_NAME_TEXT")
STOP_DOWNLOAD_TEXT = _("STOP_DOWNLOAD_TEXT")
SUPPORT_UVR_TEXT = _("SUPPORT_UVR_TEXT")
TRY_MANUAL_DOWNLOAD_TEXT = _("TRY_MANUAL_DOWNLOAD_TEXT")
UPDATE_FOUND_TEXT = _("UPDATE_FOUND_TEXT")
USER_DOWNLOAD_CODES_TEXT = _("USER_DOWNLOAD_CODES_TEXT")
UVR_BUY_ME_A_COFFEE_LINK_TEXT = _("UVR_BUY_ME_A_COFFEE_LINK_TEXT")
UVR_ERROR_LOG_TEXT = _("UVR_ERROR_LOG_TEXT")
UVR_PATREON_LINK_TEXT = _("UVR_PATREON_LINK_TEXT")
VOCAL_DEVERB_OPTIONS_TEXT = _("VOCAL_DEVERB_OPTIONS_TEXT")
VOCAL_SPLIT_MODE_OPTIONS_TEXT = _("VOCAL_SPLIT_MODE_OPTIONS_TEXT")
VOCAL_SPLIT_OPTIONS_TEXT = _("VOCAL_SPLIT_OPTIONS_TEXT")
VOLUME_COMPENSATION_TEXT = _("VOLUME_COMPENSATION_TEXT")
VR_51_MODEL_TEXT = _("VR_51_MODEL_TEXT")
VR_ARCH_TEXT = _("VR_ARCH_TEXT")
WAV_TYPE_TEXT = _("WAV_TYPE_TEXT")
CUDA_NUM_TEXT = _("CUDA_NUM_TEXT")
WINDOW_SIZE_TEXT = _("WINDOW_SIZE_TEXT")
YES_TEXT = _("YES_TEXT")
VERIFY_INPUTS_TEXT = _("VERIFY_INPUTS_TEXT")
LANGUAGE_TEXT = _("LANGUAGE_TEXT")
AUDIO_INPUT_TOTAL_TEXT = _("AUDIO_INPUT_TOTAL_TEXT")
MDX23C_ONLY_OPTIONS_TEXT = _("MDX23C_ONLY_OPTIONS_TEXT")
PROCESS_STARTING_TEXT = _("PROCESS_STARTING_TEXT")
MISSING_MESS_TEXT = _("MISSING_MESS_TEXT")
SIMILAR_TEXT = _("SIMILAR_TEXT")
LOADING_VERSION_INFO_TEXT = _("LOADING_VERSION_INFO_TEXT")
CHECK_FOR_UPDATES_TEXT = _("CHECK_FOR_UPDATES_TEXT")
INFO_UNAVAILABLE_TEXT = _("INFO_UNAVAILABLE_TEXT")
UPDATE_CONFIRMATION_TEXT = _("UPDATE_CONFIRMATION_TEXT")
BROKEN_OR_INCOM_TEXT = _("BROKEN_OR_INCOM_TEXT")
BMAC_UVR_TEXT = _("BMAC_UVR_TEXT")
MDX_MENU_WAR_TEXT = _("MDX_MENU_WAR_TEXT")
NO_FILES_TEXT = _("NO_FILES_TEXT")
CHOOSE_INPUT_TEXT = _("CHOOSE_INPUT_TEXT")
OPEN_INPUT_DIR_TEXT = _("OPEN_INPUT_DIR_TEXT")
BATCH_PROCESS_MENU_TEXT = _("BATCH_PROCESS_MENU_TEXT")
TEMP_FILE_DELETION_TEXT = _("TEMP_FILE_DELETION_TEXT")
VOCAL_SPLITTER_OPTIONS_TEXT = _("VOCAL_SPLITTER_OPTIONS_TEXT")
WAVEFORM_ENSEMBLE_TEXT = _("WAVEFORM_ENSEMBLE_TEXT")
SELECT_INPUT_TEXT = _("SELECT_INPUT_TEXT")
SELECT_OUTPUT_TEXT = _("SELECT_OUTPUT_TEXT")
TIME_CORRECTION_TEXT = _("TIME_CORRECTION_TEXT")
UVR_LIS_INFO_TEXT = _("UVR_LIS_INFO_TEXT")
ADDITIONAL_RES_CREDITS_TEXT = _("ADDITIONAL_RES_CREDITS_TEXT")
SAVE_INST_MIXTURE_TEXT = _("SAVE_INST_MIXTURE_TEXT")
DOWNLOAD_UPDATE_IN_APP_TEXT = _("DOWNLOAD_UPDATE_IN_APP_TEXT")
WAVE_TYPE_TEXT = _("WAVE_TYPE_TEXT")
OPEN_LINK_TO_MODEL_TEXT = _("OPEN_LINK_TO_MODEL_TEXT")
OPEN_MODEL_DIRECTORY = _("OPEN_MODEL_DIRECTORY")
SELECTED_MODEL_PLACE_PATH_TEXT = _("SELECTED_MODEL_PLACE_PATH_TEXT")
IS_INVERSE_STEM_TEXT = _("IS_INVERSE_STEM_TEXT")
INPUT_STEM_NAME_TEXT = _("INPUT_STEM_NAME_TEXT")
INPUT_UNIQUE_STEM_NAME_TEXT = _("INPUT_UNIQUE_STEM_NAME_TEXT")
DONE_MENU_TEXT = _("DONE_MENU_TEXT")
OK_TEXT = _("OK_TEXT")
ENSEMBLE_WARNING_NOT_ENOUGH_SHORT_TEXT = _("ENSEMBLE_WARNING_NOT_ENOUGH_SHORT_TEXT")
ENSEMBLE_WARNING_NOT_ENOUGH_TEXT = _("ENSEMBLE_WARNING_NOT_ENOUGH_TEXT")
NOT_ENOUGH_ERROR_TEXT = _("NOT_ENOUGH_ERROR_TEXT")
INVALID_FOLDER_ERROR_TEXT = _("INVALID_FOLDER_ERROR_TEXT"), "您指定的导出路径不是有效的文件夹！"

GET_DL_VIP_CODE_TEXT = (
    "请访问以下链接之一获取代码。\n您可以捐赠、订阅或直接获取代码！\n（无需捐赠即可获取 VIP 代码）"
)
CONFIRM_RESTART_TEXT = (
    _("CONFIRM_RESTART_TEXT"),
    "这将重启应用并停止所有正在运行的进程。当前设置将被保存。\n\n确定要继续吗？",
)
ERROR_LOADING_FILE_TEXT = _("ERROR_LOADING_FILE_TEXT"), "原始错误详情"
LOADING_MODEL_TEXT = _("LOADING_MODEL_TEXT")
FULL_APP_SET_TEXT = _("FULL_APP_SET_TEXT")
PROCESS_STARTING_TEXT = _("PROCESS_STARTING_TEXT")
PROCESS_STOPPED_BY_USER = "\n\n进程已被用户停止。"
NEW_UPDATE_FOUND_TEXT = lambda version: (
    f"\n\n发现新更新：{version}\n\n点击「设置」菜单中的更新按钮进行下载和安装！"
)
ROLL_BACK_TEXT = _("ROLL_BACK_TEXT")


def secondary_stem(stem: str):
    """Determines secondary stem"""

    stem = stem if stem else NO_STEM
    secondary_stem = stem

    if stem in STEM_PAIR_MAPPER.keys():
        for key, value in STEM_PAIR_MAPPER.items():
            if stem in key:
                secondary_stem = value
    else:
        secondary_stem = stem.replace(NO_STEM, "") if NO_STEM in stem else f"{NO_STEM}{stem}"

    return secondary_stem


# ─── i18n: 根据配置文件初始化语言 ───
_LANG_FILE = Path(__file__).parent.parent / "uvr_config.json"
try:
    with open(_LANG_FILE, "r") as _f:
        _cfg = json.load(_f)
    _lang = _cfg.get("language", "zh")
except (FileNotFoundError, json.JSONDecodeError, KeyError):
    _lang = "zh"
from gui_data.l10n import set_language as _set_language

_set_language(_lang)
