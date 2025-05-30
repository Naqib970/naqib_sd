from flask_sqlalchemy import SQLAlchemy
from .models import db

def init_db(app):
    db.init_app(app)

    # Create all tables
    with app.app_context():
        db.create_all()
