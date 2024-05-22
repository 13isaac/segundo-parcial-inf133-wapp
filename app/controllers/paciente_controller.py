from flask import Blueprint, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash
from utils.dacorators import role_required
from views import paciente_view
from models.paciente_model import Paciente

paciente = Blueprint("paciente", __name__)