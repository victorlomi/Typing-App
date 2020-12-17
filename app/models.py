from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login
from datetime import datetime

class User(UserMixin):
    def __init__(self, email, password):
        self.email = email 
        self.password = password

@login.user_loader
def load_user():
    return User()
