from myproject import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model,UserMixin):

    __tablename__="USER"

    id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(64),unique=True,index=True)
    username=db.Column(db.String(64),unique=True,index=True)
    hashed_password=db.Column(db.String(128))

    def __init__(self,email,username,hashed_password):
        self.email=email
        self.username=username
        self.hashed_password=generate_password_hash(hashed_password)

    def check_pass(self,password):
        return check_password_hash(self.hashed_password,password)
