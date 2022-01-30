from django.contrib import admin
from .models import index_main, order_point, index_translate
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from modeltranslation.admin import TranslationAdmin, TranslationStackedInline


class index_translate_admin(TranslationAdmin):
    model = index_translate
    extra = 0

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

class order_point_admin(SortableInlineAdminMixin, TranslationStackedInline):
    model = order_point
    extra = 0
    exclude = ('promo_photo_md', 'promo_photo_xs', 'promo_photo_xs2x')


class index_main_admin(TranslationAdmin):
    model = index_main
    inlines = [order_point_admin,]
    exclude = ('main_photo_xl', 'main_photo_md', 'main_photo_md2x', 'main_photo_sm', 'main_photo_sm2x',
               'main_photo_xs', 'main_photo_xs2x', 'first_figure_sticker_xs', 'second_figure_sticker_xs',
               'third_figure_sticker_xs', 'fourth_figure_sticker_xs', 'proud_picture_xs')

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(index_main, index_main_admin)
# admin.site.register(order_point, order_point_admin)
admin.site.register(index_translate, index_translate_admin)
