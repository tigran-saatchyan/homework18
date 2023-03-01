import logging
from dao.directors import DirectorsDAO
from log_handler import services_logger


class DirectorsService:

    def __init__(self, directors_dao: DirectorsDAO):
        self.directors_dao = directors_dao
        self.logger = services_logger

    def get_directors(self):
        self.logger.info('Retrieving all directors')
        return self.directors_dao.get_all_directors()

    def get_one_director(self, did):
        self.logger.info(f'Retrieving director with ID {did}')
        return self.directors_dao.get_one_director(did)

    def post_director(self, director):
        self.logger.info('Adding new director')
        return self.directors_dao.post_director(director)
