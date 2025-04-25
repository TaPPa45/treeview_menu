from django import template
from ..services import MenuService
import logging

logger = logging.getLogger(__name__)
register = template.Library()

@register.inclusion_tag('menu.html', takes_context=True)
def draw_menu(context, menu_name: str):
    try:
        request = context["request"]
        service = MenuService()
        menu_data = service.get_menu_context(
            menu_name=menu_name,
            current_path=request.path
        )
        return {
            "menu_tree": menu_data["menu_tree"],
            "active_item": menu_data["active_item"]
        }
    except Exception as e:
        logger.error(f"Menu rendering failed: {str(e)}", exc_info=True)
        return {"menu_tree": [], "active_item": None}