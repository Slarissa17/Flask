from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from app.models.forms import FormPaciente, FormVariante
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__) 
app.config.from_object('config')
db = SQLAlchemy(app)
migrate = Migrate(app, db)
app.secret_key = 'chave'


from app.models import tables, forms
from app.controllers import default


