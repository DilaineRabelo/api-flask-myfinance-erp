from flask import Flask, request
from models.database import db
from models.categoria import Categoria
from models.produto import Produto
from models.cliente import Cliente
from flask_cors import CORS
from flasgger import Swagger

app = Flask(__name__ )
swagger = Swagger(app)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sistema.db'
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/health', methods=['GET'])
def teste_health():
    """
    Health check da API
    ---
    tags:
      - Health
    responses:
      200:
        description: API funcionando corretamente
        schema:
          type: object
          properties:
            status:
              type: string
            mensagem:
              type: string
    """
    teste = {"status":"Ok", "mensagem":"API rodando"}
    return teste, 200

# =============================== ROTAS DE CATEGORIAS ==========================
@app.route('/categorias', methods=['POST'])
def inserir_categoria():
    """
    Cadastrar uma nova categoria
    ---
    tags:
      - Categorias
    consumes:
      - application/json
    parameters:
      - name: nome
        in: body
        type: string
        required: true
        description: Nome da categoria
    responses:
      201:
        description: Categoria cadastrada com sucesso
      400:
        description: Categoria não pode ser vazia
      409:
        description: Categoria já existe ou campo obrigatório ausente
    """
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
    """
    Listar categorias
    ---
    tags:
      - Categorias
    responses:
      200:
        description: Lista de categorias retornada com sucesso
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
              nome:
                type: string
    """
    lista_categorias = []
    categorias_db = Categoria.query.all()

    for categoria in categorias_db:
        lista_categorias.append({'id':categoria.id, 'nome':categoria.nome})
    return lista_categorias, 200

@app.route('/categorias/<int:id>', methods=['GET'])
def buscar_categoria_id(id):
    """
    Buscar categoria por ID
    ---
    tags:
      - Categorias
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID da categoria
    responses:
      200:
        description: Categoria encontrada com sucesso
      404:
        description: Categoria não existe
    """
    categoria = Categoria.query.get(id)
    if categoria == None:
        return{'erro':'Id da categoria não existe'}, 404
    return {'id':categoria.id, 'nome':categoria.nome}, 200

@app.route('/categorias/<int:id>', methods=['PUT'])
def atualizar_categoria_id(id):
    """
    Atualizar categoria por ID
    ---
    tags:
      - Categorias
    consumes:
      - application/json
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID da categoria
      - name: nome
        in: body
        type: string
        required: true
        description: Novo nome da categoria
    responses:
      200:
        description: Categoria atualizada com sucesso
      404:
        description: Categoria não existe
    """
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
    """
    Excluir categoria por ID
    ---
    tags:
      - Categorias
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID da categoria
    responses:
      200:
        description: Categoria removida com sucesso
      404:
        description: Categoria não existe
    """
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