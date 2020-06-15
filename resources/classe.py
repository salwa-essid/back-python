from flask import Response, request
from database.models import Classe
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
class ClasseApi(Resource):
    #@jwt_required
    def get(self):
        classe = Classe.objects().to_json()
        return Response(classe, mimetype="application/json", status=200)

    #@jwt_required
    def post(self):
        body = request.get_json()
        print("bbbb",body)
        classe = Classe(**body).save()
        id = classe.id
        return {'id': str(id)}, 200

class ClassesApi(Resource):
    #@jwt_required
    def put(self, id):
        body = request.get_json()
        Classe.objects.get(id=id).update(Niveau_classe=body["Niveau_classe"])
        return '', 200

    #@jwt_required
    def delete(self, id):
        classe =Classe.objects.get(id=id).delete()
        return '', 200

    #@jwt_required
    def get(self, id):
        classe = Classe.objects.get(id=id).to_json()
        return Response(classe, mimetype="application/json", status=200)