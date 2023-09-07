from src.model.item import Item
from src.service.item_service import ItemService
from src.utils import build_response


class ItemController:

    def __init__(self):
        self.item_service: ItemService = ItemService()

    async def get_items(self) -> list[Item]:
        try:
            items = await self.item_service.get_items()
            return await build_response(items)
        except Exception as e:
            return build_response({"error": "Internal server error"}, 500)
            

    async def get_item(self, item_id) -> Item | None:
        try:
            item = self.item_service.get_item(item_id)
            return await build_response(item)
        except Exception as e:
            return build_response({"error": "Internal server error"}, 500)
