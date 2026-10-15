from app import db
from datetime import datetime, timedelta

class Comentario(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    conteudo=db.Column(db.Text)
    data=db.Column(db.DateTime,nullable=False, default=lambda:datetime.now())
    publicacao_id=db.Column(db.Integer, db.ForeignKey("publicacao.id"),nullable=False)
    usuario_id=db.Column(db.Integer, db.ForeignKey("usuario.id"),nullable=False)
    usuario=db.relationship("Usuario")
    