#!/usr/bin/python3
"""add State obj `Louisiana` to hbtn_0e_6_usa db."""


if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    dlink = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"

    engine = create_engine(dlink)
    Session = sessionmaker(bind=engine)

    session = Session()

    state_add = State(name='Louisiana')
    session.add(state_add)

    session.commit()

    print(state_add.id)

    session.close()
