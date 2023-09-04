from abc import ABC, abstractmethod

from src.model.item import Item


class IItemService(ABC):

    @abstractmethod
    def get_items(self) -> list:
        pass

    @abstractmethod
    def get_item(self, item_id) -> dict | None:
        pass
