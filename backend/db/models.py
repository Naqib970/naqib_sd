from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

movie_genres = db.Table('movie_genres',
    db.Column('movie_id', db.Integer, db.ForeignKey('movies.id'), primary_key=True),
    db.Column('genre_id', db.Integer, db.ForeignKey('genres.id'), primary_key=True)
)

class Movie(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    genres = db.relationship('Genre', secondary=movie_genres, backref=db.backref('movies', lazy='dynamic'))
    release = db.Column(db.String, nullable=True)
    rating_star = db.Column(db.String, nullable=True)
    totalRatings = db.Column(db.String, nullable=True)
    age_rating = db.Column(db.String, nullable=True)
    runtime = db.Column(db.String, nullable=True)
    sypnosis = db.Column(db.String, nullable=True)
    cast = db.Column(db.String, nullable=True)
    director = db.Column(db.String, nullable=True)
    writers = db.Column(db.String, nullable=True)
    trailer = db.Column(db.String, nullable=True)
    poster = db.Column(db.String, nullable=True)
    category = db.Column(db.String, nullable=True) #new_release,popular,recommended

class Genre(db.Model):
    __tablename__ = 'genres'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)


