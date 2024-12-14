<!-- first start the env  -->
 .venv\Scripts\Activate

 <!-- deactivate env -->
Deactivate

<!-- migration flask app and sqlAlchemay database -->

<!-- importing flask_migrate  -->
    from flask_migrate import Migrate 

    <!-- create migrate object  -->
    migrate = Migrate()

    # initializing migration  for linking flask app and sqlalchemy database 
    migrate.init_app(app, db)

    <!-- command pt run this three cmd -->
    -pip install flask-migrate
    -flask db init
    -flask db migrate
    -flask db upgrade
