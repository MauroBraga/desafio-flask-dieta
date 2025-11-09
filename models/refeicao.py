from config.database import db
from flask_login import UserMixin

class Refeicao(db.model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    calorias = db.Column(db.Integer, nullable=False)
    data_hora = db.Column(db.DateTime, nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)