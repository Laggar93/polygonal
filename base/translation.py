from modeltranslation.translator import translator, TranslationOptions
from .models import footer_elements, rules, offer, policy

class FooterTranslationOptions(TranslationOptions):
    fields = ('with_love', )


class RulesTranslationOptions(TranslationOptions):
    fields = ('keywords', 'description', 'title', 'name', 'text', 'info')


class OfferTranslationOptions(TranslationOptions):
    fields = ('keywords', 'description', 'title', 'name', 'text', 'info')


class PolicyTranslationOptions(TranslationOptions):
    fields = ('keywords', 'description', 'title', 'name', 'info')

translator.register(footer_elements, FooterTranslationOptions)
translator.register(rules, RulesTranslationOptions)
translator.register(offer, OfferTranslationOptions)
translator.register(policy, PolicyTranslationOptions)
