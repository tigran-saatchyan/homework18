import logging

from dao.model.directors import Directors
from log_handler import dao_logger


class DirectorsDAO:
    def __init__(self, session):
        self.session = session
        self.logger = dao_logger

    def get_all_directors(self):
        self.logger.info('get_all_directors method called')
        directors = self.session.query(Directors).all()
        self.logger.info('get_all_directors method execution result: %s', directors)
        return directors

    def get_one_director(self, did):
        self.logger.info('get_one_director method called with parameter %s', did)
        director = self.session.query(Directors).filter(
            Directors.id == did
        ).one()
        self.logger.info('get_one_director method execution result: %s', director)
        return director

    def post_director(self, director):
        self.logger.info('post_director method called with parameter %s', director)
        director = Directors(**director)
        self.session.add(director)
        self.session.commit()
        self.logger.info('post_director method execution result: %s', director)
