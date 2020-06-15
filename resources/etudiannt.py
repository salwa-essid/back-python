from flask import Response, request
from database.models import Etudiant
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
class EtudiantApi(Resource):
    #@jwt_required
    def get(self):
        etudiant = Etudiant.objects().to_json()
        return Response(etudiant, mimetype="application/json", status=200)

    #@jwt_required
    def post(self):
        body = request.get_json()
        print("bbbb",body)
        etudiant = Etudiant(**body).save()
        id = etudiant.id
        return {'id': str(id)}, 200

class EtudiantsApi(Resource):
    #@jwt_required
    def put(self, id):
        body = request.get_json()
        Etudiant.objects.get(id=id).update(niveau=body["niveau"])
        return '', 200

    #@jwt_required
    def delete(self, id):
        etudiant =Etudiant.objects.get(id=id).delete()
        return '', 200

    #@jwt_required
    def get(self, id):
        etudiant = Etudiant.objects.get(id=id).to_json()
        return Response(etudiant, mimetype="application/json", status=200)