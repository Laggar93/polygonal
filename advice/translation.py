from modeltranslation.translator import translator, TranslationOptions
from .models import advice_page, advice_blocks, advice_main

class AdviceMainTranslationOptions(TranslationOptions):
    fields = ('keywords', 'description', 'title', 'name')

class AdvicePageTranslationOptions(TranslationOptions):
    fields = ('keywords', 'description', 'title', 'name', 'intro_text')

class AdviceBlocksTranslationOptions(TranslationOptions):
    fields = ('keywords', 'description', 'title', 'name', 'text', 'title_paragraph1', 'title_paragraph2', 'title_paragraph3',
              'title_paragraph4','title_paragraph5', 'text_paragraph1', 'text_paragraph2', 'text_paragraph3',
              'text_paragraph4','text_paragraph5')


translator.register(advice_main, AdviceMainTranslationOptions)
translator.register(advice_page, AdvicePageTranslationOptions)
translator.register(advice_blocks, AdviceBlocksTranslationOptions)