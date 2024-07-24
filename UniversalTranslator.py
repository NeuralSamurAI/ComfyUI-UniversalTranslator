# node.py

import torch
from deep_translator import (GoogleTranslator, MyMemoryTranslator, 
                             LingueeTranslator, PonsTranslator)

LANGUAGES = GoogleTranslator().get_supported_languages(as_dict=True)

class TranslationNode:
    @classmethod
    def INPUT_TYPES(cls):
        language_list = sorted(LANGUAGES.keys())
        return {
            "required": {
                "text": ("STRING", {"multiline": True}),
                "source_lang": (["auto"] + language_list,),
                "target_lang": (language_list,),
                "translation_service": ([
                    "Google Translate"
                ],),
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "translate_text"
    CATEGORY = "text"

    def __init__(self):
        self.translation_services = {
            "Google Translate": self.google_translate,
            "MyMemory": self.mymemory_translate,
            "Linguee": self.linguee_translate,
            "Pons": self.pons_translate
        }

    def translate_text(self, text, source_lang, target_lang, translation_service):
        try:
            translated = self.translation_services[translation_service](text, source_lang, target_lang)
            return (translated,)
        except Exception as e:
            print(f"Translation error: {str(e)}")
            return (f"Error: {str(e)}",)

    def google_translate(self, text, source_lang, target_lang):
        translator = GoogleTranslator(source=source_lang, target=target_lang)
        return translator.translate(text)

    def mymemory_translate(self, text, source_lang, target_lang):
        translator = MyMemoryTranslator(source=source_lang, target=target_lang)
        return translator.translate(text)

    def linguee_translate(self, text, source_lang, target_lang):
        translator = LingueeTranslator(source=source_lang, target=target_lang)
        return translator.translate(text)

    def pons_translate(self, text, source_lang, target_lang):
        translator = PonsTranslator(source=source_lang, target=target_lang)
        return translator.translate(text)