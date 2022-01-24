from modeltranslation.translator import translator, TranslationOptions
from .models import map_main

class MapMainTranslationOptions(TranslationOptions):
    fields = ('is_active',)



translator.register(map_main, MapMainTranslationOptions)