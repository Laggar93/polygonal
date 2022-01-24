from django.contrib import admin
# Register your models here.
from modeltranslation.admin import TranslationAdmin
from map.models import map_main


class map_main_admin(TranslationAdmin):
    model = map_main

    # def has_add_permission(self, request, obj=None):
    #     return False
    #
    # def has_delete_permission(self, request, obj=None):
    #     return False

admin.site.register(map_main, map_main_admin)