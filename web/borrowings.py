from fastapi import APIRouter, Body
from pydantic import BaseModel
from service import borrowings as service

router = APIRouter(prefix="/borrows")


@router.get("")
def test():
  return service.test()


class BorrowingInfo(BaseModel):
  borrower: str
  title: str


@router.post("/")
def create_borrowing(borrowing: BorrowingInfo = Body(...)):
  try:
    return service.create_borrowing(borrowing.title, borrowing.borrower)
  except Exception as e:
    print(f"Error creating borrowing: {e}")
    return False


class BorrowedInfo(BorrowingInfo):
  author: str


@router.get("/{borrower}/books")
def get_borrowed_books(borrower: str):
  return {
    "borrower": borrower,
    "books": service.get_borrowed_books(borrower)
  }


@router.get("/month/{borrow_month}")
def get_borrowings_by_month(borrow_month: int) -> list[BorrowedInfo]:
  try:
    return [BorrowedInfo(**i) for i in service.get_borrowings_by_month(borrow_month)]
  except Exception as e:
    print(f"Error retrieving borrowings: {e}")
    return []


returnRouter = APIRouter(prefix="/return")


@returnRouter.post("/")
def return_borrowing(borrowing_info: BorrowingInfo = Body(...)):
  try:
    return service.return_borrowing(borrowing_info.title, borrowing_info.borrower)
  except Exception as e:
    print(f"Error returning borrowing: {e}")
    return False
