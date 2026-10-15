from app import db
from flask import Blueprint, request, render_template, redirect, url_for
from flask_login import login_required, current_user
from app.models import Publicacao, Usuario, Comentario
from sqlalchemy import or_

moderador_bp=Blueprint("moderador", __name__)

@moderador_bp.route("/", methods=["POST", "GET"])
@login_required
def dashboard_moderador():
    try:
        if not current_user.moderador:
            return redirect(url_for("principal.portal"))
        publicacoes=Publicacao.query.all()
        
        if request.method == "POST":
            pesquisa=request.form["pesquisa"]
            publicacoes=Publicacao.query.join(Usuario).filter(or_(Publicacao.titulo.ilike(f"%{pesquisa}%"),Usuario.nome.ilike(f"%{pesquisa}%"))).all()
            return render_template("dashboardmoderador.html", publicacoes=publicacoes)
    except Exception as erro:
        return render_template("dashboardmoderador.html", erro=f"Erro identificado:\n\n{str(erro)}")
        
    return render_template("dashboardmoderador.html", publicacoes=publicacoes)
    
@moderador_bp.route("/excluirpost/<int:id>")
@login_required
def excluir_post(id):
    try:
        if not current_user.moderador:
            return redirect(url_for("principal.portal"))
            
        publicacao=Publicacao.query.get(id)
        if publicacao is None:
            return redirect(url_for("moderador.dashboard_moderador"))
        
        Comentario.query.filter_by(publicacao_id=id).delete()
        db.session.delete(publicacao)
        db.session.commit()
        
        return redirect(url_for("moderador.dashboard_moderador"))
    except Exception:
        return redirect(url_for("moderador.dashboard_moderador"))