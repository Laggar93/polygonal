from django.contrib import admin
from order_projects.models import project_page, project_list, project_images
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from modeltranslation.admin import TranslationAdmin, TranslationStackedInline

class project_images_admin(SortableInlineAdminMixin, admin.StackedInline):
    model = project_images
    extra = 0
    ordering = ('order',)


class project_list_admin(SortableAdminMixin, TranslationAdmin):
    model = project_list
    extra = 0
    inlines = [project_images_admin]
    ordering = ('order',)


class project_page_admin(TranslationAdmin):
    list_display = ('name', )
    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(project_page, project_page_admin)
admin.site.register(project_list, project_list_admin)