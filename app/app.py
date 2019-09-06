from flask import render_template
from flask import request
from etl import Etl
from models import Virus
from config import app, db, engine
from data import hamSQL, exactSQL, editSQL


def addRows():
    """
    only populates db if there is no data in it
    """
    if Virus.query.first() == None:
        df = Etl().data
        df.to_sql('viruses', engine, if_exists="replace", index=False)
        print("done adding rows")

#running addRows to make sure db is populated
addRows()

@app.route("/", methods = ["POST", "GET"])
def home():
    """
    route for home
    """
    #initializing results lists
    exact = []
    hamming = []
    edit = []
    #once html form filled out perform SQL queries
    if request.form:
        searchSeq = request.form.get('sequence')
        exact = db.session.execute(exactSQL(searchSeq)).fetchall()
        hamming = db.session.execute(hamSQL(searchSeq)).fetchall()
        edit = db.session.execute(editSQL(searchSeq)).fetchall()
    return render_template("home.html", exact=exact, hamming=hamming, edit=edit)

if __name__ == "__main__":
    app.run(debug=True)
