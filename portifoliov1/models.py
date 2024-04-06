from portifoliov1.config import db
from flask_login import UserMixin
from sqlalchemy import Column, Integer, String
from werkzeug.security import check_password_hash


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id: Column[int] = Column(Integer, primary_key=True, autoincrement=True)
    username: Column[str] = Column(String, nullable=False)
    password: Column[str] = Column(String, nullable=False)

    def verify_password(self, plain_password: str) -> bool:
        return check_password_hash(self.password, plain_password)

# TODO: Implementar Modelo do Projeto no Banco de Dados.
# class Project(db.Model):
#     __tablename__ = 'projects'

#     id: Column[int] = Column(Integer, primary_key=True, autoincrement=True)
