from marshmallow import Schema, fields

from setup_db import db


class Directors(db.Model):
    __tablename__ = 'directors'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)

    def __repr__(self):
        return f'Director: %s - %s', self.id, self.name


class DirectorsSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
