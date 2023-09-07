from flask import Flask
from src.controller.item_controller import ItemController

app = Flask(__name__)

item_controller: ItemController = ItemController()

@app.route('/items', methods=['GET'])
async def get_items_route():
    return await item_controller.get_items()

@app.route('/items/<int:item_id>', methods=['GET'])
async def get_item_route(item_id):
    return await item_controller.get_item(item_id)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
