"""
UVR i18n / L10n 轻量级国际化模块

支持从 JSON 语言包加载翻译，提供 _() 翻译函数。
语言选择保存在 uvr_config.json 中。
"""

import json
import os
from pathlib import Path
from typing import Dict, Optional

_LOCALE_DIR = Path(__file__).parent / "locales"
_DEFAULT_LANG = "zh"

_cache: Dict[str, str] = {}
_current_lang: Optional[str] = None
_fallback_cache: Dict[str, str] = {}


def _load_lang(lang: str) -> Dict[str, str]:
    """加载指定语言的翻译文件"""
    path = _LOCALE_DIR / f"{lang}.json"
    if not path.exists():
        path = _LOCALE_DIR / f"{_DEFAULT_LANG}.json"
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def set_language(lang: str) -> None:
    """切换语言"""
    global _cache, _current_lang
    _cache = _load_lang(lang)
    _current_lang = lang
    # 加载 fallback (默认语言)
    global _fallback_cache
    if lang != _DEFAULT_LANG:
        _fallback_cache = _load_lang(_DEFAULT_LANG)
    else:
        _fallback_cache = {}


def get_language() -> str:
    """获取当前语言代码"""
    return _current_lang or _DEFAULT_LANG


def _(key: str) -> str:
    """翻译函数 — 根据 key 返回当前语言的字符串"""
    # 优先当前语言
    if _cache:
        val = _cache.get(key)
        if val is not None:
            return val
    # 回退到默认语言
    if _fallback_cache:
        val = _fallback_cache.get(key)
        if val is not None:
            return val
    # 最后回退到 key 本身
    return key


def get_available_languages() -> list[dict[str, str]]:
    """获取可用的语言列表"""
    languages = []
    for fpath in sorted(_LOCALE_DIR.glob("*.json")):
        lang_code = fpath.stem
        try:
            with open(fpath, "r", encoding="utf-8") as f:
                meta = json.load(f)
            label = meta.get("_language_name", lang_code)
        except (json.JSONDecodeError, KeyError):
            label = lang_code
        languages.append({"code": lang_code, "label": label})
    return languages


# 启动时加载默认语言
set_language(_DEFAULT_LANG)
