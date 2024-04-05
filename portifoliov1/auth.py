from flask import Blueprint, render_template


auth_bp = Blueprint('Auth', __name__)


@auth_bp.route('/login', methods=['POST'])
def login():
    pass