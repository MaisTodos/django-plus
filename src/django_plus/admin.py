from django.utils.safestring import mark_safe


def admin_method_attributes(**outer_kwargs):
    def method_decorator(func):
        for kw, arg in outer_kwargs.items():
            setattr(func, kw, arg)
        return func
    return mark_safe(method_decorator)


class NoDeleteAdminMixin(object):
    can_delete = False  # only inlines

    def has_delete_permission(self, request, obj=None):
        return False  # pragma: no cover


class NoAddAdminMixin(object):
    extra = 0  # only inlines
    max_num = 0  # only inlines

    def has_add_permission(self, request, obj=None):
        return False  # pragma: no cover


class ReadOnlyAdminMixin(NoDeleteAdminMixin, NoAddAdminMixin):

    def has_change_permission(self, request, obj=None):
        return True