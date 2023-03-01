from dao.directors import DirectorsDAO


class DirectorsService:

    def __init__(self, directors_dao: DirectorsDAO):
        self.directors_dao = directors_dao

    def get_directors(self):
        return self.directors_dao.get_all_directors()

    def get_one_director(self, did):
        return self.directors_dao.get_one_director(did)

    def post_director(self, director):
        return self.directors_dao.post_director(director)
