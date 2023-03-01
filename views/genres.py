from flask_restx import Namespace, Resource

from dao.model.genres import GenresSchema
from implemented import genres_service

genres_ns = Namespace('genres')

genres_schema = GenresSchema(many=True)
genre_schema = GenresSchema()


@genres_ns.route('/')
class GenresView(Resource):
    def get(self):
        genres = genres_service.get_all_genres()
        return genres_schema.dump(genres), 200


@genres_ns.route('/<int:gid>')
class GenreView(Resource):
    @staticmethod
    def get(gid):
        genre = genres_service.get_one_genre(gid)
        return genre_schema.dump(genre), 200
