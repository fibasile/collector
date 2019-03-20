"""
Define the Attachment model
"""
from . import db
from .abc import BaseModel, MetaBaseModel
from sqlalchemy.orm import relationship


class Attachment(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ The attachment model """
    __tablename__ = 'attachment'
    _id = db.Column(db.Integer, primary_key=True)
    file_url =  db.Column(db.String(300), nullable=False)
    filename =  db.Column(db.String(300), nullable=False)
    description = db.Column(db.String(300))
    size = db.Column(db.Integer)
    content_type =  db.Column(db.String(300))
    document = relationship("Document", back_populates="attachments")

    def __init__(self, file_url, filename, description="", size=0):
        """ Create a new attachment """
        self.file_url = file_url
        self.filename = filename
        self.description = description
        self.size = size