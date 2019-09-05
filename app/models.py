from config import db

class Virus(db.Model):
    __tablename__ = "viruses"
    header = db.Column(db.Text, primary_key=True, nullable=False)
    sequence = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return "<Header: {}>".format(self.header) + "<Sequence: {}>".format(self.sequence)
