from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    UserID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    UserName = db.Column(db.String(80), unique=True, nullable=False)
    Email = db.Column(db.String(120), unique=True, nullable=False)
    PassWord = db.Column(db.String(120), nullable=False)

    def save(self):
        db.session.add(self)
        db.session.commit()
