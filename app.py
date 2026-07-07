from flask import Flask, request
from models.database import db
from models.categoria import Categoria
from models.produto import Produto
from models.cliente import Cliente
from flask_cors import CORS

app = Flask(__name__ )
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sistema.db'
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/health', methods=['GET'])
def teste_health():
    teste = {"status":"Ok", "mensagem":"API rodando"}
    return teste, 200

# ROTAS DE CATEGORIAS
@app.route('/categorias', methods=['POST'])
def inserir_categoria():
    dados = request.json
    if not 'nome' in dados:
        return{'erro':'O campo nome é obrigatório'}, 409
    categoria_existente = Categoria.query.filter_by(nome=dados['nome']).first()
    if categoria_existente:
        return{'erro':'Categoria já existe'}, 409
    if dados['nome'] == '':
        return{'erro':'Categoria não pode ser vazio'}, 400
    nova_categoria = Categoria(nome=dados['nome'])
    db.session.add(nova_categoria)
    db.session.commit()
    mensagem = {"status":f"Categoria '{dados['nome']}' cadastrada com sucesso!"}
    return mensagem, 201

@app.route('/categorias', methods=['GET'])
def buscar_categoria():
    lista_categorias = []
    categorias_db = Categoria.query.all()

    for categoria in categorias_db:
        lista_categorias.append({'id':categoria.id, 'nome':categoria.nome})
    return lista_categorias, 200

@app.route('/categorias/<int:id>', methods=['GET'])
def buscar_categoria_id(id):
    categoria = Categoria.query.get(id)
    if categoria == None:
        return{'erro':'Id da categoria não existe'}, 404
    return {'id':categoria.id, 'nome':categoria.nome}, 200

@app.route('/categorias/<int:id>', methods=['PUT'])
def atualizar_categoria_id(id):
    dados = request.json
    
    if "nome" not in dados:
        return{"erro":"É necessario informar o campo 'nome'"}
    
    categoria = Categoria.query.get(id)
    if categoria == None:
        return{'erro':'Id da categoria não existe'}, 404
    categoria.nome = dados['nome']
    db.session.commit()
    mensagem = {"status":f"Categoria '{dados['nome']}' atualizada com sucesso!"}
    return mensagem, 200 

@app.route('/categorias/<int:id>', methods=['DELETE'])
def deletar_categoria_id(id):
    categoria = Categoria.query.get(id)
    if categoria == None:
        return{'erro':'Categoria não existe'}, 404
    db.session.delete(categoria)
    db.session.commit()
    mensagem = {"status":f"Categoria removida com sucesso!"}
    return mensagem, 200 

#ROTAS DE PRODUTOS





if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)