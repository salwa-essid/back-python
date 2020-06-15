
from flask import Response, request
from database.models import Notification
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
class NotificationApi(Resource):
    #@jwt_required
    def get(self):
        notif = Notification.objects().to_json()
        return Response(notif, mimetype="application/json", status=200)

    #@jwt_required
    def post(self):
        body = request.get_json()
        print("bbbb",body)
        notif = Notification(**body).save()
        id = notif.id
        return {'id': str(id)}, 200

class NotificationsApi(Resource):
    #@jwt_required
    def put(self, id):
        body = request.get_json()
        Notification.objects.get(id=id).update(message=body["message"])
        return '', 200

    #@jwt_required
    def delete(self, id):
        notif =Notification.objects.get(id=id).delete()
        return '', 200

    #@jwt_required
    def get(self, id):
        notif = Notification.objects.get(id=id).to_json()
        return Response(notif, mimetype="application/json", status=200)