from app import db

class user_credentials(db.model):
    username = db.column(db.string(50), primary_key=True)
    password = db.column(db.stirng(50), nullable =False)