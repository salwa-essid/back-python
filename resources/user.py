from database.models import Role,User

from flask_restful import Resource
from flask import Response, request,jsonify,make_response
from flask_jwt_extended import create_access_token
import datetime
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist
from resources.errors import SchemaValidationError, EmailAlreadyExistsError, UnauthorizedError, InternalServerError

 
class SignupApi(Resource):

 def post(self):
    try:
       body = request.get_json()
       user = User(**body)
       user.hash_password()
       user.save()
       id = user.id
       #admin = Admin.objects.get(id=admin.id).to_json()
       #return Response(admin, mimetype="application/json", status=200)
       return {'id': str(id)}, 200
    except FieldDoesNotExist:
        raise SchemaValidationError
    except NotUniqueError:
        raise EmailAlreadyExistsError
    except Exception as e:
        raise InternalServerError


class LoginApi(Resource):
     def post(self):
        try:
            body = request.get_json()
            user = User.objects.get(email=body.get('email'))
            authorized = user.check_password(body.get('password'))
            if not authorized:
                raise UnauthorizedError
            expires = datetime.timedelta(days=30)
            access_token = create_access_token(identity=str(user.id), expires_delta=expires)
            responseObject = {
                'status': 'success',
                'message': 'Successfully registered.',
                'auth_token': access_token,
                'user': user,
                 'role':user.role.name

            }
            return make_response(jsonify(responseObject), 200)
        except (UnauthorizedError, DoesNotExist):
            raise UnauthorizedError
        except Exception as e:
            raise InternalServerError

