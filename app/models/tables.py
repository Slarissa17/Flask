from app import db

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_completo = db.Column(db.String(200))
    idade = db.Column(db.Integer)
    sexo = db.Column(db.String(9))
    cpf = db.Column(db.String(11), unique=True)


    def __init__(self, nome_completo, idade, sexo, cpf): # O que vai receber quando a classe (user) for inicializada
        self.nome_completo = nome_completo
        self.idade = idade
        self.sexo = sexo
        self.cpf = cpf
        

    def __repr__(self): # Representação do objeto
        return "<User %r>" % self.nome_completo
    
class Variante(db.Model):
    __tablename__ = "variantes"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cromossomo = db.Column(db.String(4))
    posicao = db.Column(db.Integer)
    base_ref = db.Column(db.String(1))
    base_alt = db.Column(db.String(1))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    user = db.relationship("User", foreign_keys=user_id)

    def __init__(self, cromossomo, posicao, base_ref, base_alt, user_id):
        self.cromossomo = cromossomo
        self.posicao = posicao
        self.base_ref = base_ref
        self.base_alt = base_alt
        self.user_id = user_id
    def __repr__(self):
        return "<Variante %r>" % self.cromossomo

