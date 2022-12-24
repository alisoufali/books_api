import fastapi
from fastapi.encoders import jsonable_encoder

from data import BOOKS
from exceptions.book import BookNotFoundException, NegativeBookNumberException
from models.book import BookModel, BookModelNoID


router = fastapi.APIRouter(prefix="/book", tags=["book"])


@router.get("/all", status_code=200, response_model=list[BookModel])
async def get_all_books(books_to_return: int | None = None):
    if books_to_return is not None and (books_to_return < 0):
        raise NegativeBookNumberException(number_books=books_to_return)
    if books_to_return is not None and len(BOOKS) > books_to_return > 0:
        n_books = books_to_return
    else:
        n_books = len(BOOKS)
    content = [None] * n_books
    counter = 1
    for book_index, book in enumerate(BOOKS.values()):
        if counter > n_books:
            break
        content[book_index] = book
        counter += 1
    content = jsonable_encoder(content)
    response = fastapi.responses.JSONResponse(content=content,
                                              status_code=200)
    return response


@router.get("/{book_id}", status_code=200, response_model=BookModel)
async def get_book(book_id: int):
    if book_id not in BOOKS.keys():
        raise BookNotFoundException(book_id=book_id)
    content = BOOKS[book_id]
    content = jsonable_encoder(content)
    response = fastapi.responses.JSONResponse(content=content,
                                              status_code=200)
    return response


@router.post("/", status_code=201, response_model=BookModel)
async def create_book(book: BookModelNoID):
    print(book)
    book_id = max(BOOKS.keys()) + 1
    created_book = BookModel(
        id=book_id,
        title=book.title,
        author=book.author,
        description=book.description,
        rating=None,
    )
    BOOKS[book_id] = created_book
    content = jsonable_encoder(BOOKS[book_id])
    response = fastapi.responses.JSONResponse(content=content,
                                              status_code=201)
    return response


@router.put("/", status_code=201, response_model=BookModel)
async def update_book(book_id: int, book: BookModel):
    if book_id not in BOOKS.keys():
        raise BookNotFoundException(book_id=book_id)
    BOOKS[book_id] = book
    content = jsonable_encoder(BOOKS[book_id])
    return fastapi.responses.JSONResponse(content=content,
                                          status_code=201)


@router.delete("/", status_code=200, response_model=str)
async def delete_book(book_id: int):
    if book_id not in BOOKS.keys():
        raise BookNotFoundException(book_id=book_id)
    del BOOKS[book_id]
    content = f"Book with ID = {book_id} has been removed successfully!"
    response = fastapi.responses.PlainTextResponse(content=content,
                                                   status_code=200)
    return response
