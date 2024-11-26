from flask import Flask
import logging
from config import init_db, setup_logger, load_config

def start_app():
    print("start")
    app = Flask(__name__)
    
    try:
        print("start2")
        init_db()
        setup_logger()
        print("start3")

        app.config.update(load_config())
        print("start4")

    except Exception as e:
        logging.critical(f"Failed at initialization: {str(e)}")

    @app.route("/")
    def index():
        return("Hello, world!")

    # Catch-all route
    @app.route('/<path:path>', methods=["GET", "POST", "PUT", "DELETE"])
    def catch_all(path):
        return "Route not found", 404

    return app

if __name__ == '__main__':
    app = start_app()
    logging.info("Starting Flask app")
    app.run(debug=app.config["DEBUG"], port=app.config["PORT"], host=app.config["HOST"])