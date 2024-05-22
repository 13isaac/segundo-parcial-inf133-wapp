from database import db
from werkzeug.security import check_password_hash
from flask_login import UserMixin

class User(db.Model,UserMixin):
    __tablename__="usuarios"

    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(50),nullable=False)
    password=db.Column(db.String(128),nullable=False)
    role=db.Column(db.String(50),nullable=False)

    def __init__(self,username,password,role):
        self.username=username
        self.password=(password)
        self.role=role

    def save(self):
        db.session.add(self)
        db.session.commit()

    def has_role(self,role):
        return self.role==role
    
    @staticmethod
    def get_by_username(username):
        return User.query.filter_by(username=username).first()