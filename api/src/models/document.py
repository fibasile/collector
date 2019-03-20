"""
Define the User model
"""
from . import db
from .abc import BaseModel, MetaBaseModel
from sqlalchemy.orm import relationship


class Document(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ The Document model """
    __tablename__ = 'user'
    _id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300))
    description = db.Column(db.String(300))
    author = db.Column(db.String(300))
    links = relationship("Link", back_populates="document")
    attachments = relationship("Attachment", back_populates="document")
    
    def __init__(self, title, description=None, author=None):
        """ Create a new Document """
        self.title = title
        self.description = description
        self.author = author




