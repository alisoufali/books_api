import fastapi
import uvicorn

from apis import book
from config import Config
from views import home
from exception_handlers.book import BookExceptionHandlers


api = fastapi.FastAPI()

api.include_router(home.router)
api.include_router(book.router)
BookExceptionHandlers.add_exception_handlers(api=api)


if __name__ == "__main__":
    Config.configure()
    uvicorn.run(api, host="0.0.0.0", port=8000)
else:
    Config.configure()
