from flask_sqlalchemy import SQLAlchemy
import uuid

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    citizenshipCard = db.Column(db.Numeric(15), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    lastName = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    password = db.Column(db.String(10), nullable=False)
    conversations = db.relationship('Conversation', order_by='Conversation.timestamp', back_populates='user')

    def __init__(self, citizenshipCard, name, lastName, email, password):
        self.id = str(uuid.uuid4())
        self.citizenshipCard = citizenshipCard
        self.name = name
        self.lastName = lastName
        self.email = email
        self.password = password