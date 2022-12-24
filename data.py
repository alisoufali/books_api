import random
from collections import OrderedDict

from models.book import BookModel

BOOKS = OrderedDict()


def populate_with_n_random_books(n_books: int = 5):
    for i in range(1, n_books + 1):
        BOOKS[i] = BookModel(
            id=i,
            title=f"Book {i}",
            author=f"Author {i}",
            description=f"Description {i}",
            rating=random.randint(0, 100),
        )
