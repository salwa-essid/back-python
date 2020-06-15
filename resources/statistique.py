from flask import Response, request
from database.models import Statistique
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
class StatistiqueApi(Resource):
    #@jwt_required
    def get(self):
        stat= Statistique.objects().to_json()
        return Response(departt, mimetype="application/json", status=200)

    #@jwt_required
    def post(self):
        body = request.get_json()
        print("bbbb",body)
        stat = Statistique(**body).save()
        id = depart.id
        return {'id': str(id)}, 200

class StatistiquesApi(Resource):
    #@jwt_required
    def put(self, id):
        body = request.get_json()
        Statistique.objects.get(id=id).update(date=body["date"])
        return '', 200

    #@jwt_required
    def delete(self, id):
        stat =Statistique.objects.get(id=id).delete()
        return '', 200

    #@jwt_required
    def get(self, id):
        stat = Statistique.objects.get(id=id).to_json()
        return Response(depart, mimetype="application/json", status=200)