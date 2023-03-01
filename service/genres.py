import logging
from dao.genres import GenresDAO
from log_handler import services_logger


class GenresService:

    def __init__(self, genres_dao: GenresDAO):
        self.genres_dao = genres_dao
        self.logger = services_logger

    def get_all_genres(self):
        self.logger.info('Retrieving all genres')
        return self.genres_dao.get_all_genres()

    def get_one_genre(self, gid):
        self.logger.info(f'Retrieving genre with ID {gid}')
        return self.genres_dao.get_one_genre(gid)

    def post_genre(self, genre):
        self.logger.info('Adding new genre')
        return self.genres_dao.post_genre(genre)
