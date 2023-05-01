# from django.core.cache import cache

# class TranslationCache:
#     def get_key(self, text, source_lang, target_lang):
#         return f'{text}-{source_lang}-{target_lang}'

#     def get_translation(self, text, source_lang, target_lang):
#         key = self.get_key(text, source_lang, target_lang)
#         return cache.get(key)

#     def add_translation(self, text, source_lang, target_lang, translation):
#         key = self.get_key(text, source_lang, target_lang)
#         cache.set(key, translation)

from django.core.cache import cache


class TranslationCache:
    def __init__(self):
        self.namespace = 'translation'

    def get_cache_key(self, text, source_lang, target_lang):
        key = f"{source_lang}-{target_lang}-{text}"
        return key

    def get_translation(self, text, source_lang, target_lang):
        key = self.get_cache_key(text, source_lang, target_lang)
        return cache.get(f"{self.namespace}:{key}")

    def add_translation(self, text, source_lang, target_lang, translation):
        key = self.get_cache_key(text, source_lang, target_lang)
        cache.set(f"{self.namespace}:{key}", translation, 24 * 60 * 60)
