from flask import Response, request
from database.models import Role
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity


class RoleApi(Resource):

    def get(self):
        role = Role.objects().to_json()
        return Response(role, mimetype="application/json", status=200)

    # @jwt_required
    def post(self):
        body = request.get_json()
        role = Role(**body).save()
        id = role.id
        return {'id': str(id)}, 200

