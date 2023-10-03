from app import app, db
from flask import render_template

from app.models.tables import User
from app.models.forms import FormPaciente

@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/cadastrarPaciente", methods=['GET', 'POST'])
def cadastroPac():
    form = FormPaciente()
    if form.validate_on_submit():
        print("Formulário válido e submetido!")
        print("Idade:", form.idade.data)
        print("Nome Completo:", form.nomeCompleto.data)
    else:
        print(form.errors)

    return render_template('cadastroPac.html', 
                           form=form)


@app.route("/teste/<info>")
@app.route("/teste", defaults={"info": None})
def teste(info):
    r = User.query.filter_by(cpf="12345678901").first()
    r.nome_completo = "João"
    db.session.delete(r)
    db.session.commit()
    return "ok"
