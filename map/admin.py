from django.contrib import admin
# Register your models here.
from modeltranslation.admin import TranslationAdmin
from map.models import map_main, map_town, map_shop


class map_shop_admin(admin.ModelAdmin):
    model = map_shop
    search_fields = ['name', 'town',]
    list_display = ('name', 'town',)


class map_main_admin(TranslationAdmin):
    model = map_main

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(map_main, map_main_admin)
admin.site.register(map_shop, map_shop_admin)
admin.site.register(map_town)
