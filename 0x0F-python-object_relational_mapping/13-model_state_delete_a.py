#!/usr/bin/python3
"""delete State objs w/ name containing 'a' from hbtn_0e_6_usa db."""


if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    dlink = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"

    engine = create_engine(dlink)
    Session = sessionmaker(bind=engine)

    session = Session()

    search_term = 'a'
    state_objs = session.query(State).filter(State.name.contains('a')).all()

    for state in state_objs:
        session.delete(state)

    session.commit()

    session.close()
