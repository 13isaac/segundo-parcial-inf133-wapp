from flask import Blueprint, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash
from utils.dacorators import role_required
from views import user_view
from models.user_model import User

user = Blueprint("user", __name__)

@user.route("/")
def index():
    if current_user.is_authenticated:
        return user_view.list_pac()
    return redirect(url_for("user.login"))

@user.route("/users/create", methods=["GET", "POST"])
def create_user():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        role = request.form["role"]
        existing_user = User.get_by_username(username)
        if existing_user:
            flash("El nombre de usuario ya está en uso", "error")
            return redirect(url_for("user.create_user"))

        user = User(username, password, role=role)
        user.set_password(password)
    
        user.save()
        flash("Usuario registrado exitosamente", "success")
        return redirect(url_for("user.index"))
    return user_view.registro()


@user.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = User.get_user_by_username(username)
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            flash("Inicio de sesión exitoso", "success")
            return redirect(url_for("user.index"))
        else:
            flash("Nombre de usuario o contraseña incorrectos", "error")
    return user_view.login()

@user.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Sesión cerrada exitosamente", "success")
    return redirect(url_for("user.login"))

