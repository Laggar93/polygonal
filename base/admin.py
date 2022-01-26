from django.contrib import admin
from base.models import footer_elements, rules, offer, policy


class footer_elements_admin(admin.ModelAdmin):
    model = footer_elements
    extra = 0

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class rules_admin(admin.ModelAdmin):
    model = rules
    extra = 0

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class offer_admin(admin.ModelAdmin):
    model = offer
    extra = 0

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class policy_admin(admin.ModelAdmin):
    model = policy
    extra = 0

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(footer_elements, footer_elements_admin)
admin.site.register(rules, rules_admin)
admin.site.register(offer, offer_admin)
admin.site.register(policy, policy_admin)
