from flask import Flask
from flasgger import Swagger
from routes.movie import movie_bp
from db import init_db
from db.data import seed_data
import os

app = Flask(__name__)

# Load environment variables for DB
app.config.update({
    'POSTGRES_HOST': os.getenv("POSTGRES_HOST"),
    'POSTGRES_DB': os.getenv("POSTGRES_DB"),
    'POSTGRES_USER': os.getenv("POSTGRES_USER"),
    'POSTGRES_PASSWORD': os.getenv("POSTGRES_PASSWORD"),
    'SQLALCHEMY_TRACK_MODIFICATIONS': False
})

app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"postgresql://{app.config['POSTGRES_USER']}:"
    f"{app.config['POSTGRES_PASSWORD']}@"
    f"{app.config['POSTGRES_HOST']}:5432/"
    f"{app.config['POSTGRES_DB']}"
)

app.secret_key = os.getenv("FLASK_SECRET_KEY", "your-secret-key")

# Initialize Swagger
Swagger(app)

# Initialize DB
init_db(app)

# Register blueprints for routes
app.register_blueprint(movie_bp)

# Seed initial data before first request
@app.before_request
def setup_data():
    seed_data()

@app.route('/')
def index():
    return {"message": "Cinema Booking Backend Running"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
