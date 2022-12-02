#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb


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
    db_connection = MySQLdb.connect(
            user=username,
            passwd=password,
            db=database,
            port=port)

    return db_connection


if __name__ == '__main__':
    db_connection = mysqlconnect(sys.argv[1], sys.argv[2], sys.argv[3])
    db_cursor = db_connection.cursor()
    db_cursor.execute('''
    SELECT cities.name
    FROM cities
    INNER JOIN states ON cities.state_id = states.id
    WHERE states.name = %(filter1)s;
    ''', {'filter1': sys.argv[4]})

    states = db_cursor.fetchall()
    print(", ".join([state[0] for state in states]))

    db_cursor.close()
    db_connection.close()
