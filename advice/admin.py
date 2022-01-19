from django.contrib import admin
from advice.models import advice_page, advice_main, advice_blocks
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from modeltranslation.admin import TranslationAdmin, TranslationStackedInline

class advice_blocks_admin(SortableInlineAdminMixin, TranslationStackedInline):
    model = advice_blocks
    extra = 0
    ordering = ('order',)
    readonly_fields = ('display_block_image',)


class advice_page_admin(SortableAdminMixin, TranslationAdmin):
    model = advice_page
    extra = 0
    inlines = [advice_blocks_admin]
    ordering = ('order',)
    exclude = ('main_photo_xxl', 'main_photo_xxl2x', 'main_photo_xs', 'main_photo_xs2x')
    readonly_fields = ('display_page_image',)


class advice_main_admin(TranslationAdmin):
    list_display = ('name', )
    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(advice_main, advice_main_admin)
admin.site.register(advice_page, advice_page_admin)