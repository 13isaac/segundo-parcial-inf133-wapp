from flask import render_template
from flask_login import current_user

def registro():
    return render_template(
        "registro.html", 
        title="Registro de usuarios", 
        current_user=current_user
    )

def login():
    return render_template(
        "login.html", title="Inicio de sesión", current_user=current_user
    )

def list_pac():
    return render_template(
        "patients.html",
        title="Lista de pacientes",
        current_user=current_user
    )

