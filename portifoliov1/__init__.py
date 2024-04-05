from flask import Flask, render_template


def create_app():
    app = Flask(__name__)

    @app.route('/', methods=['GET'])
    def index():
        return render_template('index.html')
    
    @app.route('/admin', methods=['GET'])
    def admin():
        return render_template()

    @app.route('/admin/login', methods=['GET'])
    def login():
        return render_template()

    return app