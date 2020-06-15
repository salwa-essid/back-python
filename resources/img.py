from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError
from resources.errors import SchemaValidationError, ProduitAlreadyExistsError, InternalServerError, UpdatingProduitError, DeletingProduitError, ProduitNotExistsError

from werkzeug.utils import secure_filename
from flask_wtf.file import FileField
from flask import request,send_from_directory
from flask import jsonify
import os
from app import app
from database.models import Photo




ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS





class Upload1(Resource):
    def post(self):
        if 'file' not in request.files:
            resp = jsonify({'message': 'No file part in the request'})
            resp.status_code = 400
            return resp
        file = request.files['file']
        if file.filename == '':
            resp = jsonify({'message': 'No file selected for uploading'})
            resp.status_code = 400
            return resp
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            body={'image':filename,'cours':request.form.get('id')}
            photo=Photo(**body).save()
            a=os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(a)
            resp = jsonify({'message': 'File successfully uploaded'})
            resp.statu_code = 201
            return resp
        else:
            resp = jsonify({'message': 'Allowed file types are txt, pdf, png, jpg, jpeg, gif'})
            resp.status_code = 400
            return resp
class UploadFile(Resource):
    def get(self, fileName):
        return send_from_directory(app.config['UPLOAD_FOLDER'],
                                   fileName)