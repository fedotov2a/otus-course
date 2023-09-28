import json
import csv
from pathlib import Path


class BooksDistributor:
    def __init__(self, path_to_users, path_to_books, path_to_results='result.json'):
        self.path_to_users = Path(path_to_users).resolve()
        self.path_to_books = Path(path_to_books).resolve()
        self.path_to_results = path_to_results
        self.users = []
        self.load_users()

    def load_books(self):
        with open(self.path_to_books, 'r') as fd:
            books_reader = csv.DictReader(fd)
            books_reader.fieldnames = [header.lower() for header in books_reader.fieldnames]

            for book in books_reader:
                del book['publisher']
                book['pages'] = int(book['pages'])
                yield book

    def load_users(self):
        with open(self.path_to_users, 'r') as fd:
            for user in json.load(fd):
                user_entry = {
                    'name': user['name'],
                    'gender': user['gender'],
                    'address': user['address'],
                    'age': int(user['age']),
                    'books': []
                }
                self.users.append(user_entry)

    def save_result(self):
        with open(self.path_to_results, 'w') as fd:
            json.dump(self.users, fd, indent=4)

    def count_books(self):
        with open(self.path_to_books) as fd:
            return sum(1 for _ in fd) - 1

    def distribute_v1(self):
        """Раздаёт книги по одной"""

        for i, book in enumerate(self.load_books()):
            self.users[i % len(self.users)]['books'].append(book)

    def distribute_v2(self):
        """Раздаёт книги пачками, затем остатки по одной книге с начала очереди"""

        all_books = self.load_books()
        count_books = self.count_books()
        distributed = 0

        count_books_for_every_person = count_books // len(self.users)

        while distributed != len(self.users) * count_books_for_every_person:
            books = [next(all_books) for _ in range(count_books_for_every_person)]

            user_index = distributed // count_books_for_every_person
            distributed += count_books_for_every_person

            self.users[user_index]['books'] = books

        count_people_who_get_one_book = count_books % len(self.users)

        for i in range(count_people_who_get_one_book):
            self.users[i]['books'].append(next(all_books))


if __name__ == '__main__':
    distributor = BooksDistributor(
        path_to_users='resources/users.json',
        path_to_books='resources/books.csv'
    )
    distributor.distribute_v1()
    distributor.save_result()
