from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class SinhVien(db.Model):
    
    studentID = db.Column(db.Integer, primary_key=True,autoincrement=True)
    fullName = db.Column(db.String(100), nullable=False)
    dob = db.Column(db.Date, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phoneNumber = db.Column(db.String(20), unique=True, nullable=False)
    address = db.Column(db.Text, nullable=False)
    classID = db.Column(db.String(20), nullable=False)

    def save(self):
        db.session.add(self)
        db.session.commit()