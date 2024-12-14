from flask import Flask 
# from os import path 
from .databaseSetUp import create_database, config_db
from flask_migrate import Migrate

db = None
migrate = Migrate()


def create_app():
    global db
    app = Flask(__name__)

    # creating database
    create_database()

    # importing database object
    db = config_db(app)

    # initializing migration  for linking flask app and sqlalchemy database 
    migrate.init_app(app, db)

    with app.app_context():
        # db.drop_all()  # Drop all tables (use only for debugging)
        # Create all tables
        db.create_all()  
    
    # importing routes in route folder 
    from .route import routes
    
    # registering routes and url prefix
    app.register_blueprint(routes, url_prefix="/")
    
    return app