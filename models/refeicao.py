from config.database import db

class Refeicao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(500), nullable=False)
    dt_criacao = db.Column(db.DateTime, nullable=False)
    tipo = db.Column(db.String(1), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)