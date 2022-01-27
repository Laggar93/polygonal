from django.contrib import admin
from .models import index_main, order_point
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from modeltranslation.admin import TranslationAdmin, TranslationStackedInline




class order_point_admin(SortableInlineAdminMixin, TranslationStackedInline):
    model = order_point
    extra = 0


class index_main_admin(TranslationAdmin):
    model = index_main
    inlines = [order_point_admin,]
    exclude = ('main_photo_xl', 'main_photo_md', 'main_photo_md2x', 'main_photo_sm', 'main_photo_sm2x',
               'main_photo_xs', ' main_photo_xs2x')


admin.site.register(index_main, index_main_admin)
# admin.site.register(order_point, order_point_admin)
