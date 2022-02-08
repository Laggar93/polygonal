import random
import string

from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from django.contrib import admin
from django.contrib.auth.models import User, Group
from modeltranslation.admin import TranslationAdmin, TranslationStackedInline

from .models import category, subcategory, item, item_photos, item_terms, \
    item_files, discount, coupon, shop_page


@admin.action(description='Скопировать выбранные Купоны')
def dublicate(modeladmin, request, queryset):
    for object in queryset:
        object.id = None
        object.number = ''.join(
            random.choice(string.ascii_uppercase + string.digits) for _ in
            range(10))
        object.save()


def dublicate_ad(modeladmin, request, queryset):
    for ad in queryset:
        ad.pk = None
        ad.slug = ''.join(
            random.choice(string.ascii_uppercase + string.digits) for _ in
            range(30))
        ad.save()


dublicate_ad.short_description = "Дублировать выбранный товар "


class discount_admin(TranslationAdmin):
    list_display = ('name', 'items')

    def items(self, request, obj=None):
        output = []
        for item in request.item.all():
            output.append(item)
        return output

    items.short_description = 'Товары'
    save_as = True
    save_on_top = True


class coupon_admin(TranslationAdmin):
    readonly_fields = ('number', 'used')
    save_as = True
    save_on_top = True
    actions = [dublicate]


class item_files_admin(SortableInlineAdminMixin, TranslationStackedInline):
    model = item_files
    extra = 1


class item_terms_admin(SortableInlineAdminMixin, TranslationStackedInline):
    model = item_terms
    extra = 1


class item_photos_admin(SortableInlineAdminMixin, TranslationStackedInline):
    model = item_photos
    extra = 1
    exclude = ('image_800',)
    readonly_fields = ('display_image',)
    exclude = (
        'main_photo_popup', 'main_photo_xs2', 'main_photo_xxl', 'main_photo_xs', 'main_photo_thumb_xs2', 'main_photo_thumb_xs')


class subcategory_admin(SortableAdminMixin, TranslationAdmin):
    save_as = True
    save_on_top = True


class category_admin(SortableAdminMixin, TranslationAdmin):
    exclude = ('index_photo_xs', 'index_photo_lg', 'index_photo_lg2x', 'index_photo_sm', 'index_photo_sm2x')
    save_as = True
    save_on_top = True


class item_admin(SortableAdminMixin, TranslationAdmin):
    search_fields = ['name_lower']

    def get_search_results(self, request, queryset, search_term):
        return super(item_admin, self).get_search_results(request, queryset, search_term.lower())


    list_display = ('name', 'category', 'is_active', 'difficulty', 'views')
    inlines = [item_photos_admin, item_terms_admin, item_files_admin]
    readonly_fields = ('display_main_image', 'display_bottom_image')
    exclude = (
        'main_photo_popup', 'main_photo_xs2', 'main_photo_xxl', 'main_photo_xs',
        'bottom_photo_xs2', 'bottom_photo_xxl', 'bottom_photo_xs', 'main_photo_thumb_xs2', 'main_photo_thumb_xs', 'name_lower')
    save_on_top = True
    save_as = True
    ordering = ('order',)
    actions = [dublicate_ad]

    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)
        fields = fields[-1:] + fields[:-1]
        return fields


class shop_page_admin(TranslationAdmin):
    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(shop_page, shop_page_admin)
admin.site.register(item, item_admin)
admin.site.register(category, category_admin)

admin.site.register(subcategory, subcategory_admin)
admin.site.register(discount, discount_admin)
admin.site.register(coupon, coupon_admin)
admin.site.unregister([User, Group])
admin.site.register(item_terms)
