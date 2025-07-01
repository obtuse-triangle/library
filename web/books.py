from fastapi import APIRouter, Body
from pydantic import BaseModel
from service import books as service


router = APIRouter(prefix="/books")


class BookInfo(BaseModel):
  title: str
  author: str


@router.post("/")
def create_book(book: BookInfo = Body(...)):
  try:
    return service.create_book(book.title, book.author)
  except Exception as e:
    print(f"Error creating book: {e}")
    return False


@router.get("/")
def get_books() -> list[BookInfo]:
  try:
    return [BookInfo(**i) for i in service.get_books()]
  except Exception as e:
    print(f"Error retrieving books: {e}")
    return []


@router.delete("/{book_id}")
def delete_book(book_id: int):
  try:
    return service.delete_book(book_id)
  except Exception as e:
    print(f"Error deleting book: {e}")
    return False
