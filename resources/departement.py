from flask import Response, request
from database.models import Departement
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
class DepartementApi(Resource):
    #@jwt_required
    def get(self):
        depart = Departement.objects().to_json()
        return Response(depart, mimetype="application/json", status=200)

    #@jwt_required
    def post(self):
        body = request.get_json()
        print("bbbb",body)
        depart = Departement(**body).save()
        id = depart.id
        return {'id': str(id)}, 200

class DepartementsApi(Resource):
    #@jwt_required
    def put(self, id):
        body = request.get_json()
        Departement.objects.get(id=id).update(Adresse=body["Adresse"])
        return '', 200

    #@jwt_required
    def delete(self, id):
        depart =Departement.objects.get(id=id).delete()
        return '', 200

    #@jwt_required
    def get(self, id):
        depart = Departement.objects.get(id=id).to_json()
        return Response(depart, mimetype="application/json", status=200)