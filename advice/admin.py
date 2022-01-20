from django.contrib import admin
from advice.models import advice_page, advice_main, advice_blocks
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from modeltranslation.admin import TranslationAdmin, TranslationStackedInline

class advice_blocks_admin(SortableInlineAdminMixin, TranslationStackedInline):
    model = advice_blocks
    extra = 0
    ordering = ('order',)
    readonly_fields = ('display_block_image',)
    # скопировать отсюда для оставшихся 7 изображений
    exclude = ('slide_picture_1_original', 'slide_picture_1_xxl', 'slide_picture_1_xs2x', 'slide_picture_1_xs')
    # до сюда


class advice_page_admin(SortableAdminMixin, TranslationAdmin):
    extra = 0
    inlines = [advice_blocks_admin]
    ordering = ('order',)
    exclude = ('main_photo_xxl', 'main_photo_xs', 'main_photo_xs2x')
    readonly_fields = ('display_page_image',)


class advice_main_admin(TranslationAdmin):
    list_display = ('name', )
    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(advice_main, advice_main_admin)
admin.site.register(advice_page, advice_page_admin)