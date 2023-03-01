from flask import request
from flask_restx import Api, Namespace, Resource, reqparse

from dao.model.movies import MoviesSchema
from implemented import movies_service

movies_ns = Namespace('movies')

movies_schema = MoviesSchema(many=True)
movie_schema = MoviesSchema()

api = Api()

movies_parser = reqparse.RequestParser()
movies_parser.add_argument(
    'year',
    type=int,
    help='(optional) Filter by year'
)

movies_parser.add_argument(
    'director_id',
    type=int,
    help='(optional) Filter by director ID:'
)

movies_parser.add_argument(
    'genre_id',
    type=int,
    help='(optional) Filter by genre ID:'
)


@movies_ns.route('/')
class MoviesView(Resource):
    @api.doc(parser=movies_parser)
    @movies_ns.response(200, 'Success')
    @movies_ns.response(400, 'Bad Request')
    def get(self):
        params = ['year', 'director_id', 'genre_id']
        errors = {
            param: f"{param.title()} must be a digital value" for param
            in params if
            request.args.get(param) and not request.args.get(
                param
            ).isdigit()
        }

        if errors:
            return errors, 400

        year, director_id, genre_id = (
            request.args.get(param, 0, type=int)
            for param in params
        )

        movies = movies_service.get_all_movies(year, director_id, genre_id)
        return movies_schema.dump(movies), 200

    @staticmethod
    def post():
        movie = request.json
        movies_service.post_movie(movie)
        return "", 201


@movies_ns.route('/<int:mid>')
class MovieView(Resource):
    @staticmethod
    def get(mid):
        movie = movies_service.get_one_movie(mid)
        return movie_schema.dump(movie), 200

    @staticmethod
    @movies_ns.response(204, 'No Content')
    def put(mid):
        movie = request.json
        result = movies_service.update_movie(mid, movie)
        if result:
            return "Success", 200
        return {"error": "must contain all required fields"}, 204

    @staticmethod
    def delete(mid):
        movies_service.delete_movie(mid)
        return "", 204
