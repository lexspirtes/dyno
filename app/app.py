import os
from flask import Flask
from flask import render_template
from flask import request
import psycopg2
from etl import Etl

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
db = SQLAlchemy(app)

class Virus(db.Model):
    __tablename__ = "viruses"
    header = db.Column(db.Text, primary_key=True, nullable=False)
    sequence = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return "<Header: {}>".format(self.header) + "<Sequence: {}>".format(self.sequence)

def addRows():
    if Virus.query.first() == None:
        engine = db.create_engine(DATABASE_URL)
        df = Etl().data
        df.to_sql('viruses', engine, if_exists="append", index=False)
        print("done adding rows")

addRows()

@app.route("/", methods = ["POST", "GET"])
def home():
    if request.form:
        searchSeq = request.form.get('sequence')
        exact = Virus.query.filter(Virus.sequence.like('%' + searchSeq + '%')).all()
    return render_template("home.html", viruses=exact)

if __name__ == "__main__":
    app.run(debug=True)
