from . import con, cur


def test():
  return "sqlite connect ok"


def create_borrowing(book_id, borrower):
  sql = "insert into borrowings(book_id, borrower) values (?, ?)"
  cur.execute(sql, (book_id, borrower))
  sql = "update books set available = available - 1 where book_id = ?"
  cur.execute(sql, (book_id,))
  con.commit()
  return True


def get_borrowings_by_month(month):
  month = f"%-{month:02d}-%"
  sql = "select * from borrowings, books where borrowings.book_id = books.book_id and borrowed_at like ?"
  cur.execute(sql, (month,))
  rows = cur.fetchall()
  print(rows)
  return [{
    "borrow_id": row[0],
    "book_id": row[1],
    "borrower": row[2],
    "borrowed_at": row[3],
    "returned_at": row[5],
    "title": row[6],
    "author": row[7],
    'available': row[8]
  } for row in rows]


def return_borrowing(title, borrower):
  sql = 'select * from borrowings, books where borrowings.book_id = books.book_id and title = ? and borrower = ?'
  cur.execute(sql, (title, borrower))
  row = cur.fetchone()
  if not row:
    print("대출내역없음")
    return False
  sql = 'delete from borrowings where borrow_id = ?'
  cur.execute(sql, (row[0],))
  sql = 'update books set available = available + 1 where book_id = ?'
  cur.execute(sql, (row[1],))
  con.commit()
  return True
