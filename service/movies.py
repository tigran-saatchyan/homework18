from dao.model.movies import Movies
from dao.movies import MoviesDAO


class MoviesService:
    def __init__(self, movies_dao: MoviesDAO):
        self.movies_dao = movies_dao

    def get_all_movies(self, year, did, gid):
        return self.movies_dao.get_all_movies(year, did, gid)

    def get_one_movie(self, mid):
        return self.movies_dao.get_one_movie(mid)

    def post_movie(self, movie):
        return self.movies_dao.post_movie(movie)

    def update_movie(self, mid, movie):
        count_columns = Movies.__table__.columns
        if len(count_columns) - 1 != len(movie.keys()):
            return
        return self.movies_dao.update_movie(mid, movie)

    def delete_movie(self, mid):
        return self.movies_dao.delete_movie(mid)
