#!/usr/bin/python3
"""Module to fetch all states with letter a"""

import sys
from model_state import Base, State
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
    state = session.query(State).first()
    for state in session.query(State).filter(State.name.like('%a%')):
        print(f"{state.id}: {state.name}")
