from flask_sqlalchemy import SQLAlchemy

database = SQLAlchemy()

class Users(database.Model):
  __tablename__ = 'users'
  def __init__(self, id, name, age):
    self.id = id
    self.name = name
    self.age = age

  def json(self):
    return {
      'id': self.id,
      'name': self.name,
      'age': self.age,
    }

  id = database.Column(database.Integer, primary_key=True)
  name = database.Column(database.String(100), unique=False, nullable=False)
  age = database.Column(database.Integer, unique=False, nullable=False)
