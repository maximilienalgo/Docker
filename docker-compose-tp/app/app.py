# compose_flask/app.py
from flask import Flask
import flask_sqlalchemy
import sqlalchemy
import sqlalchemy.dialects.mysql

config = {
    'host' : 'localhost',
    'port' : '3320',
    'user' : 'newuser',
    'password': 'newpassword',
    'database' : 'classicmodels'
}

db_user = config.get('user')
db_pwd = config.get('password')
db_host = config.get('host')
db_port = config.get('port')
db_name = config.get('database')

app = Flask(__name__)

def create_app():
    connection_str = 'mysql+mysql://{db_user}:{db_pwd}@{db_host}:3320/{db_name}'
    engine = sqlalchemy.create_engine(connection_str)
    connection = engine.connect()

@app.route('/')
def index():
    return ' - - - MySQL Database `classicmodels` connection ok - - - '



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)