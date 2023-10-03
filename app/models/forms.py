from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired

class FormPaciente(FlaskForm):
    nomeCompleto = StringField('Nome Completo', validators=[DataRequired()])
    idade = StringField('Idade', validators=[DataRequired()])
    sexo = SelectField('Selecione o gênero', choices=[('masculino', 'Masculino'), ('feminino', 'Feminino')])
    cpf = StringField('cpf', validators=[DataRequired()])

class FormVariante(FlaskForm):
    cromossomo = StringField('Cromossomo', validators=[DataRequired()])
    posicao = StringField('Posição', validators=[DataRequired()])
    base_ref = StringField('Base de referência', validators=[DataRequired()])
    base_alt = StringField('Base alternativa', validators=[DataRequired()])
    