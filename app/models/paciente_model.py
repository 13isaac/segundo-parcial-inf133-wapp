from database import db
from flask_login import UserMixin

class Paciente(UserMixin, db.Model):
    __tablename__="pacientes"

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50),nullable=False)
    lastname=db.Column(db.String(50),nullable=False)
    ci=db.Column(db.String(50),nullable=False)
    birth_date=db.Column(db.String(50),nullable=False)

    def __init__(self,name,lastname,ci,birth):
        self.name=name
        self.lastname=lastname
        self.ci=ci
        self.birth_date=birth

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit(self)

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Paciente.query.all()
    
    