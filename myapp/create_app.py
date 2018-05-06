from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# inisialisasi FLASK app
app = Flask(__name__)
app.config['IP_ADDRESS'] = '127.0.0.1'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/weekend'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['ENV'] = 'development'


# Inisialisasi db
db = SQLAlchemy(app=app)
Migrate(app=app, db=db)