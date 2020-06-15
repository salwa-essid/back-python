from flask import Response, request
from database.models import Enseignant
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
class EnseignantApi(Resource):
    #@jwt_required
    def get(self):
        enseignant = Enseignant.objects().to_json()
        return Response(enseignant, mimetype="application/json", status=200)

    #@jwt_required
    def post(self):
        body = request.get_json()
        print("bbbb",body)
        enseignant =  Enseignant(**body).save()
        id = enseignant.id
        return {'id': str(id)}, 200

class EnseignantsApi(Resource):
    #@jwt_required
    def put(self, id):
        body = request.get_json()
        Enseignant.objects.get(id=id).update(firstName=body["firstName"],lastName=body["lastName"],email=body["email"])
        return '', 200

    #@jwt_required
    def delete(self, id):
        enseignant =Enseignant.objects.get(id=id).delete()
        return '', 200

    #@jwt_required
    def get(self, id):
        enseignant = Enseignant.objects.get(id=id).to_json()
        return Response(enseignant, mimetype="application/json", status=200)