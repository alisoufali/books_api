from fastapi import HTTPException


class BookNotFoundException(HTTPException):
    def __init__(self, book_id: int) -> None:
        detail_message = f"Requested Book with ID = {book_id} was not found"
        headers = {"X-Header_Error": "Book_ID was not found"}
        super().__init__(
            status_code=404,
            detail=detail_message,
            headers=headers)


class NegativeBookNumberException(Exception):
    def __init__(self, number_books: int) -> None:
        self.number_books = number_books
