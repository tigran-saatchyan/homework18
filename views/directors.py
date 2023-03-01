import logging

from flask_restx import Namespace, Resource

from dao.model.directors import DirectorsSchema
from implemented import directors_service
from log_handler import views_logger

directors_ns = Namespace('directors')

directors_schema = DirectorsSchema(many=True)
director_schema = DirectorsSchema()



@directors_ns.route('/')
class DirectorsView(Resource):
    @staticmethod
    def get():
        views_logger.info('Getting all directors...')
        directors = directors_service.get_directors()
        views_logger.info(f'Returned {len(directors)} directors')
        return directors_schema.dump(directors), 200


@directors_ns.route('/<int:did>')
class DirectorView(Resource):
    @staticmethod
    def get(did):
        views_logger.info(f'Getting director with id {did}...')
        director = directors_service.get_one_director(did)
        views_logger.info(f'Returned director: {director}')
        return director_schema.dump(director), 200
