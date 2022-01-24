from modeltranslation.translator import translator, TranslationOptions
from .models import about_main

class AboutMainTranslationOptions(TranslationOptions):
    fields = ('name',)


translator.register(about_main, AboutMainTranslationOptions)