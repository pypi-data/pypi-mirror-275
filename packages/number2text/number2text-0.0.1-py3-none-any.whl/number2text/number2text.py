# number2text.py

import importlib
import os

class NumberToText:
    def __init__(self, language='en'):
        self.language = language
        self.lang_module = self._import_lang_module()

    def _import_lang_module(self):
        try:
            return importlib.import_module(f"number2text.lang.{self.language}")
        except ImportError:
            raise ValueError(f"Unsupported language: {self.language}")

    def convert(self, number):
        return self.lang_module.convert(number)

    @staticmethod
    def supported_languages():
        lang_dir = os.path.join(os.path.dirname(__file__), 'lang')
        lang_files = [f[:-3] for f in os.listdir(lang_dir) if f.endswith('.py') and f != '__init__.py']
        return sorted(lang_files)
