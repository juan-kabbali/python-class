from sqlalchemy import Column, Integer, Float, String, ForeignKey, DateTime, Date
from sqlalchemy.dialects.mysql import FLOAT as MY_SQL_FLOAT, JSON
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Coin(Base):
    __tablename__ = "coin"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=100), nullable=False)
    symbol = Column(String(length=20), nullable=False)
    status = Column(String(length=50), nullable=False)
    category = Column(String(length=50), nullable=True)
    tags = Column(JSON, nullable=True)
    website = Column(String(length=256), nullable=True)
    twitter = Column(String(length=256), nullable=True)
    chat = Column(String(length=256), nullable=True)
    reddit = Column(String(length=256), nullable=True)
    source_code = Column(String(length=256), nullable=True)
    date_launched = Column(DateTime, nullable=True)


class Historical(Base):
    __tablename__ = "historical"

    date = Column(Date, primary_key=True)
    coin_id = Column(Integer, ForeignKey("coin.id"), primary_key=True)
    rank = Column(Integer, nullable=False)
    market_cap = Column(MY_SQL_FLOAT(unsigned=True), nullable=True)
    price = Column(Float, nullable=False)
    high = Column(Float, nullable=True)
    low = Column(Float, nullable=True)
    close = Column(Float, nullable=True)
    percent_change_1h = Column(Float, nullable=True)
    percent_change_24h = Column(Float, nullable=True)
    percent_change_7d = Column(Float, nullable=True)
