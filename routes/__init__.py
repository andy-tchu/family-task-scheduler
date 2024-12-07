from routes.users_bp import users_bp
from routes.families_bp import families_bp
from routes.members_bp import members_bp
from routes.auth_bp import auth_bp
from routes.tasks_bp import tasks_bp

def register_our_blueprints(app):
    app.register_blueprint(auth_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(families_bp)
    app.register_blueprint(members_bp)
    app.register_blueprint(tasks_bp)
    
    # for rule in app.url_map.iter_rules():
    #     print(f"Route: {rule} --> Endpoint: {rule.endpoint}, Methods: {rule.methods}")
    
