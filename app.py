from flask import Flask, jsonify, Response
import jsonpickle
from src.controller.item_controller import ItemController
import asyncio

app = Flask(__name__)

item_controller: ItemController = ItemController()


def build_response(data, status_code=200):
    json_data = jsonpickle.encode(data, unpicklable=False)
    return Response(json_data, content_type='application/json'), status_code


@app.route('/items', methods=['GET'])
async def get_items_route():
    # await asyncio.sleep(1)  # Simulate async work
    items = item_controller.get_items()
    return build_response(items)


@app.route('/items/<int:item_id>', methods=['GET'])
async def get_item_route(item_id):
    item = item_controller.get_item(item_id)
    if item is not None:
        return build_response(item)
    else:
        return build_response({"error": "Item not found"}, status_code=404)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
