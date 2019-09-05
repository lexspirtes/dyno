from flask import render_template
from flask import request
from etl import Etl
from models import Virus
from config import app, db


def addRows():
    if Virus.query.first() == None:
        engine = db.create_engine(DATABASE_URL)
        df = Etl().data
        df.to_sql('viruses', engine, if_exists="append", index=False)
        print("done adding rows")

addRows()

def hamSQL(s):
    SQL = "SELECT * FROM VIRUSES WHERE "
    for index,char in enumerate(s):
        SQL +=  "SEQUENCE LIKE '%" + s[:index]+"_"+s[index+1:] + "%'"
        if index != len(s) -1:
            SQL += " OR "
    return SQL

@app.route("/", methods = ["POST", "GET"])
def home():
    exact = []
    hamming = []
    if request.form:
    #    engine = db.create_engine(DATABASE_URL)
        searchSeq = request.form.get('sequence')
        exact = Virus.query.filter(Virus.sequence.like('%' + searchSeq + '%')).all()

        print("exact matches:" + str(len(exact)))
        #need to remove duplicates from matches
        hamming = db.session.execute(hamSQL(searchSeq)).fetchall()

    return render_template("home.html", exact=exact, hamming=hamming)

if __name__ == "__main__":
    app.run(debug=True)
