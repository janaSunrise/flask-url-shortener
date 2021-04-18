from .config import HOST, PORT, DEBUG

if __name__ == '__main__':
    # Import database
    from . import db

    # Import Models
    from .models import ShortenedLink

    # Create all tables
    db.create_all()

    # Import main App
    from . import app

    # Add blueprints
    from .views import views

    app.register_blueprint(views)

    # Run the App
    app.run(host=HOST, port=PORT, debug=DEBUG)
