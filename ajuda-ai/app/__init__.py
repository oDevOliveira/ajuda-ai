from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db=SQLAlchemy()
lgm=LoginManager()

def criar_app():
    app=Flask(__name__)
    app.config.from_object("config.Config")
    db.init_app(app)
    lgm.init_app(app)
    lgm.login_view="autenticacao.login"
    
    from app import models
    from app import routes

    app.register_blueprint(routes.principal_bp)
    app.register_blueprint(routes.autenticacao_bp, url_prefix='/autenticacao')
    app.register_blueprint(routes.conta_bp, url_prefix='/conta')
    app.register_blueprint(routes.moderador_bp, url_prefix='/moderador')
    
    with app.app_context():
        db.create_all()
    return app

@lgm.user_loader
def carregar_usuario(id_usuario):
    return models.Usuario.query.get(int(id_usuario))