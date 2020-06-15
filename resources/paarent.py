from flask import Response, request
from database.models import Parent
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
class ParentApi(Resource):
    #@jwt_required
    def get(self):
        parent = Parent.objects().to_json()
        return Response(parent, mimetype="application/json", status=200)

    #@jwt_required
    def post(self):
        body = request.get_json()
        print("bbbb",body)
        parent =Parent(**body).save()
        id = parent.id
        return {'id': str(id)}, 200

class ParentsApi(Resource):
    #@jwt_required
    def put(self, id):
        body = request.get_json()
        Parent.objects.get(id=id).update(firstName=body["firstName"],lastName=body["lastName"])
        return '', 200

    #@jwt_required
    def delete(self, id):
        parent =Parent.objects.get(id=id).delete()
        return '', 200

    #@jwt_required
    def get(self, id):
        parent = Parent.objects.get(id=id).to_json()
        return Response(parent, mimetype="application/json", status=200)