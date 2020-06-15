from flask import Response, request,jsonify
from database.models import Cours
from database.models import Matiere
from database.models import Enseignant
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
class CoursApi(Resource):
    #@jwt_required
    def get(self):
        mats=Cours.objects()
        

       
        cours=[]
        for m in mats:
            cours.append(
                {
                    'id':str(m['id']),
                    
                    'matieres':m["matieres"],
                    
                }
                 
            )
        
        
        
        return jsonify(cours = cours)
       
    
    
     
    #@jwt_required
    def post(self):
        body = request.get_json()
        print("bbbb",body)
        cour =Cours(**body).save()
        id = cour.id
        return {'id': str(id)}, 200

class CourssApi(Resource):
    #@jwt_required
    def put(self, id):
        body = request.get_json()
        Cours.objects.get(id=id).update(cours=body["cours"])
        return '', 200

    #@jwt_required
    def delete(self, id):
        cour =Cours.objects.get(id=id).delete()
        return '', 200

    #@jwt_required
    def get(self, id):
        cour = Cours.objects.get(id=id).to_json()
        return Response(cour, mimetype="application/json", status=200)
