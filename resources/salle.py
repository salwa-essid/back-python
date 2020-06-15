from flask import Response, request
from database.models import Salle
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
class SalleApi(Resource):
    #@jwt_required
    def get(self):
        Sall = Salle.objects().to_json()
        return Response(Sall, mimetype="application/json", status=200)

    #@jwt_required
    def post(self):
        body = request.get_json()
        print("bbbb",body)
        Sall =Salle(**body).save()
        id = Sall.id
        return {'id': str(id)}, 200

class SallesApi(Resource):
    #@jwt_required
    def put(self, id):
        body = request.get_json()
        Salle.objects.get(id=id).update(Num_salle=body["Num_salle"])
        return '', 200

    #@jwt_required
    def delete(self, id):
        Sall =Salle.objects.get(id=id).delete()
        return '', 200

    #@jwt_required
    def get(self, id):
        Sall = Salle.objects.get(id=id).to_json()
        return Response(Sall, mimetype="application/json", status=200)