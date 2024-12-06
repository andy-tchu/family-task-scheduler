from flask import Flask
import logging
from config import init_db, setup_logger, load_config
from routes import register_our_blueprints
from flask_jwt_extended import JWTManager
from services.auth_service import require_jwt_token


def start_app():
    app = Flask(__name__)
    
    try:
        init_db()
        setup_logger()

        app.config.update(load_config())
        
        # Initialize JWT
        jwtmanger = JWTManager(app)

        app.before_request(require_jwt_token)

        register_our_blueprints(app)

    except Exception as e:
        logging.critical(f"Failed at initialization: {str(e)}")

    @app.route("/")
    def index():
        return("Family Task Scheduler application working!")

    # Catch-all route
    @app.route('/<path:path>', methods=["GET", "POST", "PUT", "DELETE"])
    def catch_all(path):
        return "Route not found", 404

    return app

if __name__ == '__main__':
    app = start_app()
    logging.info("Starting Flask app")
    app.run(debug=app.config["DEBUG"], port=app.config["PORT"], host=app.config["HOST"])