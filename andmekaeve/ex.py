import psycopg2


def create_connection_to_database():
    conn = psycopg2.connect(dbname="postgres", user="pt", password="pt", host="localhost")
    return conn



class Data:

    def __init__(self, link_to_database: str):
        self.connection = create_connection_to_database()
        self.connection.autocommit = True
        self.cursor = self.connection.cursor()
        print(self.cursor)

    def generate_database_table_content(self):
        data = open("/home/peeter/PycharmProjects/StockPredictions/andmekaeve/retail_data.txt", 'r')
        print(data.readline())
        for line in data:
            line = line.split(",")
            insert_statement = f"INSERT INTO peoplebooks (person_id, book_id) \
                                    VALUES (CAST({line[0]} AS INTEGER), CAST({line[1]} AS INTEGER));"
            print(insert_statement)
            self.cursor.execute(insert_statement)
        self.connection.commit()


if __name__ == '__main__':
    # Link has to be in url format for instance jdbc:postgresql://localhost:5432/postgres
    data = Data("jdbc:postgresql://localhost:5432/postgres")
    data.generate_database_table_content()

