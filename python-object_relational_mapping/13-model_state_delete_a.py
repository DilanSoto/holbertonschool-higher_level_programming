#!/usr/bin/python3
"""script that deletes all State objects with a name containing the letter a"""


import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    delete_states = session.query(State).filter(State.name.like('%a%')).all()
    for deleted in delete_states:
        session.delete(deleted)
    session.commit()
    session.close()
