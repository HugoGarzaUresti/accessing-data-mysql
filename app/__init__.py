from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User

DATABASE_URI = 'mysql+pymysql://user:password@localhost/test_db'

def main():
    engine = create_engine(DATABASE_URI)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    new_user = User(name='John Doe', email='john.doe@example.com')
    session.add(new_user)
    session.commit()

    for user in session.query(User).all():
        print(user)

if __name__ == "__main__":
    main()
