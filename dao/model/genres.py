# здесь модель SQLAlchemy для сущности, также могут быть дополнительные методы работы с моделью (но не с базой, с базой мы работает в классе DAO)
from marshmallow import Schema, fields

from setup_db import db


class Genres(db.Model):
    __tablename__ = 'genres'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)

    def __repr__(self):
        return f'Genre: {self.id} - {self.name}'


class GenresSchema(Schema):
    id = fields.Int()
    name = fields.Str()
