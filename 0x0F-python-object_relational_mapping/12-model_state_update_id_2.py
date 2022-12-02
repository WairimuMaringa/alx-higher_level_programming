#!/usr/bin/python3
"""
List all state objects from a database.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def mysqlconnect(username, password, database, port=3306):
    """Function: connect ot MySQL

    Args:
    username(str): username to connect to MySQL
    password(str): password to connect to MySQL
    database(str): databse to connect to MySQL
    port(int): port to connect to MySQL

    Return:
    connect to MySQL
    """
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:{}/{}'.format(
                username,
                password,
                port,
                database),
            pool_pre_ping=True)
    bd_session = sessionmaker(bind=engine)
    return bd_session()


if __name__ == '__main__':
    bd_session = mysqlconnect(sys.argv[1], sys.argv[2], sys.argv[3])

    state = bd_session.query(State).filter(State.id == 2).first()

    if state:
        state.name = 'New Mexico'
        bd_session.commit()
