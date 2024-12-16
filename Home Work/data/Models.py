import sqlalchemy as sa
import sqlalchemy.orm as orm
from flask_login import UserMixin
from .db_session import SqlAlchemyBase


class Users(SqlAlchemyBase, UserMixin):
    __tablename__ = 'Users'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True, nullable=False)
    login = sa.Column(sa.String, nullable=False)
    password = sa.Column(sa.String, nullable=False)

    posts = orm.relationship('Posts', cascade="all, delete")
    comments = orm.relationship('Comments', cascade="all, delete")

    def get_id(self):
        return int(self.id)


class Posts(SqlAlchemyBase):
    __tablename__ = 'posts'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True, nullable=False)
    title = sa.Column(sa.String, nullable=False)
    content = sa.Column(sa.String, nullable=False)
    time = sa.Column(sa.String, nullable=False)
    user = sa.Column(sa.Integer, sa.ForeignKey('Users.id', ondelete="CASCADE"), nullable=False)

    def get_id(self):
        return int(self.id)


class Comments(SqlAlchemyBase):
    __tablename__ = 'comments'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True, nullable=False)
    post = sa.Column(sa.Integer, sa.ForeignKey('posts.id', ondelete='CASCADE'), nullable=False)
    content = sa.Column(sa.String, nullable=False)
    time = sa.Column(sa.String, nullable=False)
    user = sa.Column(sa.Integer, sa.ForeignKey('Users.id', ondelete="CASCADE"), nullable=False)

    def get_id(self):
        return int(self.id)
