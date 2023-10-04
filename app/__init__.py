from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from app.models.forms import FormPaciente, FormVariante
from flask_restplus import Api

app = Flask(__name__) 
api = Api(app, version='1.0', title='API de Variantes', description='API para cadastro e consulta de variantes genéticas')
app.config.from_object('config')
db = SQLAlchemy(app)
migrate = Migrate(app, db)
app.secret_key = 'chave'


from app.models import tables, forms
from app.controllers import default


