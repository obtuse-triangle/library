from . import redis_client


def test():
  return "redis connect ok"


def get_borrowed_books(borrower):
  return redis_client.smembers(f"borrower:{borrower}:books")


def add_borrowed_book(borrower, title):
  redis_client.sadd(f"borrower:{borrower}:books", title)
  return True


def remove_borrowed_book(borrower, title):
  redis_client.srem(f"borrower:{borrower}:books", title)
  return True
