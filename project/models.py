#	project/models.py
from project import db
import datetime


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    fio = db.Column(db.String, unique=False, nullable=False)
    adress = db.Column(db.String, unique=False, nullable=False)
    phone = db.Column(db.String, unique=False, nullable=False)
    name = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    role = db.Column(db.String, default='user')
    id_inst = db.Column(db.Integer, unique=False, nullable=False)
    id_subscr = db.Column(db.Integer, unique=False, nullable=False)
    fan = db.relationship('Fan', backref='poster')


    def __init__(self, fio=None, adress=None, phone=None, name=None, email=None, password=None, role=None, id_inst=None, id_subscr=None):
        self.fio = fio
        self.adress = adress
        self.phone = phone
        self.name = name
        self.email = email
        self.password = password
        self.role = role
        self.id_inst = id_inst
        self.id_subscr = id_subscr

    def	__repr__(self):
        return '<User {0}>'.format(self.name)


class Fan(db.Model):
    __tablename__ = "fan"
    id_inst = db.Column(db.Integer, primary_key=True)
    date_inst = db.Column(db.Date, nullable=False)
    sat_net = db.Column(db.Integer, nullable=False)
    positions = db.Column(db.String, nullable=False)
    convertors = db.Column(db.String, nullable=False)
    resivers = db.Column(db.String, nullable=False)
    add_net = db.Column(db.String, nullable=False)
    add_terr = db.Column(db.String, nullable=False)
    access = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, date_inst, sat_net, positions, convertors, resivers, add_net, add_terr, access, user_id):
        self.date_inst = date_inst
        self.sat_net = sat_net
        self.positions = positions
        self.convertors = convertors
        self.resivers = resivers
        self.add_net = add_net
        self.add_terr = add_terr
        self.access = access
        self.user_id = user_id

    def __repr__(self):
        return '<id_inst {0}>'.format(self.id_inst)

class Subscr(db.Model):
    __tablename__ = "subscr"
    id_subscr = db.Column(db.Integer, primary_key=True)
    date_subscr = db.Column(db.Date, default=datetime.datetime.utcnow())
    provider = db.Column(db.String, nullable=False)
    class_subscr = db.Column(db.String, nullable=False)
    date_end_subscr = db.Column(db.Date, default=datetime.datetime.utcnow())
    costs = db.Column(db.String, nullable=False)
    balance = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, date_subscr, provider, class_subscr, date_end_subscr, costs, balance, user_id):
        self.date_subscr = date_subscr
        self.provider = provider
        self.class_subscr = class_subscr
        self.date_end_subscr = date_end_subscr
        self.costs = costs
        self.balance = balance
        self.user_id = user_id

    def __repr__(self):
        return '<id_subscr {0}>'.format(self.id_subscr)

