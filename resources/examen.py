from flask import Response, request
from database.models import Examen
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
class ExamenApi(Resource):
    #@jwt_required
    def get(self):
        mats=Examen.objects()
       
        examen=[]
        for m in mats:
            examen.append(
                {
                    'id':str(m['id']),
                    
                    'enseignants':m["enseignants"]
                }
            )
        return jsonify(examen = examen)
    #@jwt_required
    def post(self):
        body = request.get_json()
        print("bbbb",body)
        exam = Examen(**body).save()
        id = exam.id
        return {'id': str(id)}, 200

class ExamensApi(Resource):
    #@jwt_required
    def put(self, id):
        body = request.get_json()
        Examen.objects.get(id=id).update(date_examen=body["date_examen"])
        return '', 200

    #@jwt_required
    def delete(self, id):
        exam =Examen.objects.get(id=id).delete()
        return '', 200

    #@jwt_required
    def get(self, id):
        exam = Examen.objects.get(id=id).to_json()
        return Response(exam, mimetype="application/json", status=200)