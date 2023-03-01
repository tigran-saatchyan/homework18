import logging

from dao.model.genres import Genres
from log_handler import dao_logger


class GenresDAO:
    def __init__(self, session):
        self.session = session
        self.logger = dao_logger

    def get_all_genres(self):
        self.logger .info('get_all_genres method called')
        genres = self.session.query(Genres).all()
        self.logger .info('get_all_genres method execution result: %s', genres)
        return genres

    def get_one_genre(self, gid):
        self.logger .info('get_one_genre method called with parameter %s', gid)
        genre = self.session.query(Genres).filter(
            Genres.id == gid
        ).one()
        self.logger .info('get_one_genre method execution result: %s', genre)
        return genre

    def post_genre(self, genre):
        self.logger .info('post_genre method called with parameter %s', genre)
        genre = Genres(**genre)
        self.session.add(genre)
        self.session.commit()
        self.logger .info('post_genre method execution result: %s', genre)
