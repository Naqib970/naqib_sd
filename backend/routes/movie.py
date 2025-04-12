from flask import Blueprint
from controllers.movie import MovieController

movie_bp = Blueprint('movie', __name__)

@movie_bp.route('/movies/<category>', methods=['GET'])
def get_movies_by_category(category):
    """
    Get movies by category
    ---
    parameters:
      - name: category
        in: path
        required: true
        schema:
          type: string
          enum: [new_release, popular, recommended]
    responses:
      200:
        description: A list of movies by category
    """
    return MovieController.get_movies_by_category(category)
