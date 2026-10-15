from app import db

class Publicacao(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    titulo=db.Column(db.String(150), nullable=False)
    descricao=db.Column(db.Text)
    pix=db.Column(db.String(100), nullable=False)
    usuario_id=db.Column(db.Integer, db.ForeignKey("usuario.id"), nullable=False)
    imagem=db.Column(db.String(300))
    usuario=db.relationship("Usuario")