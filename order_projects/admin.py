from django.contrib import admin
from order_projects.models import project_page, project_list, project_images
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from modeltranslation.admin import TranslationAdmin, TranslationStackedInline

class project_list_admin(SortableInlineAdminMixin, admin.StackedInline):
    model = project_list
    extra = 0


class project_images_admin(SortableInlineAdminMixin, admin.StackedInline):
    model = project_images
    extra = 0


class project_page_admin(SortableAdminMixin, TranslationAdmin):
    model = project_page
    inlines = (project_list_admin, project_images_admin)
    list_display = ('name', )



admin.site.register(project_page)
admin.site.register(project_list)
admin.site.register(project_images)