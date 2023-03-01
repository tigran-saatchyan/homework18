import logging

from flask_restx import Namespace, Resource

from dao.model.genres import GenresSchema
from implemented import genres_service
from log_handler import views_logger

genres_ns = Namespace('genres')

genres_schema = GenresSchema(many=True)
genre_schema = GenresSchema()


@genres_ns.route('/')
class GenresView(Resource):
    @staticmethod
    def get():
        views_logger.info('Retrieving all genres')
        genres = genres_service.get_all_genres()
        views_logger.debug(f'Retrieved {len(genres)} genres')
        return genres_schema.dump(genres), 200


@genres_ns.route('/<int:gid>')
class GenreView(Resource):
    @staticmethod
    def get(gid):
        views_logger.info(f'Retrieving genre with id {gid}')
        genre = genres_service.get_one_genre(gid)
        if genre:
            views_logger.debug(f'Retrieved genre: {genre}')
            return genre_schema.dump(genre), 200
        else:
            views_logger.warning(f'Genre with id {gid} not found')
            return {'message': 'Genre not found'}, 404
