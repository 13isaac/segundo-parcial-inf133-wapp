from flask import render_template
from flask_login import current_user

def list_pacient(users):
    return render_template(
        "patients.html",
        title="Lista de apcientes",
        users=users,
        current_user=current_user
    )
