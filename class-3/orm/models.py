from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Coin(Base):
    __tablename__ = "coin"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=50), nullable=False)
    symbol = Column(String(length=10), nullable=False)
    status = Column(String(length=50), nullable=False)
    type = Column(String(length=50), nullable=False)


class Historical(Base):
    __tablename__ = "historical"

    id = Column(Integer, primary_key=True, autoincrement=True)
    library_id = Column(Integer, ForeignKey("library.id"))
    name = Column(String(length=100), nullable=False)
    type = Column(String(length=50), nullable=False)
    subject = Column(String(length=100), nullable=False)
    publication_year = Column(Integer, nullable=False)
