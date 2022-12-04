#!/usr/bin/python3
"""
Improve model city and model state files.
"""
import sys
from relationshipl_state import Base, State
from relationship_city import City
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
    Base.metadata.create_all(engine)
    bd_session = sessionmaker(bind=engine)
    return bd_session()


if __name__ == '__main__':
    bd_session = mysqlconnect(sys.argv[1], sys.argv[2], sys.argv[3])
    new_state = State(name='California')
    new_city = City(name='San Francisco')
    new_state.cities.append(new_city)

    bd_session.add(new_state)
    bd_session.add(new_city)
    bd_session.commit()
