from flask_sqlalchemy import SQLAlchemy
import psycopg2
import os
from flask import Flask

#would be inside .gitignore if it weren't a challenge
#connecting to DB
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
db = SQLAlchemy(app)
engine = db.create_engine(DATABASE_URL)
