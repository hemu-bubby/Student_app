from utils.db import db


class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    usn = db.Column(db.String(20), nullable=False)
    branch = db.Column(db.String(20), nullable=False)
    semester = db.Column(db.String(20), nullable=False)
    section = db.Column(db.Integer())
    dob = db.Column(db.Date)
    address = db.Column(db.String(200), nullable=True)
    phone_number = db.Column(db.String(15), nullable=True)
    father_name = db.Column(db.String(50), nullable=True)
    father_phone = db.Column(db.String(15), nullable=True)
    mother_name = db.Column(db.String(50), nullable=True)
    mother_phone = db.Column(db.String(15), nullable=True)