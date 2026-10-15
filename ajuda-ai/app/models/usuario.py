from app import db
from flask_login import UserMixin

class Usuario(UserMixin, db.Model):
    id=db.Column(db.Integer, primary_key=True)
    nome=db.Column(db.String(100), nullable=False)
    bio=db.Column(db.Text)
    email=db.Column(db.String(100), unique=True, nullable=False)
    senha=db.Column(db.String(300), nullable=False)
    foto_perfil=db.Column(db.String(300))
    moderador=db.Column(db.Boolean, default=False)