from db.models import Movie, Genre
from flask import jsonify

class MovieController:

    @staticmethod
    def get_movies_by_category(category):
        valid_categories = ['new_release', 'popular', 'recommended']
        if category not in valid_categories:
            return jsonify({"error": "Invalid category"}), 400

        movies = Movie.query.filter_by(category=category).all()
        result = []
        for movie in movies:
            result.append({
                "id": movie.id,
                "name": movie.name,
                "genres": [genre.name for genre in movie.genres],
                "release": movie.release,
                "rating_star": movie.rating_star,
                "totalRatings": movie.totalRatings,
                "age_rating": movie.age_rating,
                "runtime": movie.runtime,
                "sypnosis": movie.sypnosis,
                "cast": movie.cast,
                "director": movie.director,
                "writers": movie.writers,
                "trailer": movie.trailer,
                "poster": movie.poster,
                "category": movie.category,
            })

        return jsonify(result)
