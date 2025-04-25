from abc import ABC, abstractmethod
from typing import List, Dict, Optional


class IMenuLoader(ABC):
    @abstractmethod
    def load(self, menu_name: str) -> List[Dict]:
        ...
class IMenuBuilder(ABC):
    @abstractmethod
    def build_tree(self, items: List[Dict]) -> Dict[int, List[Dict]]:
        ...
class IActiveResolver(ABC):
    @abstractmethod
    def resolve_active(self, items: List[Dict], current_path: str) -> Optional[Dict]:
        ...