#!/usr/bin/python3
"""lists all city objects from hbtn_0e_14_usa database."""


if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    from model_city import City

    dlink = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"

    engine = create_engine(dlink)
    Session = sessionmaker(bind=engine)

    session = Session()

    city_objs = session.query(City).all()
    for city in city_objs:
        print(f"{city.parent.name}: {city.id} {city.name}")

    session.close()
