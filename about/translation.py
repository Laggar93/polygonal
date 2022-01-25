from modeltranslation.translator import translator, TranslationOptions
from .models import about_main, about_reward, about_press, about_author


class AboutMainTranslationOptions(TranslationOptions):
    fields = ('keywords', 'description', 'title', 'name', 'title_page', 'bottom_text', 'grey_text_photo',
              'bottom_text_photo', 'number_text', 'title_reward', 'title_create_model', 'title_press', 'title_author')


class AboutRewardTranslationOptions(TranslationOptions):
    fields = ('title', 'text',)


class AboutPressTranslationOptions(TranslationOptions):
    fields = ('published', 'title',)


class AboutAuthorTranslationOptions(TranslationOptions):
    fields = ('full_name', 'position', 'text',)



translator.register(about_main, AboutMainTranslationOptions)
translator.register(about_reward, AboutRewardTranslationOptions)
translator.register(about_press, AboutPressTranslationOptions)
translator.register(about_author, AboutAuthorTranslationOptions)