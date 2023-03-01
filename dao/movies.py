from dao.model.movies import Movies


class MoviesDAO:
    def __init__(self, session):
        self.session = session

    def get_all_movies(self, year, did, gid):
        all_movies = self.session.query(Movies)

        if year:
            all_movies = all_movies.filter(Movies.year == year)

        if did:
            all_movies = all_movies.filter(Movies.director_id == did)

        if gid:
            all_movies = all_movies.filter(Movies.genre_id == gid)

        all_movies = all_movies.all()
        return all_movies

    def get_one_movie(self, mid):
        return self.session.query(Movies).filter(
            Movies.id == mid
        ).one()

    def post_movie(self, movie):
        movie = Movies(**movie)
        self.session.add(movie)
        self.session.commit()

    def update_movie(self, mid, movie):
        result = self.session.query(Movies).filter(
            Movies.id == mid
        ).update(movie)

        self.session.commit()
        return result

    def delete_movie(self, mid):
        movie_data = self.get_one_movie(mid)
        self.session.delete(movie_data)
        self.session.commit()
