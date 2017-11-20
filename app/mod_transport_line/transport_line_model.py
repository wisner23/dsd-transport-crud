from app import db
from app.mod_transport.transport_model import Transport


class TransportLine(db.Model):

    __tablename__ = "transport_lines"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    hour = db.Column(db.String(50))
    passed = db.Column(db.Boolean, default=False)
    transport_id = db.Column(db.Integer, db.ForeignKey(Transport.id))

    def __init__(self, name, hour, passed, transport_id):
        self.name = name
        self.hour = hour
        self.passed = passed
        self.transport_id = transport_id

    def __repr__(self):
        return "<id {}".format(self.id)
