from django.apps import AppConfig


class TreeviewMenuConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "treeview_menu"

    def ready(self):
        import treeview_menu.signals
