from app import db

class Task(db.Model):
    id = db.column(db.integer , primary_key = True)
    name = db.column(db.string(50), nullable=False)
    status = db.column(db.string(50), nullable = False, default='pending')
