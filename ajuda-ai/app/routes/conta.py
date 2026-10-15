from app.models import Usuario, Publicacao
from app import db
from flask import Blueprint, request, render_template, redirect, url_for
from flask_login import login_required, current_user
import os
from config import BASE_DIR

conta_bp=Blueprint("conta", __name__)

@conta_bp.route("/", methods=["POST", "GET"])
@login_required
def perfil():
    try:
        publicacoes_usuario=Publicacao.query.filter_by(usuario_id=current_user.id).all()
    except Exception:
        return redirect(url_for("principal.portal"))
    return render_template("perfil.html", usuario=current_user,publicacoes=publicacoes_usuario)

@conta_bp.route("/editarperfil", methods=["POST", "GET"])
@login_required
def editar_perfil():
    if request.method == "POST":
        try:
            nome=request.form["nome"]
            bio=request.form["bio"]
            foto=request.files.get("foto")
            nome_foto=foto.filename if foto and foto.filename else None
            if foto and foto.filename:
                if current_user.foto_perfil:
                    caminho_antigo=f"{BASE_DIR}/app/static/img/usuarios/{current_user.foto_perfil}"
                    if os.path.exists(caminho_antigo):
                        os.remove(caminho_antigo)
                foto.save(os.path.join(f"{BASE_DIR}/app/static/img/usuarios", nome_foto))
                current_user.foto_perfil=nome_foto
        
            current_user.nome=nome
            current_user.bio=bio
        
            db.session.commit()
        
            return redirect(url_for("conta.perfil"))
        except Exception:
            db.session.rollback()
            return render_template("editarperfil.html",usuario=current_user,erro="Erro identificado, tente novamente!!")
    return render_template("editarperfil.html",usuario=current_user)
    
@conta_bp.route("/publicar", methods=["POST", "GET"])
@login_required
def publicar():
    if request.method == "POST":
        try:
            titulo=request.form["titulo"]
            descricao=request.form["descricao"]
            pix=request.form["pix"]
            imagem=request.files.get("imagem")
            
            imagem_nome=imagem.filename if imagem and imagem.filename else None
            if imagem and imagem.filename:
                imagem.save(os.path.join(f"{BASE_DIR}/app/static/img/publicacao", imagem_nome))
            
            publicacao=Publicacao(titulo=titulo,descricao=descricao,pix=pix,usuario_id=current_user.id,imagem=imagem_nome)
            db.session.add(publicacao)
            db.session.commit()
            return redirect(url_for("conta.perfil"))
            
        except Exception:
            db.session.rollback()
            return render_template("publicar.html",erro="Erro na publicação, tente novamente")   
    return render_template("publicar.html")
    
@conta_bp.route("/editarpublicacao/<int:id>", methods=["POST", "GET"])
@login_required
def editar_publicacao(id):
    publicacao=Publicacao.query.get(id)
    if publicacao is None:
        return redirect(url_for("conta.perfil"))
    if publicacao.usuario_id != current_user.id:
        return redirect(url_for("conta.perfil"))
    if request.method == "POST":
        try:
                
            titulo=request.form["titulo"]
            descricao=request.form["descricao"]
            pix=request.form["pix"]
            imagem=request.files.get("imagem")
            nome_imagem=imagem.filename if imagem and imagem.filename else None
            if imagem and imagem.filename:
                if publicacao.imagem:
                    caminho_antigo=f"{BASE_DIR}/app/static/img/publicacao/{publicacao.imagem}"
                    if os.path.exists(caminho_antigo):
                        os.remove(caminho_antigo)
                imagem.save(os.path.join(f"{BASE_DIR}/app/static/img/publicacao", nome_imagem))
                publicacao.imagem=nome_imagem
        
            publicacao.titulo=titulo
            publicacao.descricao=descricao
            publicacao.pix=pix
        
            db.session.commit()
        
            return redirect(url_for("conta.perfil"))
        except Exception:
            db.session.rollback()
            return render_template("editarpublicacao.html",publicacao=publicacao, erro="Erro identificado, tente novamente!!")   
    return render_template("editarpublicacao.html",publicacao=publicacao)