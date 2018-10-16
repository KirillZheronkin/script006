from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from script006.databases.alchemy import User

if __name__ == '__main__':
    engine = create_engine('sqlite:///test.db', echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    u = User("mk", "Mikhail Koshel", "123321")
    session.add(u)
    print(u)
    print(u.id)
    session.commit()
    print(u.id)
    session.add_all(
        [
            User("kolia", "Cool Kolian[S.A.]","kolia$$$"),
            User("zina", "Zina Korzina", "zk18")
        ]
    )
    print(session.new)
    mk = session.query(User).filter_by(name="mk").first()
    mk.password = 2
    print(session.dirty)
    session.commit()
    users = session.query(User).all()
    for u in users:
        print(u)



