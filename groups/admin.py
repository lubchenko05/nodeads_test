from django.contrib import admin
from .models import Group, Element


class ElementInline(admin.StackedInline):
    model = Element
    extra = 0
    verbose_name_plural = 'Element'
    fk_name = 'parent'


class CustomGroupAdmin(admin.ModelAdmin):
    inlines = (ElementInline,)
    list_display = (
        'parent',
        'icon',
        'name',
        'description',
        'get_child_group_count',
        'get_child_elements_count')


admin.site.register(Group, CustomGroupAdmin)
admin.site.register(Element)
