from modeltranslation.translator import translator, TranslationOptions
from .models import contact_main, contact_social_networks, contact_form

class ContactMainTranslationOptions(TranslationOptions):
    fields = ('keywords', 'description', 'title', 'name', 'intro_title', 'address', 'work_mode',)


class ContactSocialNetworkTranslationOptions(TranslationOptions):
    fields = ()


class ContactFormTranslationOptions(TranslationOptions):
    fields = ('heading', 'name', 'email', 'number', 'message', 'send', 'success', 'error')

translator.register(contact_main, ContactMainTranslationOptions)
translator.register(contact_social_networks, ContactSocialNetworkTranslationOptions)
translator.register(contact_form, ContactFormTranslationOptions)
