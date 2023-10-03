from app import app
from flask import render_template


from app.models.forms import FormPaciente

@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/cadastrarPaciente", methods=['GET', 'POST'])
def cadastroPac():
    form = FormPaciente()
    if form.validate_on_submit():
        return 'Formulário enviado com sucesso!'
    return render_template('cadastroPac.html', 
                           form=form)
