from flask_sqlalchemy import SQLAlchemy
from .users import User
db = SQLAlchemy()

class Conversation(db.Model):
    __tablename__ = 'conversations'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    message = db.Column(db.Text, nullable=False)
    response = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())


    user = db.relationship('User', back_populates='conversations')
User.conversations = db.relationship('Conversation', order_by=Conversation.timestamp, back_populates='user')
