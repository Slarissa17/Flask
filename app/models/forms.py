from flask_wtf import Form
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired

class FormPaciente(Form):
    nomeCompleto = StringField('Nome Completo', validators=[DataRequired()])
    idade = StringField('Idade', validators=[DataRequired()])
    sexo = SelectField('Selecione o gênero', choices=[('masculino', 'Masculino'), ('feminino', 'Feminino')])
    img = StringField('Imagem', validators=[DataRequired()])