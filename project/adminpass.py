import os
#import unittest

#from project._config import basedir
from project import db, bcrypt
from project.models import User

    def create_admin_user(self):
        new_user = User(
            name='Superman',
            email='admin@realpython.com',
            password=bcrypt.generate_password_hash('str58hzpfywtd'),
            role='admin'
        )
        db.session.add(new_user)
        db.session.commit()

