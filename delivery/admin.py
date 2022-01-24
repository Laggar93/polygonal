from django.contrib import admin
from delivery.models import delivery_main, delivery_article, delivery_columns
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from modeltranslation.admin import TranslationAdmin, TranslationStackedInline

class delivery_columns_admin(SortableInlineAdminMixin, admin.StackedInline):
    model = delivery_columns
    extra = 0
    ordering = ('order',)

class delivery_article_admin(SortableAdminMixin, TranslationAdmin):
    model = delivery_article
    extra = 0
    inlines = [delivery_columns_admin]
    ordering = ('order',)


class delivery_main_admin(TranslationAdmin):
    list_display = ('name', )
    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(delivery_main, delivery_main_admin)
admin.site.register(delivery_article, delivery_article_admin)