from flask_sqlalchemy import SQLAlchemy
from flask_security.utils import encrypt_password
from datetime import datetime


db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ufname = db.Column(db.String(80), unique=False, nullable=False)
    usname = db.Column(db.String(80), unique=False, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    eusermail = db.Column(db.String(120), unique=True, nullable=False)
    upassword = db.Column(db.String(128), unique=True, nullable=False)
    time_of_creation = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self) -> str:
        return f"User id: {self.id}\nUsername: {self.username}\nEmail: {self.eusermail}"
