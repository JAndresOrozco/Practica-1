from flask import Flask
from flask import jsonify
from config import Config
from model import database, Users

app = Flask(__name__)
app.config.from_object(Config)
database.init_app(app)

@app.route('/users')

def index():
  users = [ user.json() for user in Users.query.all() ] 
  return jsonify({'users': users })