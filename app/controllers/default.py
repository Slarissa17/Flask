from app import app, db
from flask import render_template
from flask import request, flash

from app.models.tables import User
from app.models.forms import FormPaciente

# @app.route("/index")
# @app.route("/")
# def index():
#     return render_template('index.html')

@app.route("/cadastrarPaciente", methods=['GET', 'POST'])
def cadastroPac():
    form = FormPaciente()
    if request.method == 'POST' and form.validate_on_submit():
       #obtem os dados do formulario
       nome_completo = form.nomeCompleto.data
       idade = form.idade.data
       sexo = form.sexo.data
       cpf = form.cpf.data
         #cria um novo usuario
       user = User(nome_completo, idade, sexo, cpf)
       db.session.add(user)
       db.session.commit()
       return "ok"
@app.route("/consultarPaciente/<info>")
@app.route("/consultarPaciente", defaults={"info": None})
def consultarPac(info):
    r = User.query.filter_by(info).first()
    r.nome_completo = "João"
    db.session.add(r)
    db.session.commit()
    return "ok"


@app.route("/atualizarPaciente", methods=['GET', 'POST'])
@app.route("/atualizarPaciente/<info>")
@app.route("/atualizarPaciente", defaults={"info": None})
def atualizarPac(info):
    r = User.query.filter_by(info).first()
    r.nome_completo = "João"
    db.session.add(r)
    db.session.commit()
    return "ok"


@app.route("/deletarPaciente", methods=['GET', 'POST'])
@app.route("/teste", defaults={"info": None})
def teste(info):
    r = User.query.filter_by(cpf="12345678901").first()
    r.nome_completo = "João"
    db.session.delete(r)
    db.session.commit()
    return "ok"
