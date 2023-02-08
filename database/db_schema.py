
from sqlalchemy.sql import func
from flask_login import UserMixin
# from database.db_logic import DataBase
from app_connector import db


class Admin(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30), nullable = False)
    email = db.Column(db.String(80),unique = True,nullable = False)
    password = db.Column(db.String(100))
    created_date = db.Column(db.DateTime(timezone = True),default= func.now()) 
    payloads = db.relationship('Payload')
    
class Payload(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    hotel_name = db.Column(db.String(100), nullable = False)
    review = db.Column(db.String(100), nullable = False)
    hotel_country = db.Column(db.String(100), nullable = False)
    hotel_city = db.Column(db.String(100), nullable = False)
    hotel_address = db.Column(db.String(100), nullable = False)
    expected_impression = db.Column(db.String(100), nullable = False)
    bert_impression = db.Column(db.String(100), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('admin.id'))
    created_at = db.Column(db.DateTime(timezone = True), default =func.now())
