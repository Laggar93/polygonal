from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminMixin
from django.contrib import admin
from contact.models import contact_main, contact_social_networks, contact_form
from modeltranslation.admin import TranslationAdmin, TranslationStackedInline



class contact_social_networks_admin(SortableInlineAdminMixin, TranslationStackedInline):
    model = contact_social_networks
    ordering = ('order',)


class contact_main_admin(TranslationAdmin):
    list_display = ('address', )
    exclude = ('main_photo_xl', 'main_photo_md', 'main_photo_md2x', 'main_photo_sm', 'main_photo_sm2x',
               'main_photo_xs', 'main_photo_xs2x', 'main_photo_xl1', 'main_photo_xl12x')
    inlines = [contact_social_networks_admin,]

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

class contact_form_admin(TranslationAdmin):
    model = contact_form
    # exclude = ('heading', 'send', 'success', 'error',)
    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(contact_main, contact_main_admin)
admin.site.register(contact_form, contact_form_admin)
