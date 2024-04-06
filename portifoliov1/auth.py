from portifoliov1.config import db
from portifoliov1.models import User
from flask import flash, redirect
from flask_login import LoginManager


login_manager = LoginManager()


@login_manager.user_loader
def load_user(id: int) -> User:
    return db.session.query(User).get(id)

@login_manager.unauthorized_handler
def unauthorized_handler():
    flash('Não autenticado.', category='error')
    return redirect('/admin/login')
