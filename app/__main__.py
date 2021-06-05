from .config import HOST, PORT, DEBUG
from .models import bring_databases_into_scope

if __name__ == "__main__":
    # Import database
    from . import db

    # Import Models and Create all tables
    bring_databases_into_scope()

    db.create_all()

    # Import main App
    from . import app

    # Add blueprints
    from . import views

    views_list = ["api", "main", "others"]

    for view in views_list:
        app.register_blueprint(getattr(views, view))

    # Run the App
    app.run(host=HOST, port=PORT, debug=DEBUG)
