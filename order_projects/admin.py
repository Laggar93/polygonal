from django.contrib import admin
from order_projects.models import project_page, project_list, project_images
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from modeltranslation.admin import TranslationAdmin, TranslationStackedInline

class project_images_admin(SortableInlineAdminMixin, TranslationStackedInline):
    model = project_images
    extra = 0
    ordering = ('order',)
    readonly_fields = ('display_image',)


class project_list_admin(SortableAdminMixin, TranslationAdmin):
    model = project_list
    extra = 0
    inlines = [project_images_admin]
    ordering = ('order',)
    exclude = ('main_photo_sm', 'main_photo_original', 'main_photo_xs', 'main_photo_xs2x')
    readonly_fields = ('display_image',)


class project_page_admin(TranslationAdmin):
    list_display = ('name', )
    exclude = ('promo_photo_md', 'promo_photo_xs', 'promo_photo_xs2x')

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(project_page, project_page_admin)
admin.site.register(project_list, project_list_admin)