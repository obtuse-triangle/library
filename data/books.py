from . import con, cur


def _row_to_dict(row):
  return {
      "book_id": row[0],
      "title": row[1],
      "author": row[2],
      "available": row[3]
  }


def create_book(title, author):
  sql = "insert or ignore into books(title, author) values (?, ?)"
  cur.execute(sql, (title, author))
  con.commit()
  return True


def get_books():
  sql = "select * from books where available > 0"
  cur.execute(sql)
  rows = cur.fetchall()
  return [_row_to_dict(row) for row in rows]


def delete_book(book_id):
  sql = "delete from books where book_id = ?"
  cur.execute(sql, (book_id,))
  con.commit()
  return True
