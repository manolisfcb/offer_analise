from flask_restful import Resource


class GetClassification(Resource):
    def get(self):
        return {"message": "Hello, World!"}