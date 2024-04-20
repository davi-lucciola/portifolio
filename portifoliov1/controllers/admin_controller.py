from portifoliov1.config import db
from portifoliov1.models import User
from flask import Blueprint, flash, redirect, render_template, request
from flask_login import login_required, login_user, logout_user


admin_bp = Blueprint("Admin", __name__)


@admin_bp.route("/admin", methods=['GET'])
@login_required
def admin():
    return render_template("admin/index.html")

@admin_bp.route("/login", methods=['POST'])
def login():
    user_payload = {
        'username': request.form.get('username'),
        'password': request.form.get('password')
    }

    user = (db.session.query(User)
        .where(User.username == user_payload['username']).first())
    
    if user is None or not user.verify_password(user_payload['password']):
        flash('Credenciais Inválidas', category='error')
        return redirect("/admin/login")
    
    login_user(user)
    return redirect('/admin')

@admin_bp.route("/logout", methods=['GET'])
@login_required
def logout():
    logout_user()
    return redirect('/')

@admin_bp.route("/admin/login", methods=['GET'])
def admin_login():
    return render_template('admin/login.html')
