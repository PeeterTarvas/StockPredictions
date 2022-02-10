import psycopg2


def create_connection_to_database():
    conn = psycopg2.connect(dbname="postgres", user="pt", password="pt", host="localhost")
    return conn



class Data:

    def __init__(self):
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

    def get_how_many_have_bought_both_books(self, book1, book2):
        select_statement = f"WITH first AS ( \
                                SELECT person_id, book_id AS first_book \
                                FROM peoplebooks \
                                WHERE book_id = {book1} \
                                ), second AS ( \
                                SELECT person_id, book_id AS second_book \
                                FROM peoplebooks \
                                WHERE book_id = {book2} \
                                ) \
                            SELECT COUNT(first.person_id) \
                            FROM first, second \
                            WHERE first.person_id = second.person_id;"
        self.cursor.execute(select_statement)
        return self.cursor.fetchone()[0]

    def generate_grid_table(self):
        all_books_ids = " SELECT book_id \
                          FROM peoplebooks\
                          GROUP BY book_id\
                          ORDER BY book_id"
        self.cursor.execute(all_books_ids)
        ids = self.cursor.fetchall()
        for i in ids:
            i = i[0]
            for j in ids[i + 1:]:
                j = j[0]

                print(f"{i}, {j}: {self.get_how_many_have_bought_both_books(i, j)}")




if __name__ == '__main__':
    # Link has to be in url format for instance jdbc:postgresql://localhost:5432/postgres
    data = Data()
    # data.generate_database_table_content()
    # print(data.get_how_many_have_bought_both_books(10, 38))
    print(data.generate_grid_table())

