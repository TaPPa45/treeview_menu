from typing import Set, Dict, List, Optional
from .interfaces import IMenuLoader, IMenuBuilder, IActiveResolver
from .loaders import MenuLoader
from .builders import TreeMenuBuilder
from .resolvers import DynamicURLResolver


class MenuService:
    def __init__(
        self,
        loader: IMenuLoader = MenuLoader(),
        builder: IMenuBuilder = TreeMenuBuilder(),
        resolver: IActiveResolver = DynamicURLResolver(),
    ):
        self.loader = loader
        self.builder = builder
        self.resolver = resolver

    def get_menu_context(self, menu_name: str, current_path: str) -> Dict:
        items = self.loader.load(menu_name)
        active_item = self.resolver.resolve_active(items, current_path)
        for item in items:
            item["is_active"] = active_item and item["id"] == active_item["id"]
        expanded_ids = self._get_expanded_ids(items, active_item)

        return {
            "menu_tree": self._build_hierarchy(
                self.builder.build_tree(items), expanded_ids=expanded_ids
            ),
            "active_item": active_item,
        }

    def _get_expanded_ids(self, items: List[Dict], active_item: Dict) -> Set[int]:
        expanded = set()
        if active_item:
            current = active_item
            while current:
                expanded.add(current["id"])
                current = next(
                    (i for i in items if i["id"] == current.get("parent_id")), None
                )
        return expanded

    def _build_hierarchy(
        self,
        tree: Dict[int, List[Dict]],
        parent_id: int = None,
        expanded_ids: Set[int] = None,
    ) -> List[Dict]:
        return sorted(
            [
                {
                    "item": item,
                    "children": (
                        self._build_hierarchy(tree, item["id"], expanded_ids)
                        if item["id"] in expanded_ids
                        else []
                    ),
                    "is_expanded": item["id"] in expanded_ids,
                    "is_active": item.get("is_active", False),
                }
                for item in tree.get(parent_id, [])
            ],
            key=lambda x: x["item"]["order"],
        )
