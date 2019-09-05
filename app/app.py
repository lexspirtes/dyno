from flask import render_template
from flask import request
from etl import Etl
from models import Virus
from config import app, db
from data import hamSQL, exactSQL


def addRows():
    if Virus.query.first() == None:
        engine = db.create_engine(DATABASE_URL)
        df = Etl().data
        df.to_sql('viruses', engine, if_exists="append", index=False)
        print("done adding rows")

addRows()

@app.route("/", methods = ["POST", "GET"])
def home():
    exact = []
    hamming = []
    if request.form:
    #    engine = db.create_engine(DATABASE_URL)
        searchSeq = request.form.get('sequence')
        exact = db.session.execute(exactSQL(searchSeq)).fetchall()
        print("exact matches:" + str(len(exact)))
        for ex in exact:
            if searchSeq not in ex.sequence:
                print("False")
        hamming = db.session.execute(hamSQL(searchSeq)).fetchall()
        print("hamming matches:" + str(len(hamming)))
    return render_template("home.html", exact=exact, hamming=hamming)

if __name__ == "__main__":
    app.run(debug=True)
