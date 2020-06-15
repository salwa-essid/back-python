from flask import Response, request
from database.models import Responsable
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
class ResponsableApi(Resource):
    #@jwt_required
    def get(self):
        responsable = Responsable.objects().to_json()
        return Response(responsable, mimetype="application/json", status=200)

    #@jwt_required
    def post(self):
        body = request.get_json()
        print("bbbb",body)
        responsable = Responsable(**body).save()
        id = responsable.id
        return {'id': str(id)}, 200

class ResponsablesApi(Resource):
    #@jwt_required
    def put(self, id):
        body = request.get_json()
        Responsable.objects.get(id=id).update(Fax=body["Fax"],Adresse=body["Adresse"])
        return '', 200

    #@jwt_required
    def delete(self, id):
        responsable =Responsable.objects.get(id=id).delete()
        return '', 200

    #@jwt_required
    def get(self, id):
        responsable = Responsable.objects.get(id=id).to_json()
        return Response(responsable, mimetype="application/json", status=200)