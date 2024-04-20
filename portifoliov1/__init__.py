from flask import Flask, render_template
from .config import Config, db, migrations
from .auth import login_manager
from .controllers import admin_bp
from .utils import generate_slug


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config) 
    app.jinja_env.globals.update(generate_slug=generate_slug)

    @app.route("/", methods=["GET"])
    def portifolio():
        return render_template("portifolio/index.html")

    app.register_blueprint(admin_bp)

    with app.app_context():
        db.init_app(app)
        migrations.init_app(app)
        login_manager.init_app(app)

    return app
