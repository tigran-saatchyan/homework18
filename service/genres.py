from dao.genres import GenresDAO


class GenresService:

    def __init__(self, genres_dao: GenresDAO):
        self.genres_dao = genres_dao

    def get_all_genres(self):
        return self.genres_dao.get_all_genres()

    def get_one_genre(self, gid):
        return self.genres_dao.get_one_genre(gid)

    def post_genre(self, genre):
        return self.genres_dao.post_genre(genre)
