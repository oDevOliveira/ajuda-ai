from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from app.models import Publicacao, Usuario, Comentario
from app import db
from sqlalchemy import or_
import random

principal_bp = Blueprint("principal", __name__)

@principal_bp.route("/", methods=["POST", "GET"])
def portal():
    publicacoes=None
    try:
        publicacoes=Publicacao.query.all()
        if request.method == "POST":
            pesquisa=request.form["pesquisa"]
            publicacoes=Publicacao.query.join(Usuario).filter(or_(Publicacao.titulo.ilike(f"%{pesquisa}%"),Usuario.nome.ilike(f"%{pesquisa}%"))).all()
            return render_template("portal.html", publicacoes=publicacoes)
    except Exception as erro:
        return render_template("portal.html", erro=f"Erro identificado: {str(erro)}")
    return render_template("portal.html", publicacoes=publicacoes)
    
@principal_bp.route("/publicacao/<int:id>", methods=["POST", "GET"])
def publicacao(id):
    try:
        publicacao=Publicacao.query.get(id)
        comentarios_publicacao=Comentario.query.filter_by(publicacao_id=id).all()
        if publicacao is None:
            return render_template("publicacao.html", erro="Publicação inexistente!!")
        if request.method == "POST":
            conteudo_comentario=request.form["conteudo_comentario"]
            
            comentario=Comentario(conteudo=conteudo_comentario,usuario_id=current_user.id,publicacao_id=id)
            db.session.add(comentario)
            db.session.commit()
            comentarios_publicacao=Comentario.query.filter_by(publicacao_id=id).all()
            return render_template("publicacao.html", publicacao=publicacao, comentarios=comentarios_publicacao)
            
    except Exception as erro:
        db.session.rollback()
        return render_template("publicacao.html", erro=f"Erro no carregamento da publicação: {str(erro)}")
    return render_template("publicacao.html", publicacao=publicacao, comentarios=comentarios_publicacao)
    
@principal_bp.route("/aleatorio")
def aleatorio():
    try:
        publicacoes=Publicacao.query.all()
        if publicacoes:
            publicacao=random.choice(publicacoes)
            return redirect(url_for("principal.publicacao", id=publicacao.id))
        else:
            return redirect(url_for("principal.portal"))  
    except Exception:
        return redirect(url_for("principal.portal"))