from app import db


class Transport(db.Model):

    __tablename__ = "transports"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<id {}".format(self.id)
