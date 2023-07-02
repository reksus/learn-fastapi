from sqlalchemy import Column, Integer, String

from db.config import Base

class Book2(Base):
    __tablename__ = 'books2'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    author = Column(String, nullable=False)
    release_year = Column(Integer, nullable=False)