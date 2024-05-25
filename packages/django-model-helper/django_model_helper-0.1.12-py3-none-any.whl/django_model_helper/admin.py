from django.contrib import admin
from django.contrib.auth import get_permission_codename

__all__ = [
    "WithDeletedStatusFieldsAdmin",
    "WithEnabledStatusFieldsAdmin",
    "WithVisibleFieldsFieldsAdmin",
    "WithHotspotFieldsAdmin",
]


class WithDeletedStatusFieldsAdmin(admin.ModelAdmin):

    def has_set_deleted_permission(self, request):
        opts = self.opts
        codename = get_permission_codename("set_deleted", opts)
        result = request.user.has_perm("%s.%s" % (opts.app_label, codename))
        return result

    def has_set_undeleted_permission(self, request):
        opts = self.opts
        codename = get_permission_codename("set_undeleted", opts)
        result = request.user.has_perm("%s.%s" % (opts.app_label, codename))
        return result


class WithEnabledStatusFieldsAdmin(admin.ModelAdmin):

    def has_set_enabled_permission(self, request):
        opts = self.opts
        codename = get_permission_codename("set_enabled", opts)
        result = request.user.has_perm("%s.%s" % (opts.app_label, codename))
        return result

    def has_set_disabled_permission(self, request):
        opts = self.opts
        codename = get_permission_codename("set_disabled", opts)
        result = request.user.has_perm("%s.%s" % (opts.app_label, codename))
        return result


class WithVisibleFieldsFieldsAdmin(admin.ModelAdmin):

    def has_set_visible_permission(self, request):
        opts = self.opts
        codename = get_permission_codename("set_visible", opts)
        result = request.user.has_perm("%s.%s" % (opts.app_label, codename))
        return result

    def has_set_hidden_permission(self, request):
        opts = self.opts
        codename = get_permission_codename("set_hidden", opts)
        result = request.user.has_perm("%s.%s" % (opts.app_label, codename))
        return result


class WithHotspotFieldsAdmin(admin.ModelAdmin):

    def has_set_hotspot_permission(self, request):
        opts = self.opts
        codename = get_permission_codename("set_hotspot", opts)
        result = request.user.has_perm("%s.%s" % (opts.app_label, codename))
        return result

    def has_clean_hotspot_permission(self, request):
        opts = self.opts
        codename = get_permission_codename("clean_hotspot", opts)
        result = request.user.has_perm("%s.%s" % (opts.app_label, codename))
        return result
