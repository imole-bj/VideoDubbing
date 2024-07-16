from .logging_setup import logger

LANGUAGES = {
    "Automatic detection": "Automatic detection",
    "English (en)": "en",
    "French (fr)": "fr",
    "Fongbe (fon)": "fon",
    "Yoruba (yo)": "yo",
}

BASE_L_LIST = LANGUAGES.keys()
LANGUAGES_LIST = [list(BASE_L_LIST)[0]] + sorted(list(BASE_L_LIST)[1:])
INVERTED_LANGUAGES = {value: key for key, value in LANGUAGES.items()}

EXTRA_ALIGN = {
    "yo": "ogbi/wav2vec2-large-mms-1b-yoruba-test",
}


VITS_VOICES_LIST = {
    "en-facebook-mms VITS": "facebook/mms-tts-eng",
    "fr-facebook-mms VITS": "facebook/mms-tts-fra",
    "fon-facebook-mms VITS": "facebook/mms-tts-fon",
    "yo-facebook-mms VITS": "facebook/mms-tts-yor",
    }

LANGUAGE_CODE_IN_THREE_LETTERS = {
    "Automatic detection": "aut",
    "en": "eng",
    "fr": "fre",
    "fon": "fon",
    "yo": "yor",
}

def fix_code_language(translate_to, syntax="google"):
    if syntax == "google":
        # google-translator, gTTS
        replace_lang_code = {"zh": "zh-CN", "he": "iw", "zh-cn": "zh-CN"}
    elif syntax == "coqui":
        # coqui-xtts
        replace_lang_code = {"zh": "zh-cn", "zh-CN": "zh-cn", "zh-TW": "zh-cn"}

    new_code_lang = replace_lang_code.get(translate_to, translate_to)
    logger.debug(f"Fix code {translate_to} -> {new_code_lang}")
    return new_code_lang
