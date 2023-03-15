from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func

from models import Base, Coin, Historical
from dataset.data import coins, historical_records
from database import CONFIG

engine = create_engine(
    "mysql+mysqlconnector://%s:%s@localhost:3306/%s" %
    (CONFIG['DB_USER'], CONFIG['DB_PASSWORD'], CONFIG['DB_NAME'])
)

connection = engine.connect()
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# insert coins
for coin in coins:
    c = Coin(id=coin["id"], name=coin["name"], symbol=coin["symbol"], status=coin["status"], category=coin["category"], tags=coin["tags"])
    c_instance = session.query(Coin).filter_by(id=coin["id"]).one_or_none()

    if not c_instance:
        session.add(c)
        session.commit()

# insert historical
for hr in historical_records:
    h = Historical(
        date=hr["date"], coin_id=hr["coin_id"], rank=hr["rank"], market_cap=hr["market_cap"], price=hr["price"],
        high=hr["high"], low=hr["low"], close=hr["close"], percent_change_1h=hr["percent_change_1h"],
        percent_change_24h=hr["percent_change_24h"], percent_change_7d=hr["percent_change_7d"])

    h_instance = session.query(Historical).filter_by(date=hr["date"], coin_id=hr["coin_id"]).one_or_none()

    if not h_instance:
        session.add(h)
        session.commit()

# get all coins
coins = session.query(Coin).all()
for coin in coins:
    print(f"--> {coin.name} {coin.__dict__}")

# count coins
print(f"--> total number of coins {session.query(Coin).count()}")

# market cap average for bitcoin
bitcoin = session.query(Coin).filter_by(symbol="BTC").one_or_none()
bitcoin_historical = session.query(Historical).filter_by(coin_id=bitcoin.id)

sum = 0
for bh in bitcoin_historical:
    sum += bh.market_cap
avg = sum / bitcoin_historical.count()
print(f"average --> {avg}")

# market cap average for bitcoin using mysql avg aggregation
avg = session.query().with_entities(func.avg(Historical.market_cap).label('market_cap_avg')).filter_by(coin_id=bitcoin.id)
print(f"generate avg sql -->")
print(avg)
print(f"query result --> {avg.all()}")
