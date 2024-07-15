from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from app.extensions import db, jwt

from config import Config


migrate = Migrate()


def create_app(config_class=Config):
    app = Flask(__name__)
    CORS(app, origins=['http://localhost:3000'])
    app.config.from_object(config_class)


    # Initialize Flask extensions here
    db.init_app(app)
    jwt.init_app(app)
    from app.tasks.models import Tasks
    migrate.init_app(app, db)

    # Register blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.tasks import bp as task_bp
    app.register_blueprint(task_bp)

    from app.users import bp as user_bp
    app.register_blueprint(user_bp)

    @app.route('/test')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    return app
