from app import app, db
from flask import request, jsonify
from flask import send_from_directory
from flask_swagger_ui import get_swaggerui_blueprint


from app.models.tables import User, Variante
from app.models.forms import FormPaciente

@app.route('/static/<path:path>') #ROTA PARA ACESSAR ARQUIVOS ESTÁTICOS
def send_static(path):
    return send_from_directory('static', path)

SWAGGER_URL = '/swagger' #URL PARA ACESSAR A DOCUMENTAÇÃO
API_URL = '/static/swagger.json' #ARQUIVO JSON COM A DOCUMENTAÇÃO
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Test application"})

@app.route('/user/<cpf>')  #CONSULTA USÁRIO PELO CPF
def get_user(cpf):
    user = User.query.filter_by(cpf=cpf).first()
    if user:
        return jsonify({
            'id': user.id,
            'nome_completo': user.nome_completo,
            'idade': user.idade,
            'sexo': user.sexo,
            'cpf': user.cpf
        })
    else:
        return jsonify({'message': 'Usuário não encontrado'}), 404


@app.route('/user/<cpf>/variante') #CONSULTA VARIANTES DO USUÁRIO PELO CPF
def get_user_variantes(cpf):
    user = User.query.filter_by(cpf=cpf).first()

    if user is None:
        return jsonify({'message': 'Usuário não encontrado'}), 404
    variantes = Variante.query.filter_by(user_id=user.id).all()

    variantes_data = []
    for variante in variantes:
        variantes_data.append({
            'cromossomo': variante.cromossomo,
            'posicao': variante.posicao,
            'base_ref': variante.base_ref,
            'base_alt': variante.base_alt
        })

    return jsonify(variantes_data)

@app.route('/user', methods=['POST']) #CADASTRA USUÁRIO
def create_user():
    req_data = request.get_json()
    
    new_user = User(
        nome_completo=req_data['nome_completo'],
        idade=req_data['idade'],
        sexo=req_data['sexo'],
        cpf=req_data['cpf']
    )
    
    db.session.add(new_user)
    
    db.session.commit()
    
    return jsonify({'message': 'Usuário criado com sucesso!'})



@app.route('/user/<string:cpf>/variante', methods=['POST']) #CADASTRA VARIANTES DO USUÁRIO PELO CPF
def create_user_variante(cpf):
    user = User.query.filter_by(cpf=cpf).first()
    if user is None:
        return jsonify({'message': 'Usuário não encontrado'}), 404

    req_data = request.get_json()
    
    new_variante = Variante(
        cromossomo=req_data['cromossomo'],
        posicao=req_data['posicao'],
        base_ref=req_data['base_ref'],
        base_alt=req_data['base_alt'],
        user_id=user.id  
    )
    
    db.session.add(new_variante)
    db.session.commit()
    return jsonify({'message': 'Variante criada com sucesso!'})

@app.route('/user/<string:cpf>', methods=['PUT']) #ATUALIZA USUÁRIO PELO CPF
def update_user(cpf):
    user = User.query.filter_by(cpf=cpf).first()
    if user:
        req_data = request.get_json()
        user.nome_completo = req_data['nome_completo']
        user.idade = req_data['idade']
        user.sexo = req_data['sexo']
        user.cpf = req_data['cpf']
        db.session.commit()
        return jsonify({'message': 'Usuário atualizado com sucesso!'})
    else:
        return jsonify({'message': 'Usuário não encontrado'}), 404
    
@app.route('/user/<string:cpf>/variante/<int:id>', methods=['PUT']) #ATUALIZA VARIANTES DO USUÁRIO PELO CPF
def update_user_variante(cpf, id):
    user = User.query.filter_by(cpf=cpf).first()
    if user is None:
        return jsonify({'message': 'Usuário não encontrado'}), 404
    variante = Variante.query.filter_by(id=id).first()
    if variante:
        req_data = request.get_json()
        variante.cromossomo = req_data['cromossomo']
        variante.posicao = req_data['posicao']
        variante.base_ref = req_data['base_ref']
        variante.base_alt = req_data['base_alt']
        db.session.commit()
        return jsonify({'message': 'Variante atualizada com sucesso!'})
    else:
        return jsonify({'message': 'Variante não encontrada'}), 404
@app.route('/user/<string:cpf>', methods=['DELETE']) #DELETA USUÁRIO PELO CPF
def delete_user(cpf):
    user = User.query.filter_by(cpf=cpf).first()
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'Usuário deletado com sucesso!'})
    else:
        return jsonify({'message': 'Usuário não encontrado'}), 404
@app.route('/user/<string:cpf>/variante/<int:id>', methods=['DELETE']) #DELETA VARIANTES DO USUÁRIO PELO CPF
def delete_user_variante(cpf, id):
    user = User.query.filter_by(cpf=cpf).first()
    if user is None:
        return jsonify({'message': 'Usuário não encontrado'}), 404
    variante = Variante.query.filter_by(id=id).first()
    if variante:
        db.session.delete(variante)
        db.session.commit()
        return jsonify({'message': 'Variante deletada com sucesso!'})
    else:
        return jsonify({'message': 'Variante não encontrada'}), 404



@app.route("/")
def home():
    return "Olá!"
