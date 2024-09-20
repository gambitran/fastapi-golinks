from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
from typing import Optional

Base = declarative_base()


class Links(Base):
    __tablename__ = 'links'

    id          = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name        = Column(String(100), nullable=False)
    url         = Column(String(250), nullable=False)
    description = Column(String(250), nullable=False)
    views       = Column(Integer, nullable=False, default=0)


class PostLink(BaseModel):
    name:        str
    url:         str
    description: str


class UpdateLink(BaseModel):
    id:          int
    name:        str
    url:         str
    description: str
    views:       int


class DeleteLink(BaseModel):
    id: int
