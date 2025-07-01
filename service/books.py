from data import books as data


def create_book(title, author):
  book = data.create_book(title, author)
  return True


def get_books(book_id=None):
  books = data.get_books()
  if book_id:
    books = [book for book in books if book["book_id"] == book_id]
  return books


def delete_book(book_id):
  book = get_books(book_id)
  if book[0] and book[0]['available'] > 0:
    return data.delete_book(book_id)
  else:
    raise ValueError("Book not available or does not exist")
