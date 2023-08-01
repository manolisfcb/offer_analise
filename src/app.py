from flask import Flask
from flask_restful import Api
from base import db









app = Flask(__name__)

api = Api(app)
@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


from routes.get_classification import GetClassification
api.add_resource(GetClassification, '/get-classification')


if __name__ == '__main__':
    app.run(debug=True)