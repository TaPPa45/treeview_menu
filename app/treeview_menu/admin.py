from django.contrib import admin
from .models import Menu, MenuItem


class MenuItemInline(admin.StackedInline):
    model = MenuItem
    extra = 1
    fields = ("name", "parent", "url", "named_url", "order")
    autocomplete_fields = ("parent",)
    ordering = ("order",)


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ("name", "items_count")
    list_display_links = ("name",)
    inlines = [MenuItemInline]
    search_fields = ("name",)

    def items_count(self, obj):
        return obj.menuitem_set.count()

    items_count.short_description = "Количество пунктов"


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("indented_name", "menu", "parent", "order", "url", "named_url")
    list_display_links = ("indented_name",)
    list_filter = ("menu",)
    search_fields = ("name", "url", "named_url")
    ordering = ("menu", "parent__id", "order")
    autocomplete_fields = ("menu", "parent")
    fieldsets = (
        (None, {"fields": ("menu", "name", "parent", "order")}),
        ("URL", {"fields": ("url", "named_url")}),
    )

    def indented_name(self, obj):
        indent = ""
        current = obj.parent
        while current:
            indent += "— "
            current = current.parent
        return f"{indent}{obj.name}"

    indented_name.short_description = "Название"
