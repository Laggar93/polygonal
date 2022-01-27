from modeltranslation.translator import translator, TranslationOptions
from .models import index_main, order_point


class IndexTranslationOptions(TranslationOptions):
    fields = ('keywords', 'description', 'title', 'title_page', 'title_text', 'first_figure_button_name',
              'second_figure_button_name', 'figure_title', 'figure_text', 'proud_title', 'proud_text',
              'title_link', 'third_figure_button_name', 'fourth_figure_button_name')

class PointTranslationOptions(TranslationOptions):
    fields = ('point',)

translator.register(index_main, IndexTranslationOptions)
translator.register(order_point, PointTranslationOptions)
