"""
Define the Link model
"""

from . import db
from .abc import BaseModel, MetaBaseModel
from sqlalchemy.orm import relationship

class Link(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ The link model """
    __tablename__ = 'link'
    _id = db.Column(db.Integer, primary_key=True)
    url =  db.Column(db.String(300), nullable=False)
    description = db.Column(db.String(300))
    document = relationship("Document", back_populates="links")

    def __init__(self, url, description=""):
        """Create a Link"""
        self.url = url
        self.description = description
