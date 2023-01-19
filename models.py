import os
import datetime
from sqlalchemy import Column, String, Integer, Boolean, DateTime
from flask_sqlalchemy import SQLAlchemy 
import json
import app 
from flask_login import UserMixin

#first name 
#last name 
#number 
#email 
#password 


db = SQLAlchemy()

class Notification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    massage = db.Column(db.String(400))
    date_time = db.Column(db.DateTime)

    def __init__(self,massage ,date_time):
        self.massage = massage
        self.date_time = date_time
       


class Recording(db.Model):
    _tablename_ = 'recording'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    data = db.Column(db.LargeBinary)
    mimetype = db.Column(db.String(255))
    

    def __init__(self,name , data, mimetype):
        self.name = name
        self.data=data
        self.mimetype=mimetype
        
        
#Camera_Table
class Camera_Table(db.Model):
    __tablename__ = 'Camera_Table'
    id = Column(Integer, primary_key=True)
    camera_name = db.Column(db.String(102))
    camera_ip = db.Column(db.String(30)) 
    physical_location=db.Column(db.String(50))  
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    def __init__(self,camera_name ,camera_ip,physical_location ,user_id):
        self.camera_name = camera_name
        self.camera_ip = camera_ip
        self.physical_location=physical_location
        self.user_id = user_id



class Contact(db.Model):
    __tablename__ = 'contact'
    id = Column(Integer, primary_key=True)
    email = db.Column(db.String(40))
    name = db.Column(db.String(102))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    def __init__(self,name ,email ,user_id):
        self.name = name
        self.email = email
        self.user_id = user_id




class Users(db.Model,UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(255))
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    phone = db.Column(db.String(121))


    def __init__(self,email, password ,first_name, last_name , phone):
        self.email = email
        self.first_name= first_name
        self.last_name= last_name
        self.password= password
        self.phone = phone
    def insert(self):
        db.session.add(self)
        db.session.commit()
    def update(self):
        db.session.commit()
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def format(self):
        return {
      'id': self.id,
      'email': self.email,
      'password': self.password,
      'first_name': self.first_name,
      'last_name': self.last_name,
      'phone': self.phone,
    }

