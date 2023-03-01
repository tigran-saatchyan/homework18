from dao.model.directors import Directors


class DirectorsDAO:
    def __init__(self, session):
        self.session = session

    def get_all_directors(self):
        return self.session.query(Directors).all()

    def get_one_director(self, did):
        return self.session.query(Directors).filter(
            Directors.id == did
        ).one()

    def post_director(self, director):
        director = Directors(**director)
        self.session.add(director)
        self.session.commit()
