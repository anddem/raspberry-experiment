from flask import Flask
from flask_restful import Api, Resource
import requests

app = Flask(__name__)
api = Api(app, prefix="/api/v1")

class Placeholder(Resource):
    def get(self):
        response = requests.get('https://jsonplaceholder.typicode.com/posts/1').json()
        return response

api.add_resource(Placeholder, '/placeholder')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')