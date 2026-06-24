#!/usr/bin/python3
"""Module to fetch all city objects"""

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine(
        f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}"
        f"@localhost:3306/{sys.argv[3]}",
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)

    Session = sessionmaker(engine)
    session = Session()

    data = session.query(State, City).filter(
        City.state_id == State.id
    ).order_by(City.id).all()

    for state, city in data:
        print(f"{state.name}: ({city.id}) {city.name}")
    session.close()
