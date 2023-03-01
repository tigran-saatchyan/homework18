# это файл для классов доступа к данным (Data Access Object). Здесь должен быть класс с методами доступа к данным
# здесь в методах можно построить сложные запросы к БД
from dao.model.genres import Genres


# Например

class GenresDAO:
    def __init__(self, session):
        self.session = session

    def get_all_genres(self):
        return self.session.query(Genres).all()

    def get_one_genre(self, gid):
        return self.session.query(Genres).filter(
            Genres.id == gid
        ).one()

    def post_genre(self, genre):
        genre = Genres(**genre)
        self.session.add(genre)
        self.session.commit()
