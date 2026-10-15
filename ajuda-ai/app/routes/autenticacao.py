from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_required, login_user, logout_user
from app.models import Usuario
import os
from app import db
from config import BASE_DIR

autenticacao_bp=Blueprint("autenticacao", __name__)

@autenticacao_bp.route("/", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        try:
            email=request.form["email"]
            senha=request.form["senha"]
        
            usuario=Usuario.query.filter_by(email=email).first()
            if usuario and check_password_hash(usuario.senha, senha):
                login_user(usuario)
                return redirect(url_for("principal.portal"))
            return render_template("login.html", erro="Email ou senha incorretos!!")
        except Exception:
            return render_template("login.html", erro="Erro identificado, tente novamente")
    return render_template("login.html")

@autenticacao_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("principal.portal"))

@autenticacao_bp.route("/cadastro", methods=["POST", "GET"])
def cadastro():
    if request.method == "POST":
        try:
            nome=request.form["nome"]
            bio=request.form["bio"]
            email=request.form["email"]
            senha=request.form["senha"]
            foto=request.files.get("foto_perfil")
        
            nome_foto=foto.filename if foto and foto.filename else None
            if foto and foto.filename:         
                caminho=os.path.join(f"{BASE_DIR}/app/static/img/usuarios")
                foto.save(os.path.join(caminho, nome_foto))
            
            usuario=Usuario(nome=nome,bio=bio,email=email,senha=generate_password_hash(senha),foto_perfil=nome_foto,moderador=Usuario.query.count() == 0)
            db.session.add(usuario)
            db.session.commit()
        
            login_user(usuario)
            return redirect(url_for("principal.portal"))
        except Exception as erro:
            db.session.rollback()
            return render_template("cadastro.html", erro=f"Erro identificado: {str(erro)}, tente novamente!!")
    return render_template("cadastro.html")