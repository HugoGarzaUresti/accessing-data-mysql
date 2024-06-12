from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base, User

DATABASE_URI = 'mysql+pymysql://user:password@localhost/test_db'

def setup_database():
    engine = create_engine(DATABASE_URI)
    Base.metadata.create_all(engine)
    return engine

def add_user(engine, name, email):
    Session = sessionmaker(bind=engine)
    session = Session()
    new_user = User(name=name, email=email)
    session.add(new_user)
    session.commit()
    session.close()

def get_users(engine):
    Session = sessionmaker(bind=engine)
    session = Session()
    users = session.query(User).all()
    session.close()
    return users
