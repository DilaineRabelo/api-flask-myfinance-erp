from models.database import db

class Cliente(db.Model):
    __tablename__ = 'Cliente'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False, unique=True)
    telefone = db.Column(db.String(20), nullable=True)
    cep = db.Column(db.String(9), nullable=True)
    logradouro = db.Column(db.String(200), nullable=True)
    cidade = db.Column(db.String(100), nullable=True)
    bairro = db.Column(db.String(100), nullable=True)