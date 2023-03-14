from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from models import Library, Base
from database import CONFIG

engine = create_engine("mysql+mysqlconnector://%s:%s@localhost:3306/%s" %
                       (CONFIG['DB_USER'], CONFIG['DB_PASSWORD'], CONFIG['DB_NAME']))
connection = engine.connect()
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

l1 = Library(name="universitée lyon 2")

# user = User(name='John Doe', email='john.doe@example.com')
# session.add(user)
# session.commit()

# query all users
# users = session.query(User).all()
# for user in users:
#     print(user.name, user.email)
