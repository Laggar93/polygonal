from django.contrib import admin
# Register your models here.
from modeltranslation.admin import TranslationAdmin
from map.models import map_main, map_town, map_shop


class map_shop_admin(admin.StackedInline):
    model = map_shop


class map_town_admin(admin.ModelAdmin):
    model = map_town
    inlines = [map_shop_admin,]



class map_main_admin(TranslationAdmin):
    model = map_main

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(map_main, map_main_admin)
# admin.site.register(map_shop, map_shop_admin)
admin.site.register(map_town, map_town_admin)
