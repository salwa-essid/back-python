from flask import Response, request
from database.models import Matiere
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
class MatiereApi(Resource):
    #@jwt_required
    def get(self):
        mati = Matiere.objects().to_json()
        return Response(mati, mimetype="application/json", status=200)

    #@jwt_required
    def post(self):
        body = request.get_json()
        mati =Matiere(**body).save()
        id = mati.id
        return {'id': str(id)}, 200

class MatieresApi(Resource):
    #@jwt_required
    def put(self, id):
        body = request.get_json()
        Matiere.objects.get(id=id).update(Matiere=body["Nom"])
        return '', 200

    #@jwt_required
    def delete(self, id):
        mati =Matiere.objects.get(id=id).delete()
        return '', 200

    #@jwt_required
    def get(self, id):
        mati = Matiere.objects.get(id=id).to_json()
        return Response(mati, mimetype="application/json", status=200)


