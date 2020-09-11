from flask_bootstrap import Bootstrap
from flask import Flask
from views import page

app = Flask(__name__)
bootstrap = Bootstrap(app)

def create_app(Config):
    app.config.from_object(Config)
    app.register_blueprint(page)
    return app