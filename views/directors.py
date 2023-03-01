from flask_restx import Namespace, Resource

from dao.model.directors import DirectorsSchema
from implemented import directors_service

directors_ns = Namespace('directors')

directors_schema = DirectorsSchema(many=True)
director_schema = DirectorsSchema()


@directors_ns.route('/')
class DirectorsView(Resource):
    @staticmethod
    def get():
        directors = directors_service.get_directors()
        return directors_schema.dump(directors), 200


@directors_ns.route('/<int:did>')
class DirectorView(Resource):
    @staticmethod
    def get(did):
        director = directors_service.get_one_director(did)
        return director_schema.dump(director), 200
