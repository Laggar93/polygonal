from modeltranslation.translator import translator, TranslationOptions
from .models import delivery_main, delivery_article, delivery_columns

class DeliveryMainTranslationOptions(TranslationOptions):
    fields = ('keywords', 'description', 'title', 'delivery', 'name', 'payment', 'top_text', 'bottom_text')

class DeliveryArticleTranslationOptions(TranslationOptions):
    fields = ('title', 'intro_text', 'country', 'bold_text', 'grey_text')

class DeliveryColumnsTranslationOptions(TranslationOptions):
    fields = ('first_column', 'second_column', 'third_column')


translator.register(delivery_main, DeliveryMainTranslationOptions)
translator.register(delivery_article, DeliveryArticleTranslationOptions)
translator.register(delivery_columns, DeliveryColumnsTranslationOptions)