from flask import Response
import jsonpickle

async def build_response(data, status_code=200):
    json_data = jsonpickle.encode(data, unpicklable=False)
    return Response(json_data, content_type='application/json'), status_code