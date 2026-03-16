from database import db
from datetime import datetime

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(100))
    description = db.Column(db.String(200))
    date = db.Column(db.Date, default=datetime.utcnow)