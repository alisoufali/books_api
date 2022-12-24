import fastapi
from fastapi.requests import Request

from exceptions.book import NegativeBookNumberException


class BookExceptionHandlers:

    @staticmethod
    def add_exception_handlers(api: fastapi.FastAPI):
        @api.exception_handler(NegativeBookNumberException)
        async def negative_book_number_exceptin_handler(
                request: Request, exception: NegativeBookNumberException):
            content = {"detail": f"The {exception.number_books} number of "
                                 f"books is an invalid number"}
            headers = {"X-Header_Error": "Invalid (negative) number of books"}
            response = fastapi.responses.JSONResponse(
                content=content,
                status_code=418,
                headers=headers
            )
            return response
