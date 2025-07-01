from data import borrowings as data
from data import books as book_data
from cache import borrower as cache


def test():
  db_test = data.test()
  redis_test = cache.test()
  return {"sqlite": db_test, "redis": redis_test}


def create_borrowing(title, borrower):
  # get book_id, borrower_id
  books = book_data.get_books()
  book = next((b for b in books if b["title"] == title), None)
  if not book:
    raise ValueError("Book not found")

  data.create_borrowing(book["book_id"], borrower)
  cache.add_borrowed_book(borrower, title)
  return True


def get_borrowings_by_month(month):
  return data.get_borrowings_by_month(month)


def return_borrowing(title, borrower):
  data.return_borrowing(title, borrower)
  cache.remove_borrowed_book(borrower, title)
  return True


def get_borrowed_books(borrower):
  return cache.get_borrowed_books(borrower)
