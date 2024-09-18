from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Links(Base):
    __tablename__ = 'links'

    id          = Column(Integer, primary_key=True, index=True)
    name        = Column(String(100), primary_key=True, nullable=False)
    url         = Column(String(250), nullable=False)
    description = Column(String(1000), nullable=False)
    views       = Column(Integer, default=0)
