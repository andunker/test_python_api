from abc import ABC, abstractmethod

from src.model.item import Item


class IItemService(ABC):

    @abstractmethod
    async def get_items(self) -> list[Item]:
        pass

    @abstractmethod
    async def get_item(self, item_id) -> dict | None:
        pass
