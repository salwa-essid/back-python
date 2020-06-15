from flask import Response, request
from database.models import Note
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
class NoteApi(Resource):
    #@jwt_required
    def get(self):
        nott = Note.objects().to_json()
        return Response(nott, mimetype="application/json", status=200)

    #@jwt_required
    def post(self):
        body = request.get_json()
        print("bbbb",body)
        nott = Note(**body).save()
        id = nott.id
        return {'id': str(id)}, 200

class NotesApi(Resource):
    #@jwt_required
    def put(self, id):
        body = request.get_json()
        Note.objects.get(id=id).update(Moyenne=body["Moyenne"])
        return '', 200

    #@jwt_required
    def delete(self, id):
        nott =Note.objects.get(id=id).delete()
        return '', 200

    #@jwt_required
    def get(self, id):
        nott = Note.objects.get(id=id).to_json()
        return Response(nott, mimetype="application/json", status=200)