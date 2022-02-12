import psycopg2
import json
import multiprocessing
import copy



class Data:

    def __init__(self):

        # formatted "book1 book2": people count
        self.people_that_own_same_book: dict = {}

        self.dct_people: dict = {}
        self.dct_book: dict = {}
        self.book_set = set()
        self.dicts = []
        self.generate_database_table_content()


    def generate_database_table_content(self):
        data = open("/home/peeter/PycharmProjects/StockPredictions/andmekaeve/retail_data.txt", 'r')
        for line in data:
            line = line.rstrip()
            line = line.split(",")
            self.add_to_ppl_dict(line)
            self.add_to_books_dict(line)

    def add_to_ppl_dict(self, line):
        if line[0] in self.dct_people.keys():
            self.dct_people[line[0]].add(line[1])
        else:
            self.dct_people[line[0]] = set(line[1])

    def add_to_books_dict(self, line):
        if line[1] in self.dct_book.keys():
            self.dct_book[line[1]].add(line[0])
        else:
            self.dct_book[line[1]] = set(line[0])

    def find_how_many_people_have_read_both(self, book1: str, book2: str):
        return len(self.dct_book[book1].intersection(self.dct_book[book2]))

    def count_all_ob_on_book(self, book1, enum, dct: dict):
        for book2 in list(self.dct_book.keys())[enum + 1:]:
            intersection = self.find_how_many_people_have_read_both(book1, book2)
            if intersection > 0:
                dct[f"{book1} {book2}"] = intersection

    def create_a_crossing_table(self):
        dct: dict = {}
        for enum, book1 in enumerate(self.dct_book.keys()):
            self.count_all_ob_on_book(book1, enum, dct)
            if (enum % 1000 == 0 and enum != 0) or enum == len(self.dct_book.keys()) - 1:
                print(enum)
                crosstable = open(f"/home/peeter/PycharmProjects/StockPredictions/andmekaeve/crosstables/{str(enum - 1000).zfill(4)}.json", 'w+')
                dmp = json.dumps(dct)
                crosstable.write(dmp)
                dct.clear()
                crosstable.close()

    def bought_amnt_book(self, book1, book2):
        book1 = str(book1)
        book2 = str(book2)
        strng = book1.rjust(4, "0")
        json_filename = strng[0] + "000.json"
        crosstable = open(f"/home/peeter/PycharmProjects/StockPredictions/andmekaeve/crosstables/" + json_filename, "r+")
        dct: dict = json.loads(crosstable.readline())
        query_str = book1 + " " + book2
        try:
            intersect = dct[query_str]
            return f"{round(intersect / len(self.dct_book.get(book2)), 4) * 100}%"
        except KeyError:
            return "0%"



if __name__ == '__main__':
    # Link has to be in url format for instance jdbc:postgresql://localhost:5432/postgres
    data = Data()
    # data.generate_database_table_content()
    # a = data.find_how_many_people_have_read_both(1, 2)
    # data.create_a_crossing_table()
    print(data.bought_amnt_book(1000, 1082))
