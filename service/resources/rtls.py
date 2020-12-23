from flask_restful import Resource


class Rtls(Resource):
    def __init__(self, **kwargs):
        self.logger = kwargs.get('logger')

    def get(self, package, change_id):
        return {'msg': f"Test with {package}"}, 200

    def post(self, package, change_id):
        pass

    def put(self, package, change_id):
        pass

    def delete(self, package, change_id):
        pass
