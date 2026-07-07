# API Flask para Gestão Financeira

Esta API REST foi desenvolvida em Python com Flask para servir como base para um sistema de gestão financeira e ERP simples. O projeto foi estruturado para demonstrar habilidades com desenvolvimento backend, criação de rotas REST, persistência de dados e documentação de APIs.

## Objetivo do projeto

Criar uma API funcional e organizada para gerenciar categorias de produtos, com possibilidade de expansão para módulos como clientes, produtos e pedidos. O projeto é ideal para compor um portfólio técnico e ser apresentado em entrevistas de emprego.

## Funcionalidades

- Health check da API
- Cadastro de categorias
- Listagem de categorias
- Busca de categoria por ID
- Atualização de categoria
- Exclusão de categoria
- Documentação automática da API com Swagger

## Tecnologias utilizadas

- Python
- Flask
- Flask-SQLAlchemy
- Flask-CORS
- Flasgger
- SQLite

## Estrutura do projeto

```text
api-flask-myfinance-erp/
├── app.py
├── models/
│   ├── categoria.py
│   ├── cliente.py
│   ├── database.py
│   └── produto.py
└── instance/
```

## Como executar o projeto

1. Entre na pasta do projeto:

```bash
cd api-flask-myfinance-erp
```

2. Crie um ambiente virtual:

```bash
python -m venv venv
```

3. Ative o ambiente virtual:

```bash
venv\Scripts\activate
```

4. Instale as dependências:

```bash
pip install flask flask-sqlalchemy flask-cors flasgger
```

5. Execute a aplicação:

```bash
python app.py
```

A API ficará disponível em:

```text
http://localhost:5000
```

## Endpoints principais

### Health check

- GET /health

### Categorias

- POST /categorias
- GET /categorias
- GET /categorias/<id>
- PUT /categorias/<id>
- DELETE /categorias/<id>

### Documentação Swagger

A documentação da API pode ser acessada em:

```text
http://localhost:5000/apidocs
```

## Exemplo de requisição

### Criar categoria

```bash
curl -X POST http://localhost:5000/categorias \
  -H "Content-Type: application/json" \
  -d '{"nome":"Eletrônicos"}'
```


## Autor

Dilaine Rabelo
