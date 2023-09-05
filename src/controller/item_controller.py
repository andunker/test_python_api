from src.model.item import Item
from src.service.item_service import ItemService
from src.utils import build_response


class ItemController:

    def __init__(self):
        self.item_service: ItemService = ItemService()

    def get_items(self) -> list[Item]:
        return build_response(self.item_service.get_items())

    def get_item(self, item_id) -> Item | None:
        item = self.item_service.get_item(item_id)
        if item is not None:
            return build_response(item)
        else:
            return build_response({"error": "Item not found"}, status_code=404)
