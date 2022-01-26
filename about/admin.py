from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminMixin
from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationStackedInline
from about.models import about_main, about_reward, about_author, about_press


class about_reward_admin(SortableInlineAdminMixin, TranslationStackedInline):
    model = about_reward
    ordering = ('order',)
    extra = 0


class about_press_admin(SortableInlineAdminMixin, TranslationStackedInline):
    model = about_press
    exclude = ('main_logo_lg', 'main_logo_xs', 'main_logo_xs2x')
    ordering = ('order',)
    extra = 0


class about_author_admin(SortableInlineAdminMixin, TranslationStackedInline):
    model = about_author
    ordering = ('order',)
    extra = 0


class about_main_admin(TranslationAdmin):
    model = about_main
    inlines = [about_reward_admin, about_press_admin, about_author_admin]
    exclude = ('main_photo_xl', 'main_photo_md', 'main_photo_md2x', 'main_photo_sm',
               'main_photo_sm2x', 'main_photo_xs', 'main_photo_xs2x')

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(about_main, about_main_admin)