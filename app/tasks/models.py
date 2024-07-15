from sqlalchemy import inspect

from app.extensions import db


class Tasks(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    title = db.Column(db.String(225), nullable=False)

    def to_dict(self):
        return {c.key: getattr(self, c.key) for c in
                inspect(self).mapper.column_attrs}

    def __repr__(self):
        return "<%r>" % self.name
