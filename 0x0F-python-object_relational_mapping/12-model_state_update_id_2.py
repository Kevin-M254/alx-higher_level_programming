#!/usr/bin/python3
"""
  updates name of State object id=2 in hbtn_0e_6_usa
"""

import sys
from unicodedata import name
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost:3306/{}"
            .format(sys.argv[1], sys.argv[2], sys.argv[3]),
            pool_pre_ping=True)
    session_maker = sessionmaker(bind=engine)
    session = session_maker()

    state = session.query(State).filter_by(id=2).first()
    state.name = "New Mexico"
    session.commit()
