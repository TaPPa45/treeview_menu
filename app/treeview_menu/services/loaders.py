from .interfaces import IMenuLoader
from ..models import MenuItem
from typing import List, Dict
from django.urls import reverse, NoReverseMatch


class MenuLoader(IMenuLoader):
    def load(self, menu_name: str) -> List[Dict]:
        return [
            self._process_item(item)
            for item in MenuItem.objects.filter(menu__name=menu_name)
            .order_by("order")
            .values("id", "parent_id", "name", "url", "named_url", "order")
        ]

    def _process_item(self, item: Dict) -> Dict:
        item["get_url"] = self._get_item_url(item)
        return item

    def _get_item_url(self, item: Dict) -> str:
        if item["named_url"]:
            try:
                return reverse(item["named_url"])
            except NoReverseMatch:
                pass
        return item["url"] or "#"
