from django.contrib import admin
# Register your models here.
from modeltranslation.admin import TranslationAdmin
from about.models import about_main


class about_main_admin(TranslationAdmin):
    model = about_main

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(about_main, about_main_admin)