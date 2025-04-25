from django.urls import resolve, Resolver404, reverse, NoReverseMatch

from .interfaces import IActiveResolver
from typing import List, Dict, Optional


class DynamicURLResolver(IActiveResolver):
    def resolve_active(self, items: List[Dict], current_path: str) -> Optional[Dict]:
        try:
            resolved = resolve(current_path)
            return next(
                (
                    item
                    for item in items
                    if self._is_active(
                        item, resolved.url_name, resolved.kwargs, current_path
                    )
                ),
                None,
            )
        except Resolver404:
            return None

    def _is_active(self, item: Dict, url_name: str, kwargs: Dict, path: str) -> bool:
        return any(
            [
                item.get("url") == path,
                item.get("named_url") == url_name
                and self._check_url_params(item.get("get_url"), kwargs),
            ]
        )

    def _check_url_params(self, url: str, kwargs: Dict) -> bool:
        try:
            return url == reverse(resolve(url).view_name, kwargs=kwargs)
        except:
            return False
