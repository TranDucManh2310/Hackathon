from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Message(Base):
    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True)
    text = Column(String)
    sender = Column(String)

engine = create_engine('sqlite:///chatbot.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def save_message(text, sender):
    message = Message(text=text, sender=sender)
    session.add(message)
    session.commit()

def get_messages():
    return session.query(Message).all()