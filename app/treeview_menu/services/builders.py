from collections import defaultdict
from .interfaces import IMenuBuilder
from typing import List, Dict


class TreeMenuBuilder(IMenuBuilder):
    def build_tree(self, items: List[Dict]) -> Dict[int, List[Dict]]:
        tree = defaultdict(list)
        for item in items:
            tree[item['parent_id']].append(item)
        return tree