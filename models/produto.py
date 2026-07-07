from models.database import db

class Produto(db.Model):
    __tablename__ = 'produto'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(200), nullable=False)
    preco_custo = db.Column(db.Numeric(10,2), nullable=False)
    preco_venda = db.Column(db.Numeric(10,2), nullable=False)
    quantidade = db.Column(db.Integer, default=0)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categoria.id'), nullable=False)