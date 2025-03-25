from flask_restful import Resource
from flask import request, jsonify

class DevOpsController(Resource):
    API_KEY = "2f5ae96c-b558-4c7b-a590-a501ae1c3f6c"

    def post(self):
        api_key = request.headers.get("X-Parse-REST-API-Key")
        if api_key != self.API_KEY:
            return {"message": "Unauthorized"}, 401

        payload = request.get_json()
        if not payload or 'to' not in payload:
            return {"message": "Bad Request"}, 400

        response_message = f"Hello {payload['to']} your message will be send"
        return jsonify({"message": response_message})

    def get(self):
        return "ERROR"
