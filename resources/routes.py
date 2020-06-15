
from .user import SignupApi, LoginApi
from .role import RoleApi
from .enseignnant import EnseignantApi,EnseignantsApi
from .etudiannt import EtudiantApi,EtudiantsApi
from .paarent import ParentApi,ParentsApi
from .ressponsable import ResponsableApi, ResponsablesApi
from .img import Upload1,UploadFile
from .note import NoteApi,NotesApi
from .cours import CoursApi,CourssApi
from .departement import DepartementApi,DepartementsApi
from .notification import NotificationApi,NotificationsApi
from .statistique import StatistiqueApi,StatistiquesApi
from .examen import ExamenApi,ExamensApi
from .matiere import MatiereApi,MatieresApi
from .salle import SalleApi,SallesApi
from .classe import ClasseApi,ClassesApi
from .email import Email
#from .concentration import Apprentissage
#from .output import Apprentissage1

def initialize_routes(api):
  
    # Auth Api
    api.add_resource(LoginApi,'/api/auth')
    api.add_resource(SignupApi, '/api/signup')
     #concentration
    #api.add_resource(Apprentissage, '/api/appren/apprentissage')
    #api.add_resource(Apprentissage1, '/api/apprenout/apprentissage')
    #enseignant
    api.add_resource(EnseignantApi,'/api/enseignnant')
    api.add_resource(EnseignantsApi, '/api/enseignnant/<id>')
    #etudiant
    api.add_resource(EtudiantApi,'/api/etudiannt')
    api.add_resource(EtudiantsApi, '/api/etudiannt/<id>')
    #parent
    api.add_resource(ParentApi,'/api/paarent')
    api.add_resource(ParentsApi, '/api/paarent/<id>')
    #ressponsable
    api.add_resource(ResponsableApi,'/api/ressponsable')
    api.add_resource(ResponsablesApi, '/api/ressponsable/<id>')
   
    #note
    api.add_resource(NoteApi, '/api/note')
    api.add_resource(NotesApi, '/api/note/<id>')
    #departement
    api.add_resource(DepartementApi, '/api/departement')
    api.add_resource(DepartementsApi, '/api/departement/<id>')
    #statistique
    api.add_resource(StatistiqueApi,'/api/statistique')
    api.add_resource(StatistiquesApi, '/api/statistique/<id>')
    #notification 
    api.add_resource(NotificationApi,'/api/notification')
    api.add_resource(NotificationsApi, '/api/notification/<id>')
    #examen
    api.add_resource(ExamenApi,'/api/examen')
    api.add_resource(ExamensApi, '/api/examen/<id>')
    #cours
    api.add_resource(CoursApi,'/api/cours')
    api.add_resource(CourssApi, '/api/cours/<id>')
    #salle
    api.add_resource(SalleApi,'/api/salle')
    api.add_resource(SallesApi, '/api/salle/<id>')
    #classe
    
    api.add_resource(ClasseApi,'/api/classe')
    api.add_resource(ClassesApi, '/api/classe/<id>')

    # Api Role
    api.add_resource(RoleApi, '/api/roles')

    #APi Upload
    api.add_resource(Upload1, '/api/upload')
    api.add_resource(UploadFile, '/api/uploadfile/<fileName>')


    #listematiere
    api.add_resource(MatiereApi,'/api/matiere')
    api.add_resource(MatieresApi, '/api/matiere/<id>')


    #sendmail
    api.add_resource(Email,'/api/email')