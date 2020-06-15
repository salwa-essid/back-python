from .db import db

from flask_bcrypt import generate_password_hash, check_password_hash

class User(db.Document):
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True, min_length=6)
    role = db.ReferenceField('Role')
    meta = {'strict': False}
    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')
    def check_password(self, password):
        return check_password_hash(self.password, password)


class Role(db.Document):
    name = db.StringField(required=True)
    meta = {'strict': False}

class Admin(db.Document):
    
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True, min_length=6)
    role = db.ReferenceField('Role')

    
    
    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')
    
    def check_password(self, password):
        return check_password_hash(self.password, password)

class Enseignant(db.Document):
    firstName=db.StringField(required=True)
    lastName=db.StringField(required=True)
    num_tel=db.IntField(required=True)
    specialite=db.StringField(required=True)
    email = db.EmailField(required=True, unique=True)
    #password = db.StringField(required=True)
    added_by=db.ReferenceField('User')
    cours=db.ListField(db.ReferenceField('Cours'))
    meta = {'strict': False}

class Etudiant(db.Document):
    firstName=db.StringField(required=True)
    lastName=db.StringField(required=True)
    niveau=db.StringField(required=True)
    Num_cin=db.IntField(required=True)
    Num_tel=db.IntField(required=True)
    email = db.EmailField(required=True, unique=True)
    #password = db.StringField(required=True)
   
    added_by=db.ReferenceField('User')
    meta = {'strict': False}

class Parent(db.Document):
    firstName=db.StringField(required=True)
    lastName=db.StringField(required=True)
    Num_tel=db.IntField(required=True)
    email=db.EmailField(required=True, unique=True)
    #password = db.StringField(required=True)
    added_by=db.ReferenceField('User')
    meta = {'strict': False}

class Responsable(db.Document):
    firstName=db.StringField(required=True)
    lastName=db.StringField(required=True)
    fax=db.IntField(required=True)
    email=db.StringField(required=True)
    #password = db.StringField(required=True)
    added_by=db.ReferenceField('User')
    meta = {'strict': False}

class Matiere(db.Document):
    Nom=db.StringField(required=True)
    Coef=db.IntField(required=True)
    added_by=db.ReferenceField('Enseignant')
    cours=db.ListField(db.ReferenceField('Cours'))
    meta = {'strict': False}
    
class Concentration(db.Document):
    Happy=db.IntField()
    Angry=db.IntField()
    Sad=db.IntField()
    Surprise=db.IntField()
    Neutral=db.IntField()
    meta = {'strict': False}

class Output(db.Document):
    Happy=db.IntField()
    Angry=db.IntField()
    Sad=db.IntField()
    Surprise=db.IntField()
    Neutral=db.IntField()
    Presence=db.IntField()
    concenctrer=db.IntField()
    meta = {'strict': False}

class Cours(db.Document):
    matieres=db.ListField(db.ReferenceField('Matiere'))
    Enseignants=db.ListField(db.ReferenceField('Enseignant'))
    added_by=db.ReferenceField('Enseignant')
    photo=db.StringField(required=True)
    meta = {'strict': False}

class Note(db.Document):
    Moyenne=db.IntField()
    added_by=db.ReferenceField('Enseignant')
    meta = {'strict': False}

class Departement(db.Document):
    Nom=db.StringField(required=True)
    Adresse=db.StringField(required=True)
    Fax=db.IntField()
    Num_tel=db.IntField()
    Nombre_salle=db.IntField()
  
    Email=db.EmailField(required=True)
    added_by=db.ReferenceField('Responsable')
    meta = {'strict': False}

class Notification(db.Document):
    Sujet=db.StringField(required=True)
    Date=db.DateTimeField(format='%d/%m/%Y')
    added_by=db.ReferenceField('Responsable')
    meta = {'strict': False}

class Statistique(db.Document):
    date=db.DateTimeField(format='%d/%m/%Y')
    Presence_etudiant=db.DateField()
    Concentration_etudiant=db.DateField()
    Heure=db.StringField(required=True)
    added_byconcen=db.ReferenceField('Concentration')
    added_byou=db.ReferenceField('Output')
    meta = {'strict': False}

class Examen(db.Document):
    Nom_examen=db.StringField(required=True)
    durée_examen=db.IntField()
    date_examen=db.StringField()
    matieres=db.ListField(db.ReferenceField('Matiere'))
    Enseignants=db.ListField(db.ReferenceField('Enseignant'))
    added_by=db.ReferenceField('Enseignant')
    meta = {'strict': False}    

class Salle(db.Document):
    Num_salle=db.IntField(required=True)
    added_byres=db.ReferenceField('Responsable')
    added_bydep=db.ReferenceField('Departement')
    meta = {'strict': False}
class Classe(db.Document):
    Niveau_classe=db.IntField(required=True)
    added_byres=db.ReferenceField('Enseignant')
    meta = {'strict': False}

class Photo(db.Document):
    img=db.StringField(required=True)
    added_byres=db.ReferenceField('Enseignant')
    meta = {'strict': False}







   

