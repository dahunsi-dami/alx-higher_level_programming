#!/usr/bin/python3
"""change name of State obj from hbtn_0e_6_usa db."""


if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    dlink = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"

    engine = create_engine(dlink)
    Session = sessionmaker(bind=engine)

    session = Session()

    state = session.query(State).filter_by(id=2).first()
    state.name = "New Mexico"

    session.commit()

    session.close()
