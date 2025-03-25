from flask import Flask
from flask_restful import Api
from controller import DevOpsController

app = Flask(__name__)
api = Api(app)

api.add_resource(DevOpsController, '/DevOps')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
