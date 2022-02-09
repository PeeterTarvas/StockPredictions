import sqlite3
from sqlite3 import Error


def create_connection_to_database(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


class Data:

    def __init__(self, link_to_database: str):
        self.connection = create_connection_to_database(link_to_database)


if __name__ == '__main__':
    # Link has to be in url format for instance jdbc:postgresql://localhost:5432/postgres
    data = Data("jdbc:postgresql://localhost:5432/postgres")
